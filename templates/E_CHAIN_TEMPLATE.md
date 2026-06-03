# E-Chain Template

## Directory structure

```
chains/
├── {CHAIN_ID}.yaml
└── chain_log.yaml
```

---

## {CHAIN_ID}.yaml

```yaml
chain_id: "{CHAIN_ID}"
chain_type: main  # main | feature | experiment | fix
project: "{PROJECT_NAME}"
description: "{DESCRIPTION}"

parent_chain: null  # For branch tracks, the parent chain_id
branch_point: null   # NEM ID and version where this chain branches
merge_target: null   # Target NEM on parent chain for merge

nems:
  # Ordered list of NEMs on this chain
  - nem_id: "{NEM_ID}"
    version: "0.1.0"
    order: 1
    gates_passed: []

created: "{ISO_TIMESTAMP}"
updated: "{ISO_TIMESTAMP}"
```

---

## chain_log.yaml

```yaml
events:
  - timestamp: "{ISO_TIMESTAMP}"
    type: "chain_created"
    description: "Chain initialized"
```
