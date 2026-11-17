# Security and safe operation

These diagnostics do not remediate production systems. Review commands and use a
disposable test environment before running them under an approved support task.
Use ordinary user permissions; do not elevate just to bypass a failed check.
Only choose trusted local executables. A PHP or Node executable is still code.

Never commit private keys, PFX/P12 bundles, cookies, tokens, connection strings,
customer names, tenant/application identifiers, student data, mailbox content,
hostnames, raw logs, backups, or screenshots from client environments. The
repository contains incident summaries and synthetic tests, not original logs.
Diagnostic output may be sensitive even when a command is read-only. Keep it
locally in restricted storage and share only manually redacted summaries.
The ignore rules and heuristic scan are supplementary controls, not proof that
a file is safe to publish.

For a vulnerability, use GitHub private vulnerability reporting if this repo
offers it. Otherwise open an issue requesting a private contact without any
exploit, credentials, or customer evidence. Do not assume private reporting is
enabled. If a secret was exposed, revoke/rotate it with the owner first; deleting
a commit alone does not remove exposure from clones or caches.

CI uses synthetic inputs, a read-only repository token, no production secrets,
and no scheduled access to customer services. A passing workflow establishes
only the checks described in TESTING.md, never incident resolution.
