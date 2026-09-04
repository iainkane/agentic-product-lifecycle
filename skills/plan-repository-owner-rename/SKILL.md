---
name: plan-repository-owner-rename
description: Inventory and plan a GitHub or source-control owner rename across repositories, producing one reviewable migration record per repository without changing account identity or project configuration unless separately authorized.
---

# Plan a repository owner rename

Read the hosting provider's current official rename guidance. Establish the exact
old and proposed new owner names before any mutation.

Inventory repositories, remotes, active configuration, CODEOWNERS, workflows,
API and CLI calls, deployment identity claims, packages, container images,
published Actions, Pages, webhooks, apps, badges, current documentation, historical
evidence, and external consumers. Do not scan or expose secrets.

Use `templates/repository-owner-rename.md` for each repository. Classify every
old-owner reference before editing it:

- active configuration;
- ownership or authorization;
- current documentation;
- historical evidence;
- generated or Git-internal data;
- external dependency.

Prioritize authorization, CODEOWNERS, CI, deployment, packages, and integrations.
Preserve historical accuracy and unrelated work. Do not globally replace text
across repositories or modify `.git` history and logs.

Account rename, repository transfer, visibility change, permission change, and
deployment are separate actions. Require their applicable authorization at the
time of action. After an authorized rename, update canonical remotes and verify
each repository through its normal review process.
