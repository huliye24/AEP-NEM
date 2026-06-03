# PoEW Template

## PoEW Record

```yaml
poew_id: "POEW-{TIMESTAMP}-{AEP_ID}"
timestamp: "{ISO_TIMESTAMP}"
duration: "{DURATION}"

aep:
  aep_id: "{AEP_ID}"
  version: "0.1.0"

executor:
  type: "ai_agent"  # ai_agent | human | automated_system
  model: "{MODEL}"
  provider: "{PROVIDER}"

environment:
  os: "{OS}"
  runtime: "{RUNTIME}"

execution:
  tasks_total: 0
  tasks_completed: 0
  tasks_failed: 0

outputs:
  - path: "{OUTPUT_PATH}"
    hash: "{SHA256_HASH}"

gate_results:
  - gate_id: "{GATE_ID}"
    result: PENDING

reproducibility:
  input_hash: "{INPUT_HASH}"
  output_hash: "{OUTPUT_HASH}"

signature: "auto-poew-v0.1.0"
```

---

## Usage

1. Create a new PoEW record for every AEP execution
2. Fill in all fields after execution completes
3. Compute hashes of all outputs
4. Attach gate results
5. Store in the NEM's `poew/` directory

The PoEW record is append-only. Do not modify after creation.
