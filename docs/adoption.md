# Adopting the lifecycle

## Before installation

Inventory the project's existing instructions, specifications, workflows, tests,
release process, and installed skills. Record candidate reuse decisions with
`templates/capability-assessment.yaml`. Resolve instruction conflicts before
activating lifecycle routing.

## Project integration

1. Pin this repository by release tag or immutable commit.
2. Add a project-owned overlay based on `templates/project-overlay.yaml`.
3. Reference the pinned lifecycle and overlay from the project's root agent
   instructions. Preserve existing instructions and more-specific directory rules.
4. Install or expose only the lifecycle skills the project will use.
5. Map project commands, required evidence, reviewers, release boundaries, and
   independent domain-production streams in the overlay.
6. Pilot one representative change before making the lifecycle the default.

Suggested routing text:

```text
For application or product changes, use the pinned Agentic Product Lifecycle and
this repository's project overlay. Project policy takes precedence over generic
defaults. Keep independent domain-production processes on their own lifecycle.
No lifecycle state or approval grants permission for a later external action.
```

For projects that use Google Cloud, see the [cloud authentication guide](google-cloud-authentication.md)
when preparing the project runbook and reviewing access changes.

## Updating

Review release notes and schema changes, update the pinned version on a branch,
validate the project overlay, and run a representative lifecycle exercise. Do not
track a moving default branch in governed projects.
