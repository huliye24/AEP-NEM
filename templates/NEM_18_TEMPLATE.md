# NEM-18 Template

```yaml
nem_id: "{NEM_ID}"
nem_profile: NEM-18
title: "{TITLE}"
version: "0.1.0"
status: DRAFT
node_formula: "NEM-18 = Build-6 + Validate-6 + Harden-6"

phases:
  - id: BUILD-6
    purpose: "Create a runnable capability."
    aeps: []
    gate:
      id: "{BUILD_GATE_ID}"
      status: PENDING

  - id: VALIDATE-6
    purpose: "Validate the capability against real inputs, metrics, and failure cases."
    aeps: []
    gate:
      id: "{VALIDATE_GATE_ID}"
      status: PENDING

  - id: HARDEN-6
    purpose: "Turn validated work into a reusable and maintainable asset."
    aeps: []
    gate:
      id: "{HARDEN_GATE_ID}"
      status: PENDING

seal:
  required: true
  report: null
  decision: PENDING

next_entry:
  candidate_nem: null
  candidate_echain: null
```

