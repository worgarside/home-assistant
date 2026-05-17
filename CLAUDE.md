# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Home Assistant configuration repository for HAOS running in a Proxmox VM. The HA version is tracked in `.HA_VERSION`. Configuration is structured using HA's [packages](https://www.home-assistant.io/docs/configuration/packages/) pattern: `configuration.yaml` loads everything via `!include_dir_named integrations`, and each file in `integrations/` declares one or more HA domains and points to entity files.

`esphome/` is a git submodule pointing to a separate ESPHome config repository.

## Development Commands

```bash
# Run all pre-commit hooks (lint, format, validate)
pre-commit run --all-files

# Sync local files to the live HA instance over SSH
make sync-files                          # alias for: uv run python dev_tools/hasspi_file_sync/main.py

# Run HA config validation locally via act
make vscode-shortcut-1                   # runs validate_ha_config.yml with GitHub Actions locally
```

CI runs pre-commit on every PR. The same hooks run locally:
- **yamlfmt** – auto-formats YAML (2-space mapping, 4-space sequence, 2-space offset, 4096-char width)
- **yamllint** – strict lint, max line length 101
- **validate-entities** – custom HA validator (`home-assistant-config-validator`) with `--fix` flag
- **generate-readme** – regenerates `integrations/README.md` from entity metadata
- **ruff** / **mypy** – for Python files in `dev_tools/`

## Architecture

### Package / Include pattern

```
configuration.yaml
  └─ packages: !include_dir_named integrations/
       ├─ automation.yaml   →  automation: !include_dir_list ../entities/automation
       ├─ script.yaml       →  script: !include_dir_named ../entities/script
       ├─ mqtt.yaml         →  sensor: !include_dir_named ../entities/mqtt/sensor
       └─ ...               →  (one integration per file)
```

All entity YAML files live under `entities/<domain>/`. The `integrations/` files are thin glue that just `!include_dir_*` from `entities/`.

### Entity directories

| Directory | Domain | Pattern |
|---|---|---|
| `entities/automation/` | `automation` | One file per automation, organised by the triggering entity domain |
| `entities/script/` | `script` | One file per script |
| `entities/template/` | `template` | Grouped by output type (`sensor/`, `binary_sensor/`, etc.) |
| `entities/var/` | `var` | Variable entities for complex state tracking |
| `entities/input_*/` | `input_boolean`, `input_number`, etc. | One file per helper entity |

## Naming Conventions (enforced by `config_validator.yml`)

### Automations

The `alias`, `id`, and file path must all correspond:

| Field | Case | Example |
|---|---|---|
| File path | snake_case dirs | `entities/automation/binary_sensor/basement_presence/off.yaml` |
| `alias` | kebab-case with `/` prefix | `alias: /binary-sensor/basement-presence/off` |
| `id` | snake_case | `id: binary_sensor_basement_presence_off` |
| `mode` | required | `mode: single` |

The `on`/`off` sides of a presence trigger go in separate files (`on.yaml` / `off.yaml`).

### Other entity types

- `input_*`, `sensor`, `binary_sensor`, `var`: entity `name` (and `unique_id` where applicable) must match the filename (snake_case).
- `script`: `alias` must match the filename.

## Key Automation Patterns

### Trigger syntax — always use direct entity references

```yaml
# ✅ Correct
- platform: time
  at: input_datetime.next_bedroom_sunrise
- platform: numeric_state
  entity_id: sensor.temperature
  above: input_number.max_temp

# ❌ Wrong — never wrap entity refs in states() inside triggers
- platform: time
  at: "{{ states('input_datetime.next_bedroom_sunrise') }}"
```

### Lighting — always use `sensor.lighting_modifier`

`sensor.lighting_modifier` (defined in `entities/template/sensor/lighting_modifier.yaml`) computes time- and sun-aware brightness (1–100%). **Never hard-code brightness values.**

```yaml
# ✅
brightness_pct: "{{ states('sensor.lighting_modifier') | int(70) }}"
# ❌
brightness_pct: 70
```

Common fallbacks: `| int(70)` for most lights, `| int(80)` for LED matrix.

### Conditional logic — prefer `if`/`then` over global `condition` blocks

```yaml
action:
  - if: "{{ is_state('vacuum.cosmo', 'cleaning') }}"
    then:
      - action: vacuum.pause
        target:
          entity_id: vacuum.cosmo
```

Use `choose` for multi-branch logic; use global `condition` blocks only when the whole automation must be gated.

### Parallel blocks — wrap sequential items in `sequence`

```yaml
# ✅ Correct — delay and subsequent action stay sequential within the parallel block
- parallel:
    - action: vacuum.start
      target:
        entity_id: vacuum.cosmo
    - sequence:
        - delay:
            seconds: 5
        - action: light.turn_off
          target:
            floor_id: basement

# ❌ Wrong — delay and light.turn_off would execute in parallel
- parallel:
    - action: vacuum.start
    - delay:
        seconds: 5
    - action: light.turn_off
```

### Lounge media detection — check multiple entities

Individual lounge media entities are unreliable; always check all of them:

```yaml
- if: >
    {{
      is_state('remote.lounge_tv', 'on') or
      is_state('remote.lounge_chromecast', 'on') or
      is_state('media_player.lounge_chromecast', 'on') or
      is_state('media_player.lounge_tv_2', 'on') or
      is_state('media_player.lounge_chromecast_remote', 'on')
    }}
```

### Error handling

```yaml
mode: single
max_exceeded: silent          # suppress logs for high-frequency triggers

- action: unreliable_service
  continue_on_error: true     # allow the sequence to continue on failure
```

## Dashboard Rules

- **Never** add `grid_options` (`columns`, `rows`) to a `custom:mini-graph-card` — it breaks layout.

## Debugging

- Use `script.debug_persistent_notification` to log values during development.
- Template errors: use `| tojson` to inspect complex values in Developer Tools.

## CI — HA Config Validation

The `validate_home_assistant_config.yml` workflow runs the HA config checker against four versions: `stable`, `beta`, `dev`, and the version pinned in `.HA_VERSION`. Errors in `stable` or the pinned version are treated as failures; errors in `beta`/`dev` are informational only.

Custom components required for validation (`var`, `spotcast`, `plex_recently_added`) are cloned fresh in CI; `custom_components/` is gitignored locally.
