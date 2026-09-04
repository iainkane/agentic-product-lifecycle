# Agentic Product Lifecycle contributor guidance

This repository contains project-neutral lifecycle contracts, schemas, templates,
and agent skills. Do not add a customer's domain policy, infrastructure names,
credentials, private data, deployment targets, or organization-specific approval
roles to the core.

Before changing a lifecycle contract, identify which adopting-project behaviour
will change. Keep human policy in project overlays. Maintain backward compatibility
for published schemas unless the change is intentionally versioned.

Prefer adapting an established, maintained capability over creating a duplicate.
Record provenance, licence, version, local modifications, and the reason for any
replacement. Third-party tools must not silently change branches, publish,
deploy, or send project data externally.

Run `python3 scripts/validate.py` after changing schemas, templates, or skills.
Do not describe a workflow as validated solely because its files exist.
