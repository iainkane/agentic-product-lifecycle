# Repository Owner Rename Change Specification

Status: Draft

## Change identity

- Change ID: `OWNER-RENAME-YYYY-MM-DD`
- Old owner: `OLD_OWNER`
- New owner: `NEW_OWNER`
- Repository: `OWNER/REPOSITORY`
- Change owner: `NAME_OR_ROLE`
- Planned rename time: `TIMESTAMP_AND_TIMEZONE`

## Intent

Rename the source-control account or organization while preserving repository
access, automation, releases, ownership rules, package consumers, deployment
integrations, and traceability.

## Scope

Included:

- repository URLs and local remotes;
- workflow, API, CLI, badge, documentation, and issue links;
- CODEOWNERS and account mentions;
- package, container, Pages, webhook, app, and deployment references;
- post-rename verification and rollback/escalation evidence.

Excluded unless separately authorized:

- renaming repositories;
- changing repository visibility;
- changing collaborators, teams, permissions, secrets, or environments;
- rotating credentials;
- changing package names or deployment architecture.

## Discovery record

| Area | Current reference | Required action | Risk | Owner | Evidence |
| --- | --- | --- | --- | --- | --- |
| Git remote |  | Update after rename | Low |  |  |
| CODEOWNERS |  | Replace account mention | High |  |  |
| Workflows/API calls |  | Replace owner-qualified references | High |  |  |
| Published Actions |  | Assess consumer compatibility | High |  |  |
| Packages/images |  | Assess namespace consumers | High |  |  |
| Pages/custom domains |  | Verify and update | High |  |  |
| Webhooks/GitHub Apps |  | Verify owner/repository bindings | High |  |  |
| Cloud workload identity |  | Verify repository claim conditions | Critical |  |  |
| Badges/docs/issues |  | Replace durable references | Low |  |  |
| External consumers |  | Notify or update | High |  |  |

## Requirements

- R-001: Record the exact old and new owner names before mutation.
- R-002: Confirm the new name is available and valid on the hosting platform.
- R-003: Inventory local and hosted repositories before the account rename.
- R-004: Identify owner-qualified authorization conditions, including workload
  identity, GitHub App, webhook, and deployment allowlists.
- R-005: Identify published packages, container images, Actions, Pages sites,
  gists, profile links, and username-based no-reply commit identities.
- R-006: Preserve existing repository and branch names unless separately approved.
- R-007: Update each important local remote to the canonical new URL after rename.
- R-008: Update active configuration and ownership references before historical
  documentation where sequencing is required.
- R-009: Preserve historical evidence when changing an old URL would make the
  evidence inaccurate; add a migration note instead.
- R-010: Verify fetch and push authorization without creating an unrelated commit.
- R-011: Verify CI triggers, deployment authentication, CODEOWNERS resolution,
  package pulls, Pages/custom domains, and required integrations where applicable.
- R-012: Record failures, skipped checks, owners, and follow-up dates.
- R-013: Do not treat GitHub redirects as the permanent configuration.
- R-014: Do not delete, transfer, rename, or alter visibility without separate
  explicit authorization.

## Per-repository implementation plan

1. Record clean/dirty status and preserve unrelated work.
2. Capture remotes, default branch, workflows, environments, packages, Pages,
   integrations, protection/rulesets, and owner-qualified references.
3. Classify references as active configuration, current documentation, historical
   evidence, generated/cache data, or external dependency.
4. After the account rename, update the `origin` URL.
5. Change active configuration and CODEOWNERS on a scoped branch.
6. Update current documentation; retain historical truth with migration notes.
7. Run repository-specific checks and inspect the diff.
8. Verify hosted controls and integrations.
9. Merge or release through the repository's normal authorization path.
10. Attach the completed verification record to this change.

## Acceptance criteria

- The repository's canonical remote uses `NEW_OWNER`.
- Fetch succeeds and push authorization is verified safely.
- Active workflows contain no unintended `OLD_OWNER` authorization dependency.
- CODEOWNERS resolves to the new account where used.
- Deployment identity and repository-claim conditions accept the new owner.
- Active package, image, Action, Pages, webhook, and app integrations work.
- Remaining old-owner occurrences are classified and intentionally retained.
- Checks, approvals, failures, and follow-ups are recorded.

## Verification record

| Check | Expected | Result | Evidence |
| --- | --- | --- | --- |
| Canonical remote | New owner URL | Pending |  |
| Fetch | Succeeds | Pending |  |
| Push authorization | Succeeds without unrelated change | Pending |  |
| CI | Required checks trigger and pass | Pending |  |
| CODEOWNERS | New account resolves | Pending |  |
| Deployment identity | New repository claim accepted | Pending |  |
| Packages/images | Consumers verified | N/A or pending |  |
| Pages/custom domain | Serves correctly | N/A or pending |  |
| Integrations | Required integrations healthy | Pending |  |
| Residual reference audit | Every occurrence classified | Pending |  |

## Rollback and escalation

GitHub redirects are a compatibility measure, not a complete rollback. If a
critical integration fails, pause repository changes, retain evidence, restore
the affected integration to a known-working configuration where supported, and
escalate to its owner. Do not attempt to reclaim or rapidly cycle usernames as
an automated rollback.

## Approval

- Repository review: Pending
- Security/deployment review where applicable: Pending
- Change owner acceptance: Pending
