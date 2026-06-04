# Seal Review Process v0.1

## 1. Purpose

The Seal Review Process defines how AEP results are reviewed before becoming industrial dependencies.

## 2. Roles

### Executor

The agent, human, or automation that performs the AEP.

### Evidence Builder

The person or agent that assembles PoEW, Gate result, logs, summaries, hashes, and artifacts.

### Seal Reviewer

The person or automated verifier that makes the final closure decision.

### Downstream Owner

The person or agent responsible for the next AEP/NEM that will depend on this result.

## 3. Review flow

```text
1. Executor completes function
2. Evidence Builder assembles PoEW and Gate evidence
3. Seal Reviewer checks the Seal Checklist
4. Downstream Owner confirms dependency safety
5. Final decision is recorded
```

## 4. Review decisions

| Decision | Meaning |
|---|---|
| PASS | Industrial Done |
| PASS_WITH_LIMITATIONS | Industrial Done, but with bounded usage |
| HOLD | Evidence incomplete |
| REOPEN_REQUIRED | Implementation or validation must continue |
| REJECTED | Output should not be used |

## 5. Evidence-first rule

No reviewer should approve an AEP based only on AI summary.

Minimum evidence must include:

- Direct output artifact.
- Execution log.
- PoEW reference.
- Gate result.
- Risk note.
- Downstream dependency note.

## 6. Human + automated review

AEP-NEM can support both human and automated reviewers.

Recommended split:

| Area | Best reviewer |
|---|---|
| Syntax / schema | Automated verifier |
| Logs / hashes | Automated verifier |
| Test pass/fail | Automated verifier |
| Risk interpretation | Human reviewer |
| Product direction | Human reviewer |
| Downstream dependency | Human + owner |

## 7. Multi-center review

Because AEP-NEM is designed for decentralized and multi-center engineering, Seal Review should not require a single central authority.

Any center may issue a Seal decision, but the decision must include:

- Reviewer identity.
- Evidence references.
- Decision reason.
- Reopen criteria.
- Scope of validity.

## 8. Seal validity scope

A Seal decision must declare its scope.

Examples:

```text
Valid for runtime infrastructure only.
Valid for test dataset only.
Valid for internal use only.
Valid for production NEM dependency.
Valid for public release.
```

## 9. Reopen governance

An Industrial Done AEP can be reopened when:

- New evidence contradicts the original Seal.
- Downstream dependency fails.
- Security issue appears.
- Artifact cannot be reproduced.
- Gate logic changes.
- Project direction changes.

## 10. Governance principle

> Seal is not bureaucracy. Seal is engineering memory.

A well-sealed AEP reduces future uncertainty and prevents hidden debt from spreading across the engineering organism.
