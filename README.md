# Home Assistant

Home Assistant configuration managed as packages: `configuration.yaml` loads
integration declarations from `integrations/`, which include entity definitions
from `entities/`.

## Development

Install the locked toolchain and git hooks:

```bash
just setup
```

Run all local CI checks:

```bash
just ci
```

Run `just` to list focused formatting, validation, type-checking, and utility
commands. Running the Home Assistant workflow locally with `just ha-validate`
or `just ci` also requires [act](https://nektosact.com/).

Hooks are managed and executed with [prek](https://prek.j178.dev/). Python
dependencies and commands use [uv](https://docs.astral.sh/uv/).
Pull request titles use Conventional Commits and drive Python Semantic Release
after squash merging.

## Deployment

Deployment is git-based. After local validation, the user commits and pushes
the changes, then checks out the branch on the Home Assistant instance.
Published semantic-version tags trigger the production instance to pull
`main`.

Storage-mode dashboards are updated through Home Assistant MCP tools. Files in
`lovelace/dashboards/ui_only/` are generated, read-only exports.

The Proxmox VE dashboard's GitHub Actions runner section consumes retained
MQTT telemetry from `/homeassistant/gha-runner/stats`. The raw MQTT entity keeps
the stable `sensor.github_actions_runner_slots` ID, with template entities for
active slots, available slots, waiting jobs, and saturation. During deployment,
reload the command-line integration after checkout so it removes its source
entity, then restart Home Assistant to load the MQTT sensor path. Verify the
registry does not allocate a duplicate `_2` entity ID. A missed heartbeat makes
the raw and derived telemetry unavailable after three minutes.
