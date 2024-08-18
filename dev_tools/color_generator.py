"""Color-generating utilities."""

from __future__ import annotations

import colorsys
from pathlib import Path

import matplotlib.colors as mc
from yaml import safe_load

LABELS = safe_load(
    Path(__file__).parents[1].joinpath(".github/repo_labels.yml").read_text(),
)


def rgba_to_hex(r: int, g: int, b: int, a: float = -1) -> str:
    """Convert an RGBA tuple to a HEX string."""
    if a == -1:
        return f"#{int(r):02x}{int(g):02x}{int(b):02x}".upper()

    return f"#{int(r):02x}{int(g):02x}{int(b):02x}{int(a * 255):02x}".upper()


def hls_to_hex(hue: float, lightness: float, saturation: float, /) -> str:
    """Convert HLS to HEX."""
    r, g, b = colorsys.hls_to_rgb(hue / 360.0, lightness, saturation)

    return f"{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


def lighten_color(color: str, amount: float) -> str:
    """Lighten the given color by multiplying (1-luminosity) by the given amount.

    Examples:
    >> lighten_color('F034A3', 0.6)
    """
    color = "#" + color

    try:
        c = mc.cnames[color]
    except Exception:  # noqa: BLE001
        c = color

    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    r, g, b = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    return f"{r:02x}{g:02x}{b:02x}".upper()


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
        # ("Plex Media Server", "plex_media_server"),
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


def gen_github_label_colors() -> None:
    """Generate color mappings for use in a decluttering template, for GitHub label colors."""
    lightness_threshold = 0.6
    background_alpha = 0.18
    # border_alpha = 0.298

    colors = {lbl["name"]: lbl["color"] for lbl in LABELS}
    output = {}
    for label_name, orig in colors.items():
        label_r, label_g, label_b = (int(i * 255) for i in mc.to_rgb("#" + orig))
        label_h, label_l, label_s = colorsys.rgb_to_hls(
            r=(label_r / 255),
            g=(label_g / 255),
            b=(label_b / 255),
        )

        label_h = int(label_h * 360)
        label_s = int(label_s * 100)
        label_l = int(label_l * 100)

        perceived_lightness = (
            (label_r * 0.2126) + (label_g * 0.7152) + (label_b * 0.0722)
        ) / 255
        lightness_switch = max(
            0,
            min((1 / (lightness_threshold - perceived_lightness)), 1),
        )
        lighten_by = (
            (lightness_threshold - perceived_lightness) * 100
        ) * lightness_switch

        # color_hsl = (
        #     label_h,
        #     (label_s * 0.01),
        #     ((label_l + lighten_by) * 0.01),
        # )

        color_rgb = tuple(
            int(i * 255)
            for i in colorsys.hls_to_rgb(
                h=(label_h / 360),
                l=((label_l + lighten_by) * 0.01),
                s=(label_s * 0.01),
            )
        )
        background_rgba = (label_r, label_g, label_b, background_alpha)
        # border_rgba = (
        #     *tuple(
        #         int(i * 255)
        #         for i in colorsys.hls_to_rgb(
        #             h=(label_h / 360),
        #             l=((label_l + lighten_by) * 0.01),
        #             s=(label_s * 0.01),
        #         )
        #     ),
        #     border_alpha,
        # )

        # output[label_name] = {
        #     "lighten-by": lighten_by,
        #     # "font": f"rgb{str(color_rgb)}",
        #     "font": f"hsl{color_hsl!s}",
        #     "background": f"rgba{background_rgba!s}",
        #     "border": f"rgba{border_rgba!s}",
        # }

        output[label_name] = {
            "font": rgba_to_hex(*color_rgb),
            "background": rgba_to_hex(*background_rgba),
            # "border": rgba_to_hex(*border_rgba)
        }

    output_str = "                const labelColors = {\n"

    for label_name, colors in output.items():
        output_str += f"                  '{label_name}': {colors},\n"

    output_str += "                };\n"

    print(output_str)


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
        ("ha:esphome", "ESPHome configuration files"),
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
    gen_github_label_colors()
