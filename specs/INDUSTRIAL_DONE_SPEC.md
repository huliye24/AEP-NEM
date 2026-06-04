# Industrial Done Specification v0.1

## 1. Definition

`Industrial Done` is the highest completion state for an AEP.

It means:

> The task is not only implemented, but also verified, reproducible, documented, risk-bounded, and safe for downstream dependency.

## 2. Difference from ordinary Done

| State | Meaning | Risk |
|---|---|---|
| Function Complete | The function exists | Evidence may be weak |
| Gate Passed | Quality checks passed | Closure may still be incomplete |
| Seal Complete | Closure evidence is complete | Needs final decision |
| Industrial Done | Officially dependency-safe | Low operational risk |

## 3. Industrial Done requirements

An AEP must satisfy all `MUST` requirements.

### 3.1 Functional requirements

- MUST have a clearly defined output.
- MUST demonstrate the main usage path.
- MUST satisfy the AEP acceptance criteria.
- SHOULD include at least one realistic usage example.

### 3.2 Evidence requirements

- MUST include a PoEW reference.
- MUST include a Gate result reference.
- MUST include logs or summary output.
- MUST include artifact paths or checksums.
- SHOULD include screenshots, reports, or benchmark tables when relevant.

### 3.3 Reproducibility requirements

- MUST state the execution environment.
- MUST list key dependencies or versions.
- MUST include command or procedure used.
- SHOULD provide deterministic or near-deterministic replay instructions.

### 3.4 Regression requirements

- MUST state whether existing behavior was checked.
- MUST list affected modules.
- MUST state whether any old path was broken.
- SHOULD include before/after comparison.

### 3.5 Risk requirements

- MUST list known limitations.
- MUST list unresolved warnings.
- MUST state whether risks are blocking or non-blocking.
- MUST define reopen triggers.

### 3.6 Downstream requirements

- MUST explain how future AEPs can depend on this output.
- MUST identify stable contracts or interfaces.
- MUST identify unstable areas.
- SHOULD suggest the next AEP/NEM entry point.

## 4. Industrial Done decision matrix

| Condition | Decision |
|---|---|
| Function incomplete | REOPEN_REQUIRED |
| Function complete but evidence missing | HOLD |
| Evidence complete but Gate failed | REOPEN_REQUIRED |
| Gate passed but downstream unsafe | HOLD |
| Minor non-blocking risks documented | PASS_WITH_LIMITATIONS |
| All required conditions satisfied | PASS |

## 5. Completion formula

```text
Industrial_Done =
Function_Complete
× PoEW_Complete
× Gate_Accepted
× Seal_Evidence_Complete
× Downstream_Safe
× Risk_Bounded
```

If any required factor is zero, the AEP is not Industrial Done.

## 6. Anti-patterns

### 6.1 "It ran once, so it is done"

Running once is not industrial completion.

### 6.2 "The model said it passed"

AI self-report is not enough. Evidence must be attached.

### 6.3 "No error appeared"

No visible error does not mean quality is acceptable.

### 6.4 "The next task can fix it"

AEP closure should not push hidden debt downstream.

### 6.5 "We will document later"

Undocumented engineering work decays into unverifiable memory.

## 7. Industrial Done output

A completed AEP should leave behind:

```text
1. Working artifact
2. PoEW record
3. Gate result
4. Seal report
5. Evidence bundle
6. Risk note
7. Downstream note
8. Reopen criteria
```

## 8. Final rule

> No AEP may become a dependency of a production NEM unless it has reached `Industrial Done` or has been explicitly accepted as `PASS_WITH_LIMITATIONS`.
