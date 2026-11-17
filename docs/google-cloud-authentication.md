# Google Cloud authentication

## Local operator access

Use an individual organisation-managed Google account with MFA on a trusted
workstation. Let the Google Cloud CLI reuse its saved sign-in. Use a named CLI
configuration and have project commands select the expected account,
configuration and project ID explicitly. Include a read-only connection check and
browser sign-in instructions for when Google requires reauthentication.
[Google Cloud CLI authentication](https://docs.cloud.google.com/sdk/docs/authenticate)

## CI and workloads

- **GitHub Actions.** Exchange GitHub OIDC tokens for short-lived Google Cloud
  credentials through Workload Identity Federation. Restrict trust with numeric
  owner and repository IDs and conditions for the approved workflow and
  environment. Grant the deployment identity only the permissions needed in
  its target environment.
  [Google deployment pipeline guidance](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
- **Cloud Run and other workloads on Google Cloud.** Attach a dedicated service
  account and let the application obtain credentials through Application Default
  Credentials. Give the runtime identity only the resource access it needs and
  assign deployment permissions to a separate identity.
  [Google Cloud authentication](https://docs.cloud.google.com/docs/authentication)

Use separate IAM grants and service identities for production and non-production.
Keep local OAuth caches, tokens, and credential files outside the repository.
Use federation and attached identities for routine automation and avoid
downloaded service account keys.
[Google service account guidance](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)

## Project ownership

Record the permitted project IDs, environment and identity mappings, connection
check, and reauthentication steps in each project's runbook. Keep reviewer roles,
IAM change approvals, and release authority in the project's own policy. Verify
an allowed connection and check that unexpected repositories and environments
are denied before using a new CI trust configuration for deployment.
