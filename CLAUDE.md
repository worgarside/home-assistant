# Home Assistant Config — Claude Guidelines

## Automation & Script Conventions

### File layout
- Automations live in `entities/automation/{entity_type}/{optional_device}/filename.yaml`
- Notification automations go in `entities/automation/notification/`
- One automation per file; file name matches the automation's purpose in `snake_case`

### Naming
| Field | Convention | Example |
|-------|-----------|---------|
| `id` | `snake_case` path | `notification_external_ip_unavailable` |
| `alias` | `/path/to/automation` | `/notification/external-ip-unavailable` |
| `notification_id` | `short_snake_case` | `external_ip_unavailable` |

### Notifications
- Use `script.notify_will` and/or `script.notify_vic` — never call `notify.*` services directly
- Always set `continue_on_error: true` on notification action calls; they are non-critical and a transient failure must not abort the automation
- Use `mdi:` icons via `mobile_notification_icon`
- Set `sticky: true` for alerts that should persist until dismissed
- Set `persistent: true` for critical alerts that survive "Clear All"
- Provide a `notification_id` so notifications can be grouped or cleared

### Example notification action block
```yaml
action:
  - action: script.notify_will
    continue_on_error: true
    data:
      title: "Something Happened"
      message: "Details here"
      notification_id: something_happened
      mobile_notification_icon: mdi:alert
      sticky: true
```
