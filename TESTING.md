# Validation scope

Run from the repository root:

```sh
python3 tests/check_repository.py
python3 -m unittest discover -s tests -p "test_*.py" -v
```

The hygiene check checks required files, a small set of credential patterns,
prohibited evidence-file extensions, and Bash syntax. It is not a full secret
scanner. Behavioral tests use disposable synthetic inputs and command mocks.
PowerShell tests also parse all shipped scripts. Tests must fail with a nonzero
exit code on failed assertions. No test signs into a tenant, reads a real
keychain, runs Moodle cron, contacts Gemini, or changes hosting settings.

CI runs on Linux with Bash, Python and PowerShell supplied by the hosted runner.
Windows PowerShell 5.1 and native macOS behavior need separate target-system
validation. Review the Actions run for the exact commit before claiming checks
passed. These checks do not establish production compatibility or recovery.
