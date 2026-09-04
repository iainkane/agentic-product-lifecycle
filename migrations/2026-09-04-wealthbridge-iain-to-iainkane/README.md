# Wealthbridge-iain to iainkane migration

Status: Account renamed; repository migrations in progress

## Change identity

- Change ID: `OWNER-RENAME-2026-09-04`
- Old owner: `Wealthbridge-iain`
- New owner: `iainkane`
- Account type: Personal GitHub account
- Intent: Establish a durable personal identity for a public AI portfolio and
  open-source projects now that the Wealthbridge identity is retired.

## GitHub-confirmed effects

- Repository web and Git access receive redirects.
- The old profile page and Pages sites do not receive redirects.
- Redirects are compatibility support; canonical references still need updating.

## Local discovery snapshot

The scan excluded `.git`, dependency folders, and Python environments. Counts are
a routing aid and must be refreshed before editing.

| Repository | Matching files | Approx. occurrences | Dirty entries | Initial risk |
| --- | ---: | ---: | ---: | --- |
| `Tap.Scot` | 9 | 35 | 1 | High: deployment/workload identity references |
| `gcp-local-ai-adult-ops` | 6 | 10 | 0 | Medium: cross-repository links |
| `gcp-local-ai-content-ops` | 6 | 7 | 0 | Medium: cross-repository links |
| `vega-trading-v2` | 29 | 220 | 0 | Critical: CODEOWNERS, workflows and deployment scripts |

## Repository migration order

1. `vega-trading-v2`: update ownership and active automation first; verify
   CODEOWNERS, API calls, deployment identity and GitHub integrations.
2. `Tap.Scot`: preserve unrelated local work; verify GitHub workload-identity
   repository claims and build deployment before documentation cleanup.
3. `gcp-local-ai-content-ops`: update its remote and reciprocal links.
4. `gcp-local-ai-adult-ops`: update its remote and reciprocal links.
5. Publish `agentic-product-lifecycle` under `iainkane` after the rename.

Each repository uses `templates/repository-owner-rename.md` as its change record.
Changes are made independently through that repository's normal branch, review,
test, and deployment controls. Historical records are not rewritten merely to
remove the former username.

## Account-level preflight

- [x] Confirm authenticated account is `Wealthbridge-iain`.
- [x] Confirm `iainkane` is accepted by GitHub's rename form.
- [x] Inventory local repositories and owner references.
- [x] Establish repository-specific change specification.
- [x] Confirm final account rename submission.
- [x] Rename account.
- [x] Verify repositories resolve in the new namespace.
- [x] Update local remotes and verify read access.
- [ ] Complete repository-specific active-configuration migrations.
- [ ] Check profile, Pages, packages, images, Actions, apps and integrations.
- [x] Publish the public lifecycle repository under Apache 2.0.

## Known issue

The first `agentic-product-lifecycle` GitHub Actions run was not started because
GitHub reports that the account is locked due to a billing issue. Local validation
passes; hosted CI remains unverified until the account-level billing issue is
resolved and the workflow is rerun.
