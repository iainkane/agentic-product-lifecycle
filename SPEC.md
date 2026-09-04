# Generic Agentic Product Lifecycle Specification

Status: Draft v0.1.0
Audience: Teams adopting a repeatable, agent-assisted application-development process

## 1. Purpose

Provide a reusable and tool-portable lifecycle that helps teams convert uncertain
requests into explicit intent, testable requirements, approved specifications,
implementation plans, verified changes, controlled releases, and learning.

The framework MUST support existing repositories without requiring them to
rewrite their history or replace established governance.

## 2. Principles

- Intent precedes solution commitment.
- Requirements describe observable needs before technical implementation.
- Every material claim links to evidence.
- Automated evidence and human approval are different states.
- Approval for one stage does not authorize a later external action.
- Project policy overrides generic defaults where the override is explicit.
- Skills are composable operations; the lifecycle contract remains independently
  readable and enforceable.
- Existing maintained capabilities are evaluated before new ones are built.
- The process is proportional to risk and may use project-defined profiles.

## 3. Scope

The framework SHALL provide:

- intake, intent, requirements, specification, planning, handoff, verification,
  review, release-interface, observation, and learning contracts;
- machine-readable records with stable identifiers and traceability;
- reusable skills for the human-agent workflows where judgement is helpful;
- deterministic validation for record structure and lifecycle transitions;
- project overlays for policy, commands, risk profiles, and approval roles;
- adoption alongside existing agent instructions and development tooling;
- provenance and evaluation records for reused third-party capabilities.

The framework SHALL NOT:

- define an adopting project's domain policy;
- grant permission to merge, deploy, publish, contact third parties, or mutate
  live data;
- treat an automated pass as human approval;
- assume one vendor, model, source-control host, CI provider, or deployment stack;
- combine application development with domain-specific production streams such
  as curriculum or editorial content generation.

## 4. Actors

- **Requester:** supplies an initial need or opportunity.
- **Intent owner:** accountable for the desired outcome and priority.
- **Product reviewer:** accepts scope and product requirements.
- **Delivery owner:** accountable for implementation and evidence.
- **Domain reviewer:** applies project-specific security, legal, safety, content,
  accessibility, or operational judgement.
- **Release authority:** authorizes an identified candidate for an identified target.
- **Agent:** prepares artefacts and evidence within the authority granted to it.

One person MAY hold several roles. Role assignment MUST be explicit where an
approval is required.

## 5. Lifecycle states

1. **Intake:** The original request, context, evidence, urgency, and unknowns are
   recorded without presuming the proposed solution is correct.
2. **Intent:** The problem, affected users, desired outcomes, measurable signals,
   constraints, assumptions, and non-goals are made explicit.
3. **Requirements:** Observable functional and quality needs, scenarios, failure
   behaviour, dependencies, and unresolved questions are recorded.
4. **Specification:** Approved intent and requirements are assembled into the
   product contract for the change.
5. **Plan:** Technical choices, tasks, affected contracts, verification, rollout,
   rollback, and project-specific gates are mapped to requirements.
6. **Execute:** The scoped candidate is implemented. Material discoveries update
   upstream artefacts rather than remaining hidden in code.
7. **Verify:** Required automated and manual checks produce attributable results,
   including failures and skips.
8. **Review:** Designated reviewers evaluate the exact candidate and evidence.
9. **Release:** A release authority may authorize an identified candidate for an
   identified environment. Release execution remains a separate permission.
10. **Observe:** Predeclared technical, product, and project-governance signals
    are assessed against success and rollback criteria.
11. **Learn:** Outcomes, defects, incidents, and decisions update a requirement,
    test, skill, policy, or backlog item.

Projects MAY return to an earlier state. They MUST retain the decision and reason.

## 6. Intent and requirements quality

An intent is ready for requirements work when it identifies:

- the problem or opportunity and available evidence;
- affected users and the accountable intent owner;
- desired outcomes and observable success signals;
- constraints, assumptions, non-goals, and open questions;
- why the work is worth considering now.

Requirements are ready for specification review when they are:

- traceable to intent;
- solution-neutral unless a constraint requires a solution;
- observable and testable;
- explicit about failure and boundary cases;
- clear about data, privacy, security, accessibility, compatibility, and
  operational needs when applicable;
- free of unresolved contradictions;
- labelled when an important unknown remains.

## 7. Approval and authorization

Every approval MUST identify the artefact or candidate, approver role, decision,
timestamp, and conditions. Editing an approved artefact invalidates approval when
the changed fields affect its decision basis.

Handoffs MUST state what has been completed, what remains uncertain, what evidence
exists, and the exact decision or action requested. Agents MUST not infer approval
from silence, file presence, test success, or an earlier-stage approval.

## 8. Capability reuse

Before building a capability, maintainers MUST assess suitable existing tools,
skills, templates, or libraries. Each assessment records:

- capability and candidate;
- source, licence, version, and maintenance status;
- data and side-effect behaviour;
- fit with the lifecycle and project overlays;
- decision: adopt, configure, wrap, replace, or build;
- gaps and rationale.

The first implementation SHOULD assess GitHub Spec Kit for specification,
planning, task decomposition, and cross-artefact analysis. Integration SHOULD
use supported presets or extensions where practical rather than copying or
forking upstream behaviour.

## 9. Project overlays

An adopting project MUST define:

- lifecycle version or immutable commit reference;
- risk profiles and classification rules;
- required reviews and approval roles;
- repository commands and evidence sources;
- environment and release boundaries;
- local policies and more-specific instructions;
- any independent domain-production lifecycle.

Generic defaults MUST NOT weaken a project overlay. Conflicts MUST be surfaced.

## 10. Acceptance criteria for v1

- A new and an existing repository can adopt the framework without overwriting
  existing instructions.
- An agent can route an application request through intake, intent, requirements,
  specification, plan, execution, and handoff using discrete skills.
- Records validate against published schemas and retain stable traceability IDs.
- Missing approvals, evidence, unresolved questions, or candidate identity prevent
  an invalid forward transition when required by the project overlay.
- A project can add domain-specific gates without modifying framework core.
- Third-party capability decisions are documented and reproducible.
- At least two distinct projects complete representative pilot changes.
- Tap.Scot application development consumes the generic framework through an
  overlay while its curriculum/content lifecycle remains independently governed.

## 11. Open decisions

- Distribution mechanism: source reference, package, or skill-only plugin.
- Canonical record serialization and signing requirements.
- Whether lifecycle transition validation belongs in CI, a local CLI, or both.
- Minimum supported coding agents and required adapter tests.
- Versioning and migration policy after the two-project pilot.
