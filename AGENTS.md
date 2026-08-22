# Agent guidance

## Repository overview

This repository is a Home Assistant configuration for HAOS running in a Proxmox
VM. The Home Assistant version is pinned in `.HA_VERSION`.

`configuration.yaml` loads packages from `integrations/`. Those files are thin
integration declarations which include entity definitions from `entities/`.
ESPHome configuration lives in the separate `esphome/` submodule.

The main authored paths are:

- `entities/automation/` — automations grouped by triggering entity domain
- `entities/script/` — reusable scripts
- `entities/template/` and `entities/template_triggered/` — template entities
- `entities/input_*/` and `entities/var/` — helpers and state
- `integrations/` — thin package/include declarations
- `dev_tools/` — maintained Python utilities

Zigbee2MQTT runs separately in a Proxmox LXC and exposes devices through MQTT.
The GitHub Actions runner publishes retained concurrency telemetry to MQTT; the
raw sensor and its derived template entities feed the Proxmox VE dashboard.
Home Assistant has branch-selection and per-domain auto-reload helpers for the
user-owned git deployment workflow.

## Live Home Assistant context

Proactively inspect live Home Assistant through MCP before:

- creating or editing automations;
- troubleshooting entities, integrations, or state changes;
- answering questions about what is currently happening;
- relying on entity IDs, availability, areas, device capabilities, or values.

Use the available Home Assistant tools directly or through Backplane—for
example overview, search, entity, state, history, service-list, template-eval,
and automation-trace tools. Do not wait for the user to request live context
when correctness depends on it, and never guess live behavior.

## Git safety

Do not mutate git state or the working tree unless the user explicitly requests
the operation. Read-only commands such as `git status`, `git diff`, `git log`,
`git show`, and `git rev-parse` are always allowed. Creating a worktree and its
branch is allowed when the user asks for a worktree. Create branches from a
remote base with `--no-track` so they do not inherit the base branch as their
upstream. When the user asks to publish the branch or configure its upstream,
push it under its own name with `git push -u origin HEAD`.

Without explicit user authorization, do not run `git add`, `commit`, `push`,
`pull`, `fetch`, `checkout`, `switch`, `restore`, `reset`, `merge`, `rebase`,
`stash`, `tag`, `clean`, or equivalents. Ask the user to perform required git
operations; do not work around this with GitHub APIs, MCP, or shell redirects.

## Deployment

The only deployment method for repository files is user-owned git:

1. Make and validate local changes.
2. Ask the user to commit and push them.
3. The user checks out the branch on Home Assistant.
4. Wait for the user to confirm the checkout.
5. Reload affected integrations through MCP where supported, then verify the
   changed entities and behavior against live state.

Never transfer or directly edit repository files on Home Assistant using SSH,
rsync, SFTP, scp, a file-sync watcher, an API, MCP, or any other bypass. These
methods dirty the remote working tree and cause git conflicts. Never assume
local changes are live before the user confirms the checkout. In particular,
never run obsolete workflows such as `make sync-files` or `hasspi_file_sync`.

Storage-mode dashboard updates through MCP are not repository-file deployments
and remain the only exception. YAML dashboard or entity changes still require
the git workflow above.

## Dashboard changes

Everything under `lovelace/dashboards/ui_only/` is a read-only export of a
storage-mode dashboard. Treat these files as if they do not exist:

- Never edit, format, lint, review, or use them as evidence of live dashboard
  configuration.
- Treat diffs touching only these exports as no-ops during review. If an export
  is edited accidentally, revert it rather than treating it as a dashboard
  change.
- A request to create or update a dashboard means changing the live dashboard
  with Home Assistant MCP dashboard tools, whether exposed directly by the Home
  Assistant MCP server or through Backplane.
- Use `ha_config_get_dashboard` to inspect or search a dashboard, then
  `ha_config_set_dashboard` with a `python_transform` and the returned
  `config_hash`.
- Never add `grid_options` to `custom:mini-graph-card` unless the user
  explicitly requests it. This applies to live dashboards and authored config
  such as `lovelace/decluttering_templates.yaml`.

Typical workflow:

```text
ha_config_get_dashboard(url_path="home-will", entity_id="sensor.example")
→ use python_path and config_hash from the result
→ ha_config_set_dashboard(
    url_path="home-will",
    config_hash=...,
    python_transform=...,
  )
```

## File structure and naming

Automations live under `entities/automation/<trigger-domain>/`. Their file path,
alias, and ID must correspond:

```yaml
# entities/automation/binary_sensor/kitchen_presence/on.yaml
alias: /binary-sensor/kitchen-presence/on
id: binary_sensor_kitchen_presence_on
mode: single
```

Use separate `on.yaml` and `off.yaml` automations for opposite sides of a state
transition. Other entity names and unique IDs should match their snake-case
filenames. Script aliases must match their filenames. Every automation requires
an explicit mode such as `mode: single`.

Kitchen presence automations use
`binary_sensor.kitchen_presence_sensor`; do not infer a shorter entity ID.

## Automation conventions

- Before changing automations or answering questions about current states,
  entity availability, areas, or device capabilities, inspect live Home
  Assistant context through the Home Assistant MCP tools (directly or through
  Backplane). Do not guess entity IDs or live behavior.
- Use direct entity references in triggers. Do not wrap trigger entity
  references in `states()`.
- Prefer `if`/`then` actions over global conditions when later actions may be
  added. Use a global condition only when the entire automation must be gated.
  Use `choose` for multi-branch behavior; every branch requires `conditions`
  and `sequence`, while `default` does not.
- In `parallel`, wrap related sequential actions in a `sequence`.
- Use `sensor.lighting_modifier` for brightness rather than hard-coded values:
  `{{ states('sensor.lighting_modifier') | int(70) }}`. Use `int(80)` for LED
  matrix brightness where appropriate.
- Use area or floor targets where they express the intended scope.
- `floor_id` is a valid target for floor-wide actions.
- Use standard `vacuum.pause` and `vacuum.start` services for `vacuum.cosmo`
  presence pause/resume behavior unless a custom service is required.
- Add `continue_on_error: true` to non-critical actions.
- Use `max_exceeded: silent` for intentionally high-frequency single-mode
  automations.
- Use `script.debug_persistent_notification` for temporary automation
  diagnostics and remove development logging when verification is complete.

### Trigger references

Entity-backed trigger fields accept direct entity IDs:

```yaml
# Correct
- platform: time
  at: input_datetime.next_bedroom_sunrise
- platform: numeric_state
  entity_id: sensor.temperature
  above: input_number.max_temp
  below: input_number.min_temp
- platform: state
  entity_id: binary_sensor.motion
  to: "on"

# Wrong
- platform: time
  at: "{{ states('input_datetime.next_bedroom_sunrise') }}"
- platform: numeric_state
  entity_id: sensor.temperature
  above: "{{ states('input_number.max_temp') }}"
```

This applies to time, numeric-state, state, zone, and similar triggers. Use a
template trigger only for genuinely complex expressions.

### Parallel actions

Every item in `parallel` must be one independent action, a `sequence`, or an
`if`/`then` block:

```yaml
# Wrong: the delay and light action also start immediately
- parallel:
    - action: vacuum.start
      target:
        entity_id: vacuum.cosmo
    - delay:
        seconds: 5
    - action: light.turn_off
      target:
        floor_id: basement

# Correct: delay and light action remain sequential
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
```

See `entities/automation/binary_sensor/basement_presence/off.yaml` for the
canonical pattern.

For lounge media activity, check all unreliable sources together:

```jinja2
{{
  is_state('remote.lounge_tv', 'on') or
  is_state('remote.lounge_chromecast', 'on') or
  is_state('media_player.lounge_chromecast', 'on') or
  is_state('media_player.lounge_tv_2', 'on') or
  is_state('media_player.lounge_chromecast_remote', 'on')
}}
```

## Lighting modifier

`sensor.lighting_modifier`, defined in
`entities/template/sensor/lighting_modifier.yaml`, produces context-aware
brightness from time of day, quiet hours, weekday status, and sun elevation.
Use it for every automated brightness value:

```yaml
brightness_pct: "{{ states('sensor.lighting_modifier') | int(70) }}"
```

Use `int(70)` as the normal fallback and `int(80)` for LED matrices. To scale
the result, calculate from the modifier rather than hard-coding brightness:

```yaml
brightness_pct: >-
  {{ (states('sensor.lighting_modifier') | int(70) * 0.5) | int }}
```

## Notifications

Use `script.notify_will` or `script.notify_vic`, never `notify.*` services
directly. Notification actions are non-critical and must use
`continue_on_error: true`. Supply a `notification_id` and an `mdi:` icon. Use
`sticky: true` for alerts that should remain visible and `persistent: true` for
critical alerts that must survive “Clear All”.

```yaml
- action: script.notify_will
  continue_on_error: true
  data:
    title: Something Happened
    message: Details here
    notification_id: something_happened
    mobile_notification_icon: mdi:alert
    sticky: true
```

For template debugging, use `| tojson` in Developer Tools to inspect complex
values.

## Validation

CI runs:

- prek hooks for formatting, linting, entity validation, actionlint, and
  basedpyright;
- Home Assistant configuration checks against stable, beta, dev, and the
  version pinned in `.HA_VERSION`.

Stable and pinned-version failures are blocking. Beta and dev results are
informational. Run `just ci` before handing off substantial changes.

Pull request titles and commits use Conventional Commits. Squash-merged PR
titles drive Python Semantic Release: `feat` creates a minor release;
`build`, `deps`, `fix`, `hotfix`, and `perf` create patch releases; `!` or a
`BREAKING CHANGE` footer creates a major release. Other allowed types do not
release.

Do not add new dependencies without updating `pyproject.toml` and `uv.lock`.
Do not hand-edit generated `integrations/README.md`; regenerate it through the
entity-validation hook.
