import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=next((ROOT/'scripts').glob('*.sh'))
BASH=shutil.which('bash')

class Diagnostics(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)
        self.env=dict(os.environ)
        self.env['PATH']=str(self.path)+os.pathsep+os.environ['PATH']

    def mock(self,name,body):
        path=self.path/name
        path.write_text('#!/bin/sh\n'+body+'\n')
        path.chmod(0o755)
        return str(path)

    def run_script(self):
        return subprocess.run([BASH,str(SCRIPT)],env=self.env,capture_output=True,text=True,timeout=10)

    def test_wrong_platform_is_refused(self):
        self.mock('uname','echo Linux')
        self.mock('security','exit 99')
        result=self.run_script()
        self.assertEqual(result.returncode,2)
        self.assertIn('requires macOS',result.stderr)

    def test_identity_listing_and_safe_arguments(self):
        self.mock('uname','echo Darwin')
        self.mock('sw_vers','echo synthetic-version')
        self.mock('security', "case \"$*\" in 'list-keychains -d user') echo synthetic-keychain;; 'find-identity -v -p ssl-client') echo '0 valid identities found';; *) exit 99;; esac")
        result=self.run_script()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('0 valid identities',result.stdout)
        self.assertIn('does not validate browser login',result.stdout)

    def test_security_failure_is_not_silenced(self):
        self.mock('uname','echo Darwin')
        self.mock('sw_vers','echo synthetic-version')
        self.mock('security', 'exit 7')
        self.assertEqual(self.run_script().returncode,7)

if __name__ == "__main__": unittest.main()
