"""Color-generating utilities."""

from __future__ import annotations

from colorsys import hls_to_rgb


def hls_to_hex(hue: float, lightness: float, saturation: float, /) -> str:
    """Convert HLS to HEX."""
    r, g, b = hls_to_rgb(hue / 360.0, lightness, saturation)

    return f"{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


def generate_unique_colors(n: int) -> list[str]:
    """Generate n unique colors."""
    if n < 1:
        raise ValueError(n)

    step = 360.0 / n if n > 1 else 0
    colors = []

    for i in range(n):
        hue = i * step
        hex_color = hls_to_hex(hue, 0.5, 0.8)
        colors.append(hex_color)

    return colors


def get_addon_colors() -> None:
    """Generate colors for the Add-ons."""
    addon_names = (
        ("AdGuard", "adguard"),
        ("AppDaemon", "appdaemon"),
        ("ESPHome", "esphome_add_on"),
        ("Grafana", "grafana"),
        ("InfluxDB", "influxdb"),
        ("Google Drive Backup", "google_drive_backup_add_on"),
        ("Item Warehouse API", "item_warehouse_api"),
        ("Item Warehouse Website", "item_warehouse_website"),
        ("MariaDB", "mariadb"),
        ("Matter Server", "matter_server"),
        ("Mosquitto Broker", "mosquitto_broker"),
        # ("Plex Media Server", "plex_media_server"),  # noqa: ERA001
        ("Silicon Labs Multiprotocol", "silicon_labs_multiprotocol_add_on"),
        ("Terminal & SSH", "terminal_ssh_add_on"),
        ("VSCode", "visual_studio_code_add_on"),
        ("YAS-209 Bridge", "yas_209_bridge"),
    )

    template = """  - type: custom:decluttering-card
    template: addon_active_entity_template
    variables:
      - color: '#{color}'
      - name: {name}
      - slug: {slug}"""

    print("""square: false
type: grid
columns: 3
cards:""")

    color_tuples = tuple(
        (c.upper(), addon, slug)
        for c, (addon, slug) in zip(generate_unique_colors(len(addon_names)), addon_names)
    )

    for color, addon, slug in color_tuples:
        print(template.format(color=color, name=addon, slug=slug))

    print("\n\n\n\n\n\n")
    print("""type: custom:mini-graph-card
name: 6 Hour History
entities:""")
    for color, _, slug in color_tuples:
        print(f"""  - entity: sensor.{slug}_cpu_usage
    color: '#{color}'""")

    print("""show:
  state: false
  legend: false
  fill: fade
  name: true
  icon: false
  labels: true
  labels_secondary: true
  unit: true
hours_to_show: 6
points_per_hour: 60
lower_bound: 0
upper_bound: ~70
height: 150
animate: true
hour24: true
line_width: 2
""")


def get_repo_label_colors() -> None:
    """Generate colors for the repository labels."""
    repo_labels = (
        ("ha:appdaemon", "AppDaemon apps for Home Assistant"),
        ("ha:automations", "Automations to control devices"),
        ("ha:config", "Configuration files for Home Assistant"),
        ("ha:command-line", "Command line sensors"),
        ("ha:cover", "Window blinds, curtains, and garage doors"),
        ("ha:custom-components", "Custom Components added to Home Assistant"),
        ("ha:device-tracker", "Track device locations and presence"),
        ("ha:groups", "Group entities together for easy control"),
        ("ha:input-boolean", "Binary on/off input controls"),
        ("ha:input-button", "Momentary push button input controls"),
        ("ha:input-datetime", "Date and time input controls"),
        ("ha:input-number", "Numeric input controls"),
        ("ha:input-select", "Dropdown selection input controls"),
        ("ha:input-text", "Text input controls"),
        ("ha:lovelace", "Lovelace UI configuration files"),
        ("ha:media-player", "Music and video playback devices"),
        ("ha:mqtt", "MQTT broker and clients"),
        ("ha:pyscript", "Custom Python scripts for Home Assistant"),
        ("ha:rest-command", "RESTful API commands"),
        ("ha:scenes", "Preconfigured sets of entity states"),
        ("ha:scripts", "Reusable blocks of automation code"),
        ("ha:sensors", "Gather data about the environment"),
        ("ha:shell-command", "Shell commands to run on the host system"),
        ("ha:switch", "On/off switches for devices"),
        ("ha:template", "Template entities for customization"),
        ("ha:variables", "Global variables for use in automations"),
    )

    for i, c in enumerate(generate_unique_colors(len(repo_labels))):
        label, description = repo_labels[i]

        print(
            f"""\n  - name: {label}
    color: "{c.upper()}"
    description: {description}
        """.rstrip(),
        )


if __name__ == "__main__":
    print("\n\n\n")
    get_addon_colors()
