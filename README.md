# Agentic Product Lifecycle

A project-neutral foundation for intent-led, agent-assisted product development.
It turns an initial request into reviewed intent, requirements, a product
specification, an implementation plan, verified delivery evidence, and durable
learning.

This repository provides process contracts and composable agent skills. Adopting
projects keep ownership of their domain policy, commands, approval roles, and
release controls through a local overlay.

## Lifecycle

```text
Intake -> Intent -> Requirements -> Specification -> Plan -> Execute
       -> Verify -> Review -> Release -> Observe -> Learn
```

The content of a stage may be prepared by an agent. Human approval is required
where the adopting project's policy declares an approval gate. Evidence does
not imply approval, and approval does not imply authorization for a later
external action.

## Start here

1. Read [SPEC.md](SPEC.md).
2. Copy [templates/project-overlay.yaml](templates/project-overlay.yaml) into the
   adopting project and replace its placeholders.
3. Reference a tagged release or commit of this repository from the adopting
   project's agent instructions.
4. Copy or install only the skills needed by that project.
5. Run `python3 scripts/validate.py` in this repository.

The repository currently supplies the portable foundation. Automated installation
and package distribution will be designed after the first real-project pilot.
