# Packages

## Automation

<details><summary><h3>Entities (199)</h3></summary>

<details><summary><code>/automation/auto-reload-complete</code></summary>

**Entity ID: `automation.automation_auto_reload_complete`**

> *No description provided*

- Alias: /automation/auto-reload-complete
- ID: `automation_auto_reload_complete`
- Mode: `single`

File: [`automation/automation/auto_reload_complete.yaml`](entities/automation/automation/auto_reload_complete.yaml)
</details>

<details><summary><code>/binary-sensor/basement-presence/off</code></summary>

**Entity ID: `automation.binary_sensor_basement_presence_off`**

> Resumes Cosmo (vacuum.cosmo) when kitchen presence is cleared for 1 minute and Cosmo is paused, but only if he was cleaning the basement.

- Alias: /binary-sensor/basement-presence/off
- ID: `binary_sensor_basement_presence_off`
- Mode: `single`

File: [`automation/binary_sensor/basement_presence/off.yaml`](entities/automation/binary_sensor/basement_presence/off.yaml)
</details>

<details><summary><code>/binary-sensor/basement-presence/on</code></summary>

**Entity ID: `automation.binary_sensor_basement_presence_on`**

> Pauses Cosmo when someone enters the basement while he's cleaning.

- Alias: /binary-sensor/basement-presence/on
- ID: `binary_sensor_basement_presence_on`
- Mode: `restart`

File: [`automation/binary_sensor/basement_presence/on.yaml`](entities/automation/binary_sensor/basement_presence/on.yaml)
</details>

<details><summary><code>/binary-sensor/dining-area-occupancy/state-change</code></summary>

**Entity ID: `automation.binary_sensor_dining_area_occupancy_state_change`**

> *No description provided*

- Alias: /binary-sensor/dining-area-occupancy/state-change
- ID: `binary_sensor_dining_area_occupancy_state_change`
- Mode: `queued`

File: [`automation/binary_sensor/dining_area_occupancy/state_change.yaml`](entities/automation/binary_sensor/dining_area_occupancy/state_change.yaml)
</details>

<details><summary><code>/binary-sensor/front-door/open</code></summary>

**Entity ID: `automation.binary_sensor_front_door_open`**

> *No description provided*

- Alias: /binary-sensor/front-door/open
- ID: `binary_sensor_front_door_open`
- Mode: `single`

File: [`automation/binary_sensor/front_door/open.yaml`](entities/automation/binary_sensor/front_door/open.yaml)
</details>

<details><summary><code>/binary-sensor/kitchen-hallway-occupancy/on</code></summary>

**Entity ID: `automation.binary_sensor_kitchen_hallway_occupancy_on`**

> *No description provided*

- Alias: /binary-sensor/kitchen-hallway-occupancy/on
- ID: `binary_sensor_kitchen_hallway_occupancy_on`
- Mode: `single`

File: [`automation/binary_sensor/kitchen_hallway_occupancy/on.yaml`](entities/automation/binary_sensor/kitchen_hallway_occupancy/on.yaml)
</details>

<details><summary><code>/binary-sensor/kitchen-occupancy/state-change</code></summary>

**Entity ID: `automation.binary_sensor_kitchen_occupancy_state_change`**

> *No description provided*

- Alias: /binary-sensor/kitchen-occupancy/state-change
- ID: `binary_sensor_kitchen_occupancy_state_change`
- Mode: `queued`

File: [`automation/binary_sensor/kitchen_occupancy/state_change.yaml`](entities/automation/binary_sensor/kitchen_occupancy/state_change.yaml)
</details>

<details><summary><code>/binary-sensor/lounge-diffuser-needs-water/state-change</code></summary>

**Entity ID: `automation.binary_sensor_lounge_diffuser_needs_water_state_change`**

> Send a notification when the lounge diffuser runs out of water

- Alias: /binary-sensor/lounge-diffuser-needs-water/state-change
- ID: `binary_sensor_lounge_diffuser_needs_water_state_change`
- Mode: `single`

File: [`automation/binary_sensor/lounge_diffuser_needs_water/state_change.yaml`](entities/automation/binary_sensor/lounge_diffuser_needs_water/state_change.yaml)
</details>

<details><summary><code>/binary-sensor/lounge-occupancy/off</code></summary>

**Entity ID: `automation.binary_sensor_lounge_occupancy_off`**

> Turn off lounge lighting when room becomes empty

- Alias: /binary-sensor/lounge-occupancy/off
- ID: `binary_sensor_lounge_occupancy_off`
- Mode: `single`

File: [`automation/binary_sensor/lounge_occupancy/off.yaml`](entities/automation/binary_sensor/lounge_occupancy/off.yaml)
</details>

<details><summary><code>/binary-sensor/lounge-occupancy/on</code></summary>

**Entity ID: `automation.binary_sensor_lounge_occupancy_on`**

> Turn on lounge lighting when someone enters the room

- Alias: /binary-sensor/lounge-occupancy/on
- ID: `binary_sensor_lounge_occupancy_on`
- Mode: `single`

File: [`automation/binary_sensor/lounge_occupancy/on.yaml`](entities/automation/binary_sensor/lounge_occupancy/on.yaml)
</details>

<details><summary><code>/binary-sensor/lounge-occupancy/room-timeout</code></summary>

**Entity ID: `automation.binary_sensor_lounge_occupancy_room_timeout`**

> Turn off lounge room after N minutes of being empty

- Alias: /binary-sensor/lounge-occupancy/room-timeout
- ID: `binary_sensor_lounge_occupancy_room_timeout`
- Mode: `single`

File: [`automation/binary_sensor/lounge_occupancy/room_timeout.yaml`](entities/automation/binary_sensor/lounge_occupancy/room_timeout.yaml)
</details>

<details><summary><code>/binary-sensor/lower-hallway-occupancy/on</code></summary>

**Entity ID: `automation.binary_sensor_lower_hallway_occupancy_on`**

> *No description provided*

- Alias: /binary-sensor/lower-hallway-occupancy/on
- ID: `binary_sensor_lower_hallway_occupancy_on`
- Mode: `single`

File: [`automation/binary_sensor/lower_hallway_occupancy/on.yaml`](entities/automation/binary_sensor/lower_hallway_occupancy/on.yaml)
</details>

<details><summary><code>/binary-sensor/main-hallway-motion-sensor-occupancy/on</code></summary>

**Entity ID: `automation.binary_sensor_main_hallway_motion_sensor_occupancy_on`**

> *No description provided*

- Alias: /binary-sensor/main-hallway-motion-sensor-occupancy/on
- ID: `binary_sensor_main_hallway_motion_sensor_occupancy_on`
- Mode: `single`

File: [`automation/binary_sensor/main_hallway_motion_sensor_occupancy/on.yaml`](entities/automation/binary_sensor/main_hallway_motion_sensor_occupancy/on.yaml)
</details>

<details><summary><code>/binary-sensor/quiet-hours/off</code></summary>

**Entity ID: `automation.binary_sensor_quiet_hours_off`**

> *No description provided*

- Alias: /binary-sensor/quiet-hours/off
- ID: `binary_sensor_quiet_hours_off`
- Mode: `single`

File: [`automation/binary_sensor/quiet_hours/off.yaml`](entities/automation/binary_sensor/quiet_hours/off.yaml)
</details>

<details><summary><code>/binary-sensor/quiet-hours/on</code></summary>

**Entity ID: `automation.binary_sensor_quiet_hours_on`**

> *No description provided*

- Alias: /binary-sensor/quiet-hours/on
- ID: `binary_sensor_quiet_hours_on`
- Mode: `single`

File: [`automation/binary_sensor/quiet_hours/on.yaml`](entities/automation/binary_sensor/quiet_hours/on.yaml)
</details>

<details><summary><code>/binary-sensor/roof-shutters-e1-box-leak-sensor/on</code></summary>

**Entity ID: `automation.binary_sensor_roof_shutters_e1_box_leak_sensor_on`**

> Alert Will when water leak is detected in the E1 box

- Alias: /binary-sensor/roof-shutters-e1-box-leak-sensor/on
- ID: `binary_sensor_roof_shutters_e1_box_leak_sensor_on`
- Mode: `single`

File: [`automation/binary_sensor/roof_shutters_e1_box_leak_sensor/on.yaml`](entities/automation/binary_sensor/roof_shutters_e1_box_leak_sensor/on.yaml)
</details>

<details><summary><code>/binary-sensor/vic-s-office/occupancy/state-change</code></summary>

**Entity ID: `automation.binary_sensor_vic_s_office_occupancy_state_change`**

> *No description provided*

- Alias: /binary-sensor/vic-s-office/occupancy/state-change
- ID: `binary_sensor_vic_s_office_occupancy_state_change`
- Mode: `restart`
- Variables:

```json
{
  "state_manager": "var.vic_s_office_state_manager",
  "cached_states": "{{\n  (state_attr(state_manager, \"entity_states_b64\") or \"e30=\")\n  | base64_decode\n  | from_json\n}}",
  "target_area_id": "{{ area_id(state_manager) }}"
}
```
File: [`automation/binary_sensor/vic_s_office/occupancy/state_change.yaml`](entities/automation/binary_sensor/vic_s_office/occupancy/state_change.yaml)
</details>

<details><summary><code>/binary-sensor/will-s-office/external-opening-detected/on</code></summary>

**Entity ID: `automation.binary_sensor_will_s_office_external_opening_detected_on`**

> Turn off office heating when window or roof terrace door is opened

- Alias: /binary-sensor/will-s-office/external-opening-detected/on
- ID: `binary_sensor_will_s_office_external_opening_detected_on`
- Mode: `restart`
- Variables:

```json
{
  "radiator_was_on": "{{ is_state('climate.will_s_office_radiator', 'heat') }}",
  "fan_was_heating": "{{ is_state('climate.will_s_office_fan', 'heat') }}",
  "heating_is_on": "{{ is_state('switch.central_heating', 'on') }}",
  "notif_id": "office_heating_off"
}
```
File: [`automation/binary_sensor/will_s_office/external_opening_detected/on.yaml`](entities/automation/binary_sensor/will_s_office/external_opening_detected/on.yaml)
</details>

<details><summary><code>/binary-sensor/will-s-office/occupancy/state-change</code></summary>

**Entity ID: `automation.binary_sensor_will_s_office_occupancy_state_change`**

> *No description provided*

- Alias: /binary-sensor/will-s-office/occupancy/state-change
- ID: `binary_sensor_will_s_office_occupancy_state_change`
- Mode: `restart`
- Variables:

```json
{
  "state_manager": "var.will_s_office_state_manager",
  "cached_states": "{{\n  (state_attr(state_manager, \"entity_states_b64\") or \"e30=\")\n  | base64_decode\n  | from_json\n}}",
  "target_area_id": "{{ area_id(state_manager) }}"
}
```
File: [`automation/binary_sensor/will_s_office/occupancy/state_change.yaml`](entities/automation/binary_sensor/will_s_office/occupancy/state_change.yaml)
</details>

<details><summary><code>/camera/offline-notify-will</code></summary>

**Entity ID: `automation.camera_offline_notify_will`**

> Notify Will when either basement or lounge camera goes offline

- Alias: /camera/offline-notify-will
- ID: `camera_offline_notify_will`
- Mode: `queued`
- Variables:

```json
{
  "camera_name": "{% if trigger.entity_id == 'camera.basement' %}\n  Basement\n{% elif trigger.entity_id == 'camera.lounge' %}\n  Lounge\n{% else %}\n  Unknown\n{% endif %}"
}
```
File: [`automation/camera/offline_notify_will.yaml`](entities/automation/camera/offline_notify_will.yaml)
</details>

<details><summary><code>/cosmo/docked-set-basement-map</code></summary>

**Entity ID: `automation.cosmo_docked_set_basement_map`**

> Sets Cosmo's selected map to Basement when docked and/or charging

- Alias: /cosmo/docked-set-basement-map
- ID: `cosmo_docked_set_basement_map`
- Mode: `single`

File: [`automation/cosmo/docked_set_basement_map.yaml`](entities/automation/cosmo/docked_set_basement_map.yaml)
</details>

<details><summary><code>/cosmo/nightly-kitchen-clean</code></summary>

**Entity ID: `automation.cosmo_nightly_kitchen_clean`**

> *No description provided*

- Alias: /cosmo/nightly-kitchen-clean
- ID: `cosmo_nightly_kitchen_clean`
- Mode: `single`

File: [`automation/cosmo/nightly_kitchen_clean.yaml`](entities/automation/cosmo/nightly_kitchen_clean.yaml)
</details>

<details><summary><code>/cover/office-desk/keepalive</code></summary>

**Entity ID: `automation.cover_office_desk_keepalive`**

> *No description provided*

- Alias: /cover/office-desk/keepalive
- ID: `cover_office_desk_keepalive`
- Mode: `single`

File: [`automation/cover/office_desk/keepalive.yaml`](entities/automation/cover/office_desk/keepalive.yaml)
</details>

<details><summary><code>/cover/office-desk/work-mode</code></summary>

**Entity ID: `automation.cover_office_desk_work_mode`**

> *No description provided*

- Alias: /cover/office-desk/work-mode
- ID: `cover_office_desk_work_mode`
- Mode: `single`

File: [`automation/cover/office_desk/work_mode.yaml`](entities/automation/cover/office_desk/work_mode.yaml)
</details>

<details><summary><code>/cover/will-s-office-blinds/auto-close</code></summary>

**Entity ID: `automation.cover_will_s_office_blinds_auto_close`**

> Closes Will's office blinds when the office door is closed, the office desk is occupied, and the sun is below -3 degrees.

- Alias: /cover/will-s-office-blinds/auto-close
- ID: `cover_will_s_office_blinds_auto_close`
- Mode: `single`

File: [`automation/cover/will_s_office_blinds/auto_close.yaml`](entities/automation/cover/will_s_office_blinds/auto_close.yaml)
</details>

<details><summary><code>/cover/will-s-office-blinds/work-camera-active</code></summary>

**Entity ID: `automation.cover_will_s_office_blinds_work_camera_active`**

> Closes Will's office blinds when Will is at home and the work MacBook Pro starts using the configured work camera, and re-opens them when the camera has not been used for 60 seconds (only if the blinds were originally open).

- Alias: /cover/will-s-office-blinds/work-camera-active
- ID: `cover_will_s_office_blinds_work_camera_active`
- Mode: `single`
- Variables:

```json
{
  "blinds_were_open": "{{ is_state('cover.will_s_office_blinds', 'open') }}"
}
```
File: [`automation/cover/will_s_office_blinds/work_camera_active.yaml`](entities/automation/cover/will_s_office_blinds/work_camera_active.yaml)
</details>

<details><summary><code>/crtpi/cpu-fan-control</code></summary>

**Entity ID: `automation.crtpi_cpu_fan_control`**

> *No description provided*

- Alias: /crtpi/cpu-fan-control
- ID: `crtpi_cpu_fan_control`
- Mode: `restart`
- Variables:

```json
{
  "cpu_temp": "{{ states('sensor.crtpi_cpu_temperature') | float(0) }}",
  "threshold": "{{ states('input_number.crtpi_fan_auto_on_threshold') | int(999) }}",
  "should_be_on": "{{ cpu_temp | float(0) > threshold | int(999) }}"
}
```
File: [`automation/crtpi/cpu_fan_control.yaml`](entities/automation/crtpi/cpu_fan_control.yaml)
</details>

<details><summary><code>/crtpi/update-display</code></summary>

**Entity ID: `automation.crtpi_update_display`**

> *No description provided*

- Alias: /crtpi/update-display
- ID: `crtpi_update_display`
- Mode: `queued`
- Variables:

```json
{
  "media_player": "{{ states('input_select.crtpi_media_player_source') }}",
  "artwork_uri": "{% set url = trigger.to_state.attributes.entity_picture | default(None) %} {%\n  set host = (\n    states('sensor.local_ip')\n    if has_value('sensor.local_ip')\n    else \"homeassistant.local\"\n  )\n%} {{\n  \"http://\" ~ host ~ \":8123\" ~ url\n  if url is string and url.startswith(\"/api/\")\n  else url\n}}"
}
```
File: [`automation/crtpi/update_display.yaml`](entities/automation/crtpi/update_display.yaml)
</details>

<details><summary><code>/cube/knock</code></summary>

**Entity ID: `automation.cube_knock`**

> *No description provided*

- Alias: /cube/knock
- ID: `cube_knock`
- Mode: `queued`
- Variables:

```json
{
  "active_face": "{{ states('sensor.cube_active_face') }}",
  "target_entity": "{{ states('input_text.cube_entity_' ~ active_face ) | lower }}",
  "target_domain": "{{ target_entity.split('.')[0] }}"
}
```
File: [`automation/cube/knock.yaml`](entities/automation/cube/knock.yaml)
</details>

<details><summary><code>/cube/rotate</code></summary>

**Entity ID: `automation.cube_rotate`**

> *No description provided*

- Alias: /cube/rotate
- ID: `cube_rotate`
- Mode: `queued`
- Variables:

```json
{
  "active_face": "{{ states('sensor.cube_active_face') }}",
  "target_entity": "{{ states('input_text.cube_entity_' ~ active_face ) | lower }}",
  "target_domain": "{{ target_entity.split('.')[0] }}"
}
```
File: [`automation/cube/rotate.yaml`](entities/automation/cube/rotate.yaml)
</details>

<details><summary><code>/cube/slide</code></summary>

**Entity ID: `automation.cube_slide`**

> *No description provided*

- Alias: /cube/slide
- ID: `cube_slide`
- Mode: `queued`
- Variables:

```json
{
  "active_face": "{{ states('sensor.cube_active_face') }}",
  "target_entity": "{{ states('input_text.cube_entity_' ~ active_face ) | lower }}",
  "target_domain": "{{ target_entity.split('.')[0] }}"
}
```
File: [`automation/cube/slide.yaml`](entities/automation/cube/slide.yaml)
</details>

<details><summary><code>/diffuser/lounge/set-color</code></summary>

**Entity ID: `automation.diffuser_lounge_set_color`**

> Keep the color of the lounge diffuser the same

- Alias: /diffuser/lounge/set-color
- ID: `diffuser_lounge_set_color`
- Mode: `single`

File: [`automation/diffuser/lounge/set_color.yaml`](entities/automation/diffuser/lounge/set_color.yaml)
</details>

<details><summary><code>/diffuser/lounge/timeout</code></summary>

**Entity ID: `automation.diffuser_lounge_timeout`**

> *No description provided*

- Alias: /diffuser/lounge/timeout
- ID: `diffuser_lounge_timeout`
- Mode: `single`

File: [`automation/diffuser/lounge/timeout.yaml`](entities/automation/diffuser/lounge/timeout.yaml)
</details>

<details><summary><code>/event/repair/state-change</code></summary>

**Entity ID: `automation.event_repair_state_change`**

> Log repairs to the Home Assistant GitHub repository

- Alias: /event/repair/state-change
- ID: `event_repair_state_change`
- Mode: `queued`
- Variables:

```json
{
  "domains": [
    "group",
    "lovelace",
    "switch_as_x",
    "automation",
    "binary_sensor",
    "button",
    "calendar",
    "camera",
    "conversation",
    "cover",
    "device_tracker",
    "event",
    "fan",
    "image",
    "input_boolean",
    "input_button",
    "input_datetime",
    "input_number",
    "input_select",
    "input_text",
    "light",
    "media_player",
    "number",
    "person",
    "remote",
    "scene",
    "script",
    "select",
    "sensor",
    "stt",
    "sun",
    "switch",
    "tag",
    "tts",
    "update",
    "vacuum",
    "var",
    "weather",
    "zone"
  ],
  "issue_types": [
    "deprecated_yaml",
    "unknown_source",
    "unknown_members",
    "unknown_area_references",
    "unknown_device_references",
    "unknown_entity_references",
    "unknown_floor_references",
    "unknown_label_references",
    "unknown_service_references"
  ],
  "issue_id": "{{ trigger.to_state.attributes.issue_id }}",
  "event_type": "{{ trigger.to_state.attributes.event_type or 'something-e' }}"
}
```
File: [`automation/event/repair/state_change.yaml`](entities/automation/event/repair/state_change.yaml)
</details>

<details><summary><code>/fan/air-purifier/control</code></summary>

**Entity ID: `automation.fan_air_purifier_control`**

> *No description provided*

- Alias: /fan/air-purifier/control
- ID: `fan_air_purifier_control`
- Mode: `single`
- Variables:

```json
{
  "diffuser_is_on": "{{ states('switch.lounge_diffuser') | bool(false) }}",
  "purifier_is_on": "{{ states('fan.air_purifier') | bool(false) }}"
}
```
File: [`automation/fan/air_purifier/control.yaml`](entities/automation/fan/air_purifier/control.yaml)
</details>

<details><summary><code>/fan/kitchen-extractor-vent/control</code></summary>

**Entity ID: `automation.fan_kitchen_extractor_vent_control`**

> *No description provided*

- Alias: /fan/kitchen-extractor-vent/control
- ID: `fan_kitchen_extractor_vent_control`
- Mode: `single`
- Variables:

```json
{
  "voc_high": "{{\n  states('sensor.kitchen_air_quality_sensor_voc_index') | float >\n  states('input_number.kitchen_extractor_vent_voc_index_threshold') | float\n}}\n",
  "pm25_high": "{{\n  states('sensor.kitchen_air_quality_sensor_pm25') | float >\n  states('input_number.kitchen_extractor_vent_pm2_5_threshold') | float\n}}\n"
}
```
File: [`automation/fan/kitchen_extractor_vent/control.yaml`](entities/automation/fan/kitchen_extractor_vent/control.yaml)
</details>

<details><summary><code>/fan/prusa-i3-enclosure-fan/turn-off</code></summary>

**Entity ID: `automation.fan_prusa_i3_enclosure_fan_turn_off`**

> *No description provided*

- Alias: /fan/prusa-i3-enclosure-fan/turn-off
- ID: `fan_prusa_i3_enclosure_fan_turn_off`
- Mode: `single`

File: [`automation/fan/prusa_i3_enclosure_fan/turn_off.yaml`](entities/automation/fan/prusa_i3_enclosure_fan/turn_off.yaml)
</details>

<details><summary><code>/fan/prusa-i3-enclosure-fan/turn-on</code></summary>

**Entity ID: `automation.fan_prusa_i3_enclosure_fan_turn_on`**

> *No description provided*

- Alias: /fan/prusa-i3-enclosure-fan/turn-on
- ID: `fan_prusa_i3_enclosure_fan_turn_on`
- Mode: `single`

File: [`automation/fan/prusa_i3_enclosure_fan/turn_on.yaml`](entities/automation/fan/prusa_i3_enclosure_fan/turn_on.yaml)
</details>

<details><summary><code>/fan/vic-s-office-fan/control</code></summary>

**Entity ID: `automation.fan_vic_s_office_fan_control`**

> Turn on Vic's office fan when air quality is bad (high PM2.5 or VOC levels). The fan will turn on when either PM2.5 or VOC index exceeds their respective thresholds.

- Alias: /fan/vic-s-office-fan/control
- ID: `fan_vic_s_office_fan_control`
- Mode: `single`
- Variables:

```json
{
  "pm25_high": "{{\n  states('sensor.vic_s_office_fan_pm_2_5') | float(0) >\n  states('input_number.vic_s_office_fan_pm2_5_threshold') | float(0)\n}}\n",
  "voc_high": "{{\n  states('sensor.vic_s_office_fan_volatile_organic_compounds_index') | float(0) >\n  states('input_number.vic_s_office_fan_voc_index_threshold') | float(0)\n}}\n",
  "room_occupied": "{{ is_state('binary_sensor.vic_s_office_occupancy', 'on') }}",
  "occupied_speed": "{{ states('input_number.vic_s_office_fan_purifier_speed') | int(50) }}"
}
```
File: [`automation/fan/vic_s_office_fan/control.yaml`](entities/automation/fan/vic_s_office_fan/control.yaml)
</details>

<details><summary><code>/fan/will-s-office-fan/control</code></summary>

**Entity ID: `automation.fan_will_s_office_fan_control`**

> Turn on Will's office fan when air quality is bad (high PM2.5 or VOC levels). The fan will turn on when either PM2.5 or VOC index exceeds their respective thresholds.

- Alias: /fan/will-s-office-fan/control
- ID: `fan_will_s_office_fan_control`
- Mode: `single`
- Variables:

```json
{
  "pm25_high": "{{\n  states('sensor.will_s_office_fan_pm_2_5') | float(0) >\n  states('input_number.will_s_office_fan_pm2_5_threshold') | float(0)\n}}\n",
  "voc_high": "{{\n  states('sensor.will_s_office_fan_volatile_organic_compounds_index') | float(0) >\n  states('input_number.will_s_office_fan_voc_index_threshold') | float(0)\n}}\n",
  "room_occupied": "{{ is_state('binary_sensor.will_s_office_occupancy', 'on') }}",
  "occupied_speed": "{{ states('input_number.will_s_office_fan_purifier_speed') | int(70) }}"
}
```
File: [`automation/fan/will_s_office_fan/control.yaml`](entities/automation/fan/will_s_office_fan/control.yaml)
</details>

<details><summary><code>/gh-cli/user-updated</code></summary>

**Entity ID: `automation.gh_cli_user_updated`**

> Keep the input select up to date (e.g. if the user is changed in a different way)

- Alias: /gh-cli/user-updated
- ID: `gh_cli_user_updated`
- Mode: `restart`

File: [`automation/gh_cli/user_updated.yaml`](entities/automation/gh_cli/user_updated.yaml)
</details>

<details><summary><code>/homeassistant/clear-queued-service-reload</code></summary>

**Entity ID: `automation.homeassistant_clear_queued_service_reload`**

> *No description provided*

- Alias: /homeassistant/clear-queued-service-reload
- ID: `homeassistant_clear_queued_service_reload`
- Mode: `queued`
- Variables:

```json
{
  "domain": "{{ trigger.event.data.domain }}",
  "service_queue": "{{ state_attr('var.auto_reload_queue', 'service_queue') | default([]) }}"
}
```
File: [`automation/homeassistant/clear_queued_service_reload.yaml`](entities/automation/homeassistant/clear_queued_service_reload.yaml)
</details>

<details><summary><code>/homeassistant/clear-service-reload-queue-on-start</code></summary>

**Entity ID: `automation.homeassistant_clear_service_reload_queue_on_start`**

> *No description provided*

- Alias: /homeassistant/clear-service-reload-queue-on-start
- ID: `homeassistant_clear_service_reload_queue_on_start`
- Mode: `single`
- Variables:

```json
{
  "empty_list": []
}
```
File: [`automation/homeassistant/clear_service_reload_queue_on_start.yaml`](entities/automation/homeassistant/clear_service_reload_queue_on_start.yaml)
</details>

<details><summary><code>/homeassistant/handle-service-reload</code></summary>

**Entity ID: `automation.homeassistant_handle_service_reload`**

> *No description provided*

- Alias: /homeassistant/handle-service-reload
- ID: `homeassistant_handle_service_reload`
- Mode: `queued`
- Variables:

```json
{
  "domain": "{% set parts = trigger.event.data.path.split(\"/\") %} {% if parts | length > 3 %}\n  {{ parts[3] }}\n{% endif %}",
  "service_mapping": {
    "media_player": "universal",
    "template_triggered": "template"
  },
  "service": "{{ service_mapping.get(domain, domain) }}",
  "orig_service_queue": "{{ state_attr('var.auto_reload_queue', 'service_queue') or [] }}",
  "reloadable_services": [
    "automation",
    "command_line",
    "conversation",
    "group",
    "input_boolean",
    "input_button",
    "input_datetime",
    "input_number",
    "input_select",
    "input_text",
    "mqtt",
    "rest",
    "rest_command",
    "scene",
    "schedule",
    "script",
    "template",
    "timer",
    "universal",
    "var",
    "zone"
  ],
  "auto_reload_boolean": "input_boolean.auto_reload_{{ service }}"
}
```
File: [`automation/homeassistant/handle_service_reload.yaml`](entities/automation/homeassistant/handle_service_reload.yaml)
</details>

<details><summary><code>/homeassistant/integrations/speedtest/reload</code></summary>

**Entity ID: `automation.homeassistant_integrations_speedtest_reload`**

> Reload speedtest config entry when any speedtest sensor becomes unavailable for 30 seconds

- Alias: /homeassistant/integrations/speedtest/reload
- ID: `homeassistant_integrations_speedtest_reload`
- Mode: `single`

File: [`automation/homeassistant/integrations/speedtest/reload.yaml`](entities/automation/homeassistant/integrations/speedtest/reload.yaml)
</details>

<details><summary><code>/homeassistant/load-gh-cli-on-start</code></summary>

**Entity ID: `automation.homeassistant_load_gh_cli_on_start`**

> *No description provided*

- Alias: /homeassistant/load-gh-cli-on-start
- ID: `homeassistant_load_gh_cli_on_start`
- Mode: `single`

File: [`automation/homeassistant/load_gh_cli_on_start.yaml`](entities/automation/homeassistant/load_gh_cli_on_start.yaml)
</details>

<details><summary><code>/input-boolean/air-purifier-quiet-mode/state-change</code></summary>

**Entity ID: `automation.input_boolean_air_purifier_quiet_mode_state_change`**

> *No description provided*

- Alias: /input-boolean/air-purifier-quiet-mode/state-change
- ID: `input_boolean_air_purifier_quiet_mode_state_change`
- Mode: `single`

File: [`automation/input_boolean/air_purifier_quiet_mode/state_change.yaml`](entities/automation/input_boolean/air_purifier_quiet_mode/state_change.yaml)
</details>

<details><summary><code>/input-boolean/air-purifier-quiet-mode/toggle</code></summary>

**Entity ID: `automation.input_boolean_air_purifier_quiet_mode_toggle`**

> *No description provided*

- Alias: /input-boolean/air-purifier-quiet-mode/toggle
- ID: `input_boolean_air_purifier_quiet_mode_toggle`
- Mode: `single`
- Variables:

```json
{
  "tv_is_on": "{{ states('remote.lounge_tv') | bool(false) }}"
}
```
File: [`automation/input_boolean/air_purifier_quiet_mode/toggle.yaml`](entities/automation/input_boolean/air_purifier_quiet_mode/toggle.yaml)
</details>

<details><summary><code>/input-boolean/lounge-lights-exercise-mode/off</code></summary>

**Entity ID: `automation.input_boolean_lounge_lights_exercise_mode_off`**

> Disable exercise mode - re-enable occupancy automation if it was enabled before

- Alias: /input-boolean/lounge-lights-exercise-mode/off
- ID: `input_boolean_lounge_lights_exercise_mode_off`
- Mode: `single`

File: [`automation/input_boolean/lounge_lights_exercise_mode/off.yaml`](entities/automation/input_boolean/lounge_lights_exercise_mode/off.yaml)
</details>

<details><summary><code>/input-boolean/lounge-lights-exercise-mode/on</code></summary>

**Entity ID: `automation.input_boolean_lounge_lights_exercise_mode_on`**

> Enable exercise mode - set lounge lights to 100% and disable occupancy automation

- Alias: /input-boolean/lounge-lights-exercise-mode/on
- ID: `input_boolean_lounge_lights_exercise_mode_on`
- Mode: `single`

File: [`automation/input_boolean/lounge_lights_exercise_mode/on.yaml`](entities/automation/input_boolean/lounge_lights_exercise_mode/on.yaml)
</details>

<details><summary><code>/input-datetime/home-assistant-start-time/set-datetime</code></summary>

**Entity ID: `automation.input_datetime_home_assistant_start_time_set_datetime`**

> *No description provided*

- Alias: /input-datetime/home-assistant-start-time/set-datetime
- ID: `input_datetime_home_assistant_start_time_set_datetime`
- Mode: `single`

File: [`automation/input_datetime/home_assistant_start_time/set_datetime.yaml`](entities/automation/input_datetime/home_assistant_start_time/set_datetime.yaml)
</details>

<details><summary><code>/input-datetime/next-bedroom-sunrise/sunrise-start</code></summary>

**Entity ID: `automation.input_datetime_next_bedroom_sunrise_sunrise_start`**

> Start the bedroom sunrise alarm when the scheduled time is reached

- Alias: /input-datetime/next-bedroom-sunrise/sunrise-start
- ID: `input_datetime_next_bedroom_sunrise_sunrise_start`
- Mode: `restart`
- Variables:

```json
{
  "original_start_time": "{{ states('input_datetime.next_bedroom_sunrise') }}",
  "max_brightness_pct": "{{ states('input_number.bedroom_sunrise_max_brightness') | int(100) }}",
  "sunrise_duration": "{{ states('input_number.bedroom_sunrise_duration') | int(30) }}"
}
```
File: [`automation/input_datetime/next_bedroom_sunrise/sunrise_start.yaml`](entities/automation/input_datetime/next_bedroom_sunrise/sunrise_start.yaml)
</details>

<details><summary><code>/input-select/gh-cli-active-user/option-selected</code></summary>

**Entity ID: `automation.input_select_gh_cli_active_user_option_selected`**

> Change the active user in the GH CLI and update the current user command line sensor

- Alias: /input-select/gh-cli-active-user/option-selected
- ID: `input_select_gh_cli_active_user_option_selected`
- Mode: `queued`

File: [`automation/input_select/gh_cli_active_user/option_selected.yaml`](entities/automation/input_select/gh_cli_active_user/option_selected.yaml)
</details>

<details><summary><code>/input-select/target-git-branch/option-selected</code></summary>

**Entity ID: `automation.input_select_target_git_branch_option_selected`**

> *No description provided*

- Alias: /input-select/target-git-branch/option-selected
- ID: `input_select_target_git_branch_option_selected`
- Mode: `queued`

File: [`automation/input_select/target_git_branch/option_selected.yaml`](entities/automation/input_select/target_git_branch/option_selected.yaml)
</details>

<details><summary><code>/input-select/target-git-branch/set-options</code></summary>

**Entity ID: `automation.input_select_target_git_branch_set_options`**

> *No description provided*

- Alias: /input-select/target-git-branch/set-options
- ID: `input_select_target_git_branch_set_options`
- Mode: `restart`

File: [`automation/input_select/target_git_branch/set_options.yaml`](entities/automation/input_select/target_git_branch/set_options.yaml)
</details>

<details><summary><code>/input-text/test-mqtt-events-device-name/log-event</code></summary>

**Entity ID: `automation.input_text_test_mqtt_events_device_name_log_event`**

> Log MQTT device events for the device name specified in input_text.test_mqtt_events_device_name. This automation listens to Zigbee2MQTT MQTT topics and filters by device name to capture device events.

- Alias: /input-text/test-mqtt-events-device-name/log-event
- ID: `input_text_test_mqtt_events_device_name_log_event`
- Mode: `queued`
- Variables:

```json
{
  "target_device_name": "{{ states('input_text.test_mqtt_events_device_name') }}",
  "topic_parts": "{{ trigger.topic.split('/') }}",
  "device_name_from_topic": "{{ topic_parts[1] if topic_parts | length > 1 else '' }}"
}
```
File: [`automation/input_text/test_mqtt_events_device_name/log_event.yaml`](entities/automation/input_text/test_mqtt_events_device_name/log_event.yaml)
</details>

<details><summary><code>/label/critical-battery/low-battery-alert</code></summary>

**Entity ID: `automation.label_critical_battery_low_battery_alert`**

> Check all entities with "Critical Battery" label every hour and alert if battery is below 5%

- Alias: /label/critical-battery/low-battery-alert
- ID: `label_critical_battery_low_battery_alert`
- Mode: `single`

File: [`automation/label/critical_battery/low_battery_alert.yaml`](entities/automation/label/critical_battery/low_battery_alert.yaml)
</details>

<details><summary><code>/label/radiator/all-off</code></summary>

**Entity ID: `automation.label_radiator_all_off`**

> Turn off central heating when all radiators are off

- Alias: /label/radiator/all-off
- ID: `label_radiator_all_off`
- Mode: `single`

File: [`automation/label/radiator/all_off.yaml`](entities/automation/label/radiator/all_off.yaml)
</details>

<details><summary><code>/label/radiator/any-on</code></summary>

**Entity ID: `automation.label_radiator_any_on`**

> Turn on central heating when any radiator turns on

- Alias: /label/radiator/any-on
- ID: `label_radiator_any_on`
- Mode: `single`

File: [`automation/label/radiator/any_on.yaml`](entities/automation/label/radiator/any_on.yaml)
</details>

<details><summary><code>/label/restore-state-after-room-vacancy/state-change</code></summary>

**Entity ID: `automation.label_restore_state_after_room_vacancy_state_change`**

> *No description provided*

- Alias: /label/restore-state-after-room-vacancy/state-change
- ID: `label_restore_state_after_room_vacancy_state_change`
- Mode: `restart`

File: [`automation/label/restore_state_after_room_vacancy/state_change.yaml`](entities/automation/label/restore_state_after_room_vacancy/state_change.yaml)
</details>

<details><summary><code>/light/bedroom-shapes/bon-appetit</code></summary>

**Entity ID: `automation.light_bedroom_shapes_bon_appetit`**

> Reset bedroom shapes to "bon appetit" effect at 10 AM

- Alias: /light/bedroom-shapes/bon-appetit
- ID: `light_bedroom_shapes_bon_appetit`
- Mode: `single`

File: [`automation/light/bedroom_shapes/bon_appetit.yaml`](entities/automation/light/bedroom_shapes/bon_appetit.yaml)
</details>

<details><summary><code>/light/lounge-lights/stop-tv-reflections</code></summary>

**Entity ID: `automation.light_lounge_lights_stop_tv_reflections`**

> *No description provided*

- Alias: /light/lounge-lights/stop-tv-reflections
- ID: `light_lounge_lights_stop_tv_reflections`
- Mode: `single`

File: [`automation/light/lounge_lights/stop_tv_reflections.yaml`](entities/automation/light/lounge_lights/stop_tv_reflections.yaml)
</details>

<details><summary><code>/light/lower-hallway-lights/timeout</code></summary>

**Entity ID: `automation.light_lower_hallway_lights_timeout`**

> *No description provided*

- Alias: /light/lower-hallway-lights/timeout
- ID: `light_lower_hallway_lights_timeout`
- Mode: `single`

File: [`automation/light/lower_hallway_lights/timeout.yaml`](entities/automation/light/lower_hallway_lights/timeout.yaml)
</details>

<details><summary><code>/light/moomin-box/on</code></summary>

**Entity ID: `automation.light_moomin_box_on`**

> The Moomin Box light only seems to actually turn on when the brightness value is changed - a simple state change doesn't work. This increments the brightness by 1 every time the light is turned on as a workaround.

- Alias: /light/moomin-box/on
- ID: `light_moomin_box_on`
- Mode: `single`

File: [`automation/light/moomin_box/on.yaml`](entities/automation/light/moomin_box/on.yaml)
</details>

<details><summary><code>/light/upper-landing-lights/on</code></summary>

**Entity ID: `automation.light_upper_landing_lights_on`**

> *No description provided*

- Alias: /light/upper-landing-lights/on
- ID: `light_upper_landing_lights_on`
- Mode: `single`
- Variables:

```json
{
  "brightness": "{{ states('sensor.lighting_modifier') | int(70) }}",
  "upper_landing_brightness": "{{\n  [states('sensor.lighting_modifier') | int(70), 20] | max\n  if 12 <= now().hour < 23\n  else states('sensor.lighting_modifier') | int(70)\n}}"
}
```
File: [`automation/light/upper_landing_lights/on.yaml`](entities/automation/light/upper_landing_lights/on.yaml)
</details>

<details><summary><code>/light/upper-landing-lights/timeout</code></summary>

**Entity ID: `automation.light_upper_landing_lights_timeout`**

> *No description provided*

- Alias: /light/upper-landing-lights/timeout
- ID: `light_upper_landing_lights_timeout`
- Mode: `single`

File: [`automation/light/upper_landing_lights/timeout.yaml`](entities/automation/light/upper_landing_lights/timeout.yaml)
</details>

<details><summary><code>/light/vic-s-office/rain-flash</code></summary>

**Entity ID: `automation.light_vic_s_office_rain_flash`**

> *No description provided*

- Alias: /light/vic-s-office/rain-flash
- ID: `light_vic_s_office_rain_flash`
- Mode: `single`
- Variables:

```json
{
  "original_state": "{{ is_state('light.vic_s_office', 'on') }}",
  "original_brightness": "{{ state_attr('light.vic_s_office', 'brightness') | int(128) }}",
  "original_rgb_color": "{{\n  state_attr('light.vic_s_office', 'rgb_color') | default([255, 255, 255])\n}}",
  "last_flash_time": "{{ states('input_datetime.rain_flash_cooldown') }}",
  "cooldown_expired": "{{ (as_timestamp(now()) - as_timestamp(last_flash_time)) > 3600 }}"
}
```
File: [`automation/light/vic_s_office/rain_flash.yaml`](entities/automation/light/vic_s_office/rain_flash.yaml)
</details>

<details><summary><code>/light/wardrobe-lights/auto-off</code></summary>

**Entity ID: `automation.light_wardrobe_lights_auto_off`**

> *No description provided*

- Alias: /light/wardrobe-lights/auto-off
- ID: `light_wardrobe_lights_auto_off`
- Mode: `single`

File: [`automation/light/wardrobe_lights/auto_off.yaml`](entities/automation/light/wardrobe_lights/auto_off.yaml)
</details>

<details><summary><code>/light/wardrobe-lights/toggle</code></summary>

**Entity ID: `automation.light_wardrobe_lights_toggle`**

> *No description provided*

- Alias: /light/wardrobe-lights/toggle
- ID: `light_wardrobe_lights_toggle`
- Mode: `queued`

File: [`automation/light/wardrobe_lights/toggle.yaml`](entities/automation/light/wardrobe_lights/toggle.yaml)
</details>

<details><summary><code>/light/will-s-office-grow-light/off</code></summary>

**Entity ID: `automation.light_will_s_office_grow_light_off`**

> Turn off grow light when any condition becomes invalid: office occupied, light outside, openings detected, or doors open.

- Alias: /light/will-s-office-grow-light/off
- ID: `light_will_s_office_grow_light_off`
- Mode: `restart`

File: [`automation/light/will_s_office_grow_light/off.yaml`](entities/automation/light/will_s_office_grow_light/off.yaml)
</details>

<details><summary><code>/light/will-s-office-grow-light/on</code></summary>

**Entity ID: `automation.light_will_s_office_grow_light_on`**

> Turn on grow light when office is unoccupied, dark outside, openings are secured, and blinds are closed (before midnight) or will be closed by automation (after midnight).

- Alias: /light/will-s-office-grow-light/on
- ID: `light_will_s_office_grow_light_on`
- Mode: `restart`

File: [`automation/light/will_s_office_grow_light/on.yaml`](entities/automation/light/will_s_office_grow_light/on.yaml)
</details>

<details><summary><code>/light/will-s-office-shapes/reboot-on-unavailable</code></summary>

**Entity ID: `automation.light_will_s_office_shapes_reboot_on_unavailable`**

> Reboot Will's office shapes if unavailable for 2 minutes

- Alias: /light/will-s-office-shapes/reboot-on-unavailable
- ID: `light_will_s_office_shapes_reboot_on_unavailable`
- Mode: `single`

File: [`automation/light/will_s_office_shapes/reboot_on_unavailable.yaml`](entities/automation/light/will_s_office_shapes/reboot_on_unavailable.yaml)
</details>

<details><summary><code>/light/will-s-office-voice-assistant-led-ring/door-open-flash</code></summary>

**Entity ID: `automation.light_will_s_office_voice_assistant_led_ring_door_open_flash`**

> Flashes Will's office voice assistant LED ring red at 100% brightness when the office door is opened, then restores the previous color and brightness.

- Alias: /light/will-s-office-voice-assistant-led-ring/door-open-flash
- ID: `light_will_s_office_voice_assistant_led_ring_door_open_flash`
- Mode: `single`
- Variables:

```json
{
  "was_on": "{{ is_state('light.will_s_office_voice_assistant_led_ring', 'on') }}",
  "saved_color": "{{ state_attr('light.will_s_office_voice_assistant_led_ring', 'rgb_color') }}",
  "saved_brightness": "{{\n  state_attr('light.will_s_office_voice_assistant_led_ring', 'brightness')\n}}"
}
```
File: [`automation/light/will_s_office_voice_assistant_led_ring/door_open_flash.yaml`](entities/automation/light/will_s_office_voice_assistant_led_ring/door_open_flash.yaml)
</details>

<details><summary><code>/media-player/topaz-sr10/off</code></summary>

**Entity ID: `automation.media_player_topaz_sr10_off`**

> Run when the Topaz SR10 is turned off, this resets the `input_number.topaz_sr10_volume_level` to -50 so that it is correct next time the amp is turned on.

- Alias: /media-player/topaz-sr10/off
- ID: `media_player_topaz_sr10_off`
- Mode: `single`

File: [`automation/media_player/topaz_sr10/off.yaml`](entities/automation/media_player/topaz_sr10/off.yaml)
</details>

<details><summary><code>/media-player/topaz-sr10/on</code></summary>

**Entity ID: `automation.media_player_topaz_sr10_on`**

> Run when the Topaz SR10 media player entity is turned on, this ensures the plug is turned on and that the volume is initialized to a reasonable level for the speakers.

- Alias: /media-player/topaz-sr10/on
- ID: `media_player_topaz_sr10_on`
- Mode: `single`

File: [`automation/media_player/topaz_sr10/on.yaml`](entities/automation/media_player/topaz_sr10/on.yaml)
</details>

<details><summary><code>/media-player/topaz-sr10/timeout</code></summary>

**Entity ID: `automation.media_player_topaz_sr10_timeout`**

> Artificially timeout the Topaz SR10 after a period of inactivity

- Alias: /media-player/topaz-sr10/timeout
- ID: `media_player_topaz_sr10_timeout`
- Mode: `single`

File: [`automation/media_player/topaz_sr10/timeout.yaml`](entities/automation/media_player/topaz_sr10/timeout.yaml)
</details>

<details><summary><code>/mobile-app/notification-action/bedroom-sunrise-delay</code></summary>

**Entity ID: `automation.mobile_app_notification_action_bedroom_sunrise_delay`**

> Handle delay for sunrise alarm (15 or 60 minutes)

- Alias: /mobile-app/notification-action/bedroom-sunrise-delay
- ID: `mobile_app_notification_action_bedroom_sunrise_delay`
- Mode: `single`
- Variables:

```json
{
  "delay_minutes": "{% if trigger.id == 'BEDROOM_SUNRISE_DELAY_15' %}\n  15\n{% elif trigger.id == 'BEDROOM_SUNRISE_DELAY_30' %}\n  30\n{% elif trigger.id == 'BEDROOM_SUNRISE_DELAY_60' %}\n  60\n{% endif %}"
}
```
File: [`automation/mobile_app/notification_action/bedroom_sunrise_delay.yaml`](entities/automation/mobile_app/notification_action/bedroom_sunrise_delay.yaml)
</details>

<details><summary><code>/mobile-app/notification-action/bedroom-sunrise-stop</code></summary>

**Entity ID: `automation.mobile_app_notification_action_bedroom_sunrise_stop`**

> Stop the sunrise alarm completely

- Alias: /mobile-app/notification-action/bedroom-sunrise-stop
- ID: `mobile_app_notification_action_bedroom_sunrise_stop`
- Mode: `single`

File: [`automation/mobile_app/notification_action/bedroom_sunrise_stop.yaml`](entities/automation/mobile_app/notification_action/bedroom_sunrise_stop.yaml)
</details>

<details><summary><code>/mobile-app/notification-action/central-heating-turn-off</code></summary>

**Entity ID: `automation.mobile_app_notification_action_central_heating_turn_off`**

> Turn off central heating from notification action

- Alias: /mobile-app/notification-action/central-heating-turn-off
- ID: `mobile_app_notification_action_central_heating_turn_off`
- Mode: `single`

File: [`automation/mobile_app/notification_action/central_heating_turn_off.yaml`](entities/automation/mobile_app/notification_action/central_heating_turn_off.yaml)
</details>

<details><summary><code>/mtrxpi/content-trigger/audio-visualiser</code></summary>

**Entity ID: `automation.mtrxpi_content_trigger_audio_visualiser`**

> *No description provided*

- Alias: /mtrxpi/content-trigger/audio-visualiser
- ID: `mtrxpi_content_trigger_audio_visualiser`
- Mode: `queued`

File: [`automation/mtrxpi/content_trigger/audio_visualiser.yaml`](entities/automation/mtrxpi/content_trigger/audio_visualiser.yaml)
</details>

<details><summary><code>/mtrxpi/content-trigger/clock</code></summary>

**Entity ID: `automation.mtrxpi_content_trigger_clock`**

> *No description provided*

- Alias: /mtrxpi/content-trigger/clock
- ID: `mtrxpi_content_trigger_clock`
- Mode: `queued`

File: [`automation/mtrxpi/content_trigger/clock.yaml`](entities/automation/mtrxpi/content_trigger/clock.yaml)
</details>

<details><summary><code>/mtrxpi/content-trigger/gif-door-animated</code></summary>

**Entity ID: `automation.mtrxpi_content_trigger_gif_door_animated`**

> *No description provided*

- Alias: /mtrxpi/content-trigger/gif-door-animated
- ID: `mtrxpi_content_trigger_gif_door_animated`
- Mode: `queued`

File: [`automation/mtrxpi/content_trigger/gif_door_animated.yaml`](entities/automation/mtrxpi/content_trigger/gif_door_animated.yaml)
</details>

<details><summary><code>/mtrxpi/content-trigger/now-playing</code></summary>

**Entity ID: `automation.mtrxpi_content_trigger_now_playing`**

> *No description provided*

- Alias: /mtrxpi/content-trigger/now-playing
- ID: `mtrxpi_content_trigger_now_playing`
- Mode: `queued`
- Variables:

```json
{
  "media_player": "{{ states('input_select.mtrxpi_media_player_source') }}",
  "artwork_uri": "{% set url = trigger.to_state.attributes.entity_picture | default(None) %} {%\n  set host = (\n    states('sensor.local_ip')\n    if has_value('sensor.local_ip')\n    else \"homeassistant.local\"\n  )\n%} {{\n  \"http://\" ~ host ~ \":8123\" ~ url\n  if url is string and url.startswith(\"/api/\")\n  else url\n}}"
}
```
File: [`automation/mtrxpi/content_trigger/now_playing.yaml`](entities/automation/mtrxpi/content_trigger/now_playing.yaml)
</details>

<details><summary><code>/mtrxpi/content-trigger/raining-grid</code></summary>

**Entity ID: `automation.mtrxpi_content_trigger_raining_grid`**

> *No description provided*

- Alias: /mtrxpi/content-trigger/raining-grid
- ID: `mtrxpi_content_trigger_raining_grid`
- Mode: `queued`
- Variables:

```json
{
  "rain": "{{ trigger.to_state.state | float(0) }}",
  "limit": "{{ states('input_number.mtrxpi_raining_grid_maximum_rain_intensity') | float(15) }}",
  "rain_chance": "{{ ( rain | float(0) * (100 / limit) ) | round(2) }}"
}
```
File: [`automation/mtrxpi/content_trigger/raining_grid.yaml`](entities/automation/mtrxpi/content_trigger/raining_grid.yaml)
</details>

<details><summary><code>/notification/apollo-plt1b/ota-mode-off</code></summary>

**Entity ID: `automation.notification_apollo_plt1b_ota_mode_off`**

> Clear Apollo PLT-1B OTA mode notification when OTA mode is turned off

- Alias: /notification/apollo-plt1b/ota-mode-off
- ID: `notification_apollo_plt1b_ota_mode_off`
- Mode: `single`

File: [`automation/notification/apollo_plt1b/ota_mode_off.yaml`](entities/automation/notification/apollo_plt1b/ota_mode_off.yaml)
</details>

<details><summary><code>/notification/apollo-plt1b/ota-mode-on</code></summary>

**Entity ID: `automation.notification_apollo_plt1b_ota_mode_on`**

> *No description provided*

- Alias: /notification/apollo-plt1b/ota-mode-on
- ID: `notification_apollo_plt1b_ota_mode_on`
- Mode: `single`
- Variables:

```json
{
  "online": "{%- set ns = namespace(plants=[]) %} {%- set all_plants = {\n  'binary_sensor.apollo_plt_1b_1510d0_online': 'Begonia',\n  'binary_sensor.apollo_plt_1b_1511bc_online': 'Coleus',\n  'binary_sensor.apollo_plt_1b_151430_online': 'Monstera',\n  'binary_sensor.apollo_plt_1b_1743a8_online': 'Spider Plant'\n} %} {%- for entity_id, name in all_plants.items() %}\n  {%- if is_state(entity_id, 'on') %}\n    {%- set ns.plants = ns.plants + [name] %}\n  {%- endif %}\n{%- endfor %} {{ ns.plants }}"
}
```
File: [`automation/notification/apollo_plt1b/ota_mode_on.yaml`](entities/automation/notification/apollo_plt1b/ota_mode_on.yaml)
</details>

<details><summary><code>/notification/apollo-plt1b/turn-ota-mode-off</code></summary>

**Entity ID: `automation.notification_apollo_plt1b_turn_ota_mode_off`**

> Turn off Apollo OTA mode when notification action is pressed

- Alias: /notification/apollo-plt1b/turn-ota-mode-off
- ID: `notification_apollo_plt1b_turn_ota_mode_off`
- Mode: `single`

File: [`automation/notification/apollo_plt1b/turn_ota_mode_off.yaml`](entities/automation/notification/apollo_plt1b/turn_ota_mode_off.yaml)
</details>

<details><summary><code>/notification/heating-invalid-state</code></summary>

**Entity ID: `automation.notification_heating_invalid_state`**

> Notify when heating is on but shouldn't be (e.g. SwitchBot failure, low battery)

- Alias: /notification/heating-invalid-state
- ID: `notification_heating_invalid_state`
- Mode: `single`

File: [`automation/notification/heating_invalid_state.yaml`](entities/automation/notification/heating_invalid_state.yaml)
</details>

<details><summary><code>/notification/prusa-i3/print-completed</code></summary>

**Entity ID: `automation.notification_prusa_i3_print_completed`**

> *No description provided*

- Alias: /notification/prusa-i3/print-completed
- ID: `notification_prusa_i3_print_completed`
- Mode: `single`

File: [`automation/notification/prusa_i3/print_completed.yaml`](entities/automation/notification/prusa_i3/print_completed.yaml)
</details>

<details><summary><code>/notification/prusa-i3/user-input-required</code></summary>

**Entity ID: `automation.notification_prusa_i3_user_input_required`**

> *No description provided*

- Alias: /notification/prusa-i3/user-input-required
- ID: `notification_prusa_i3_user_input_required`
- Mode: `single`

File: [`automation/notification/prusa_i3/user_input_required.yaml`](entities/automation/notification/prusa_i3/user_input_required.yaml)
</details>

<details><summary><code>/notification/rain-door-open-alert</code></summary>

**Entity ID: `automation.notification_rain_door_open_alert`**

> Alert Will when it starts to rain and the roof terrace door is open

- Alias: /notification/rain-door-open-alert
- ID: `notification_rain_door_open_alert`
- Mode: `single`

File: [`automation/notification/rain_door_open_alert.yaml`](entities/automation/notification/rain_door_open_alert.yaml)
</details>

<details><summary><code>/octopi/cpu-fan-control</code></summary>

**Entity ID: `automation.octopi_cpu_fan_control`**

> *No description provided*

- Alias: /octopi/cpu-fan-control
- ID: `octopi_cpu_fan_control`
- Mode: `restart`
- Variables:

```json
{
  "cpu_temp": "{{ states('sensor.octopi_cpu_temperature') | float(0) }}",
  "threshold": "{{ states('input_number.octopi_fan_auto_on_threshold') | int(999) }}",
  "should_be_on": "{{ cpu_temp | float(0) > threshold | int(999) }}"
}
```
File: [`automation/octopi/cpu_fan_control.yaml`](entities/automation/octopi/cpu_fan_control.yaml)
</details>

<details><summary><code>/person/nobody-home</code></summary>

**Entity ID: `automation.person_nobody_home`**

> Turn off all physical devices when nobody is home

- Alias: /person/nobody-home
- ID: `person_nobody_home`
- Mode: `restart`

File: [`automation/person/nobody_home.yaml`](entities/automation/person/nobody_home.yaml)
</details>

<details><summary><code>/person/will/home</code></summary>

**Entity ID: `automation.person_will_home`**

> *No description provided*

- Alias: /person/will/home
- ID: `person_will_home`
- Mode: `single`

File: [`automation/person/will/home.yaml`](entities/automation/person/will/home.yaml)
</details>

<details><summary><code>/person/will/leaving-work</code></summary>

**Entity ID: `automation.person_will_leaving_work`**

> *No description provided*

- Alias: /person/will/leaving-work
- ID: `person_will_leaving_work`
- Mode: `single`

File: [`automation/person/will/leaving_work.yaml`](entities/automation/person/will/leaving_work.yaml)
</details>

<details><summary><code>/prusa-i3/bed/timeout</code></summary>

**Entity ID: `automation.prusa_i3_bed_timeout`**

> *No description provided*

- Alias: /prusa-i3/bed/timeout
- ID: `prusa_i3_bed_timeout`
- Mode: `single`

File: [`automation/prusa_i3/bed/timeout.yaml`](entities/automation/prusa_i3/bed/timeout.yaml)
</details>

<details><summary><code>/prusa-i3/hotend/timeout</code></summary>

**Entity ID: `automation.prusa_i3_hotend_timeout`**

> *No description provided*

- Alias: /prusa-i3/hotend/timeout
- ID: `prusa_i3_hotend_timeout`
- Mode: `single`

File: [`automation/prusa_i3/hotend/timeout.yaml`](entities/automation/prusa_i3/hotend/timeout.yaml)
</details>

<details><summary><code>/remote/basement-remote/double-left</code></summary>

**Entity ID: `automation.remote_basement_remote_double_left`**

> Set dining area lights to 100% and disable automations

- Alias: /remote/basement-remote/double-left
- ID: `remote_basement_remote_double_left`
- Mode: `single`

File: [`automation/remote/basement_remote/double_left.yaml`](entities/automation/remote/basement_remote/double_left.yaml)
</details>

<details><summary><code>/remote/basement-remote/double-right</code></summary>

**Entity ID: `automation.remote_basement_remote_double_right`**

> Set kitchen lights to 100% and disable automations

- Alias: /remote/basement-remote/double-right
- ID: `remote_basement_remote_double_right`
- Mode: `single`

File: [`automation/remote/basement_remote/double_right.yaml`](entities/automation/remote/basement_remote/double_right.yaml)
</details>

<details><summary><code>/remote/basement-remote/hold-left</code></summary>

**Entity ID: `automation.remote_basement_remote_hold_left`**

> Reset dining area - re-enable automations and trigger lighting based on occupancy

- Alias: /remote/basement-remote/hold-left
- ID: `remote_basement_remote_hold_left`
- Mode: `single`

File: [`automation/remote/basement_remote/hold_left.yaml`](entities/automation/remote/basement_remote/hold_left.yaml)
</details>

<details><summary><code>/remote/basement-remote/hold-right</code></summary>

**Entity ID: `automation.remote_basement_remote_hold_right`**

> Reset kitchen room - re-enable automations and trigger lighting based on occupancy

- Alias: /remote/basement-remote/hold-right
- ID: `remote_basement_remote_hold_right`
- Mode: `single`

File: [`automation/remote/basement_remote/hold_right.yaml`](entities/automation/remote/basement_remote/hold_right.yaml)
</details>

<details><summary><code>/remote/basement-remote/single-left</code></summary>

**Entity ID: `automation.remote_basement_remote_single_left`**

> Set dining area lights to lighting modifier and disable automations

- Alias: /remote/basement-remote/single-left
- ID: `remote_basement_remote_single_left`
- Mode: `single`

File: [`automation/remote/basement_remote/single_left.yaml`](entities/automation/remote/basement_remote/single_left.yaml)
</details>

<details><summary><code>/remote/basement-remote/single-right</code></summary>

**Entity ID: `automation.remote_basement_remote_single_right`**

> Set kitchen lights to occupied state brightness and disable automations

- Alias: /remote/basement-remote/single-right
- ID: `remote_basement_remote_single_right`
- Mode: `single`

File: [`automation/remote/basement_remote/single_right.yaml`](entities/automation/remote/basement_remote/single_right.yaml)
</details>

<details><summary><code>/remote/basement-remote/triple-left</code></summary>

**Entity ID: `automation.remote_basement_remote_triple_left`**

> Set dining area big light to 100%, spotlights/shelves to min(modifier, 20%), and kitchen to empty state and disable automations

- Alias: /remote/basement-remote/triple-left
- ID: `remote_basement_remote_triple_left`
- Mode: `single`

File: [`automation/remote/basement_remote/triple_left.yaml`](entities/automation/remote/basement_remote/triple_left.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/down-press</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_down_press`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/down-press
- ID: `remote_bedroom_hue_remote_down_press`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/down_press.yaml`](entities/automation/remote/bedroom_hue_remote/down_press.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/off-hold</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_off_hold`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/off-hold
- ID: `remote_bedroom_hue_remote_off_hold`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/off_hold.yaml`](entities/automation/remote/bedroom_hue_remote/off_hold.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/off-press</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_off_press`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/off-press
- ID: `remote_bedroom_hue_remote_off_press`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/off_press.yaml`](entities/automation/remote/bedroom_hue_remote/off_press.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/on-hold</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_on_hold`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/on-hold
- ID: `remote_bedroom_hue_remote_on_hold`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/on_hold.yaml`](entities/automation/remote/bedroom_hue_remote/on_hold.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/on-press</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_on_press`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/on-press
- ID: `remote_bedroom_hue_remote_on_press`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/on_press.yaml`](entities/automation/remote/bedroom_hue_remote/on_press.yaml)
</details>

<details><summary><code>/remote/bedroom-hue-remote/up-press</code></summary>

**Entity ID: `automation.remote_bedroom_hue_remote_up_press`**

> *No description provided*

- Alias: /remote/bedroom-hue-remote/up-press
- ID: `remote_bedroom_hue_remote_up_press`
- Mode: `single`

File: [`automation/remote/bedroom_hue_remote/up_press.yaml`](entities/automation/remote/bedroom_hue_remote/up_press.yaml)
</details>

<details><summary><code>/remote/bedroom-remote/arrow-left-click</code></summary>

**Entity ID: `automation.remote_bedroom_remote_arrow_left_click`**

> *No description provided*

- Alias: /remote/bedroom-remote/arrow-left-click
- ID: `remote_bedroom_remote_arrow_left_click`
- Mode: `single`

File: [`automation/remote/bedroom_remote/arrow_left_click.yaml`](entities/automation/remote/bedroom_remote/arrow_left_click.yaml)
</details>

<details><summary><code>/remote/bedroom-remote/brightness-move-down</code></summary>

**Entity ID: `automation.remote_bedroom_remote_brightness_move_down`**

> *No description provided*

- Alias: /remote/bedroom-remote/brightness-move-down
- ID: `remote_bedroom_remote_brightness_move_down`
- Mode: `single`

File: [`automation/remote/bedroom_remote/brightness_move_down.yaml`](entities/automation/remote/bedroom_remote/brightness_move_down.yaml)
</details>

<details><summary><code>/remote/bedroom-remote/brightness-move-up</code></summary>

**Entity ID: `automation.remote_bedroom_remote_brightness_move_up`**

> *No description provided*

- Alias: /remote/bedroom-remote/brightness-move-up
- ID: `remote_bedroom_remote_brightness_move_up`
- Mode: `single`

File: [`automation/remote/bedroom_remote/brightness_move_up.yaml`](entities/automation/remote/bedroom_remote/brightness_move_up.yaml)
</details>

<details><summary><code>/remote/bedroom-remote/off</code></summary>

**Entity ID: `automation.remote_bedroom_remote_off`**

> *No description provided*

- Alias: /remote/bedroom-remote/off
- ID: `remote_bedroom_remote_off`
- Mode: `single`

File: [`automation/remote/bedroom_remote/off.yaml`](entities/automation/remote/bedroom_remote/off.yaml)
</details>

<details><summary><code>/remote/bedroom-remote/on</code></summary>

**Entity ID: `automation.remote_bedroom_remote_on`**

> *No description provided*

- Alias: /remote/bedroom-remote/on
- ID: `remote_bedroom_remote_on`
- Mode: `single`

File: [`automation/remote/bedroom_remote/on.yaml`](entities/automation/remote/bedroom_remote/on.yaml)
</details>

<details><summary><code>/remote/charging-hub-button/single</code></summary>

**Entity ID: `automation.remote_charging_hub_button_single`**

> Toggle the charging hub's power state

- Alias: /remote/charging-hub-button/single
- ID: `remote_charging_hub_button_single`
- Mode: `single`

File: [`automation/remote/charging_hub_button/single.yaml`](entities/automation/remote/charging_hub_button/single.yaml)
</details>

<details><summary><code>/remote/coffee-table/double</code></summary>

**Entity ID: `automation.remote_coffee_table_double`**

> Control the TV to use the speakrers as the audio output

- Alias: /remote/coffee-table/double
- ID: `remote_coffee_table_double`
- Mode: `single`
- Variables:

```json
{
  "delay_ms": 750,
  "codes": {
    "action_menu": "BUwJZgKcBIADAxoCZgJAC0AHQAPgCwtAAcAbA5wEB1DgAz9AAQOcBGYCwAHgDwtAAUAbAZwE4AU/wFdAB0ABA5wEZgLAAeADC0ABQA8BnATgBT9AAQOcBGYCwAHgDwtAAUAbAZwE4N0/QU8DnARmAkAHwANADwGcBOAF/0AbA5wEZgJAB0AD4AULA70CGgLgAQMJnAS9ApwEB1BMCQ==",
    "down": "B24JWwKtBFsCQAHgAwdAC8AD4AUBAUVg4FszAbcC4F1nAVsC4ChnAgJbAg==",
    "enter": "B2IJWgKuBFoCQAHAB0ABQAvAA+AFAQW9YmIJWgJAG0ABwAdAAUALwAPgBQHgxDMCAloC"
  }
}
```
File: [`automation/remote/coffee_table/double.yaml`](entities/automation/remote/coffee_table/double.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/down-press</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_down_press`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/down-press
- ID: `remote_lounge_hue_remote_down_press`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/down_press.yaml`](entities/automation/remote/lounge_hue_remote/down_press.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/off-hold</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_off_hold`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/off-hold
- ID: `remote_lounge_hue_remote_off_hold`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/off_hold.yaml`](entities/automation/remote/lounge_hue_remote/off_hold.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/off-press</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_off_press`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/off-press
- ID: `remote_lounge_hue_remote_off_press`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/off_press.yaml`](entities/automation/remote/lounge_hue_remote/off_press.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/on-hold</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_on_hold`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/on-hold
- ID: `remote_lounge_hue_remote_on_hold`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/on_hold.yaml`](entities/automation/remote/lounge_hue_remote/on_hold.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/on-press</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_on_press`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/on-press
- ID: `remote_lounge_hue_remote_on_press`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/on_press.yaml`](entities/automation/remote/lounge_hue_remote/on_press.yaml)
</details>

<details><summary><code>/remote/lounge-hue-remote/up-press</code></summary>

**Entity ID: `automation.remote_lounge_hue_remote_up_press`**

> *No description provided*

- Alias: /remote/lounge-hue-remote/up-press
- ID: `remote_lounge_hue_remote_up_press`
- Mode: `single`

File: [`automation/remote/lounge_hue_remote/up_press.yaml`](entities/automation/remote/lounge_hue_remote/up_press.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/down-press</code></summary>

**Entity ID: `automation.remote_office_hue_remote_down_press`**

> *No description provided*

- Alias: /remote/office-hue-remote/down-press
- ID: `remote_office_hue_remote_down_press`
- Mode: `single`

File: [`automation/remote/office_hue_remote/down_press.yaml`](entities/automation/remote/office_hue_remote/down_press.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/off-hold</code></summary>

**Entity ID: `automation.remote_office_hue_remote_off_hold`**

> *No description provided*

- Alias: /remote/office-hue-remote/off-hold
- ID: `remote_office_hue_remote_off_hold`
- Mode: `single`

File: [`automation/remote/office_hue_remote/off_hold.yaml`](entities/automation/remote/office_hue_remote/off_hold.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/off-press</code></summary>

**Entity ID: `automation.remote_office_hue_remote_off_press`**

> *No description provided*

- Alias: /remote/office-hue-remote/off-press
- ID: `remote_office_hue_remote_off_press`
- Mode: `single`

File: [`automation/remote/office_hue_remote/off_press.yaml`](entities/automation/remote/office_hue_remote/off_press.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/on-hold</code></summary>

**Entity ID: `automation.remote_office_hue_remote_on_hold`**

> *No description provided*

- Alias: /remote/office-hue-remote/on-hold
- ID: `remote_office_hue_remote_on_hold`
- Mode: `single`

File: [`automation/remote/office_hue_remote/on_hold.yaml`](entities/automation/remote/office_hue_remote/on_hold.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/on-press</code></summary>

**Entity ID: `automation.remote_office_hue_remote_on_press`**

> *No description provided*

- Alias: /remote/office-hue-remote/on-press
- ID: `remote_office_hue_remote_on_press`
- Mode: `single`

File: [`automation/remote/office_hue_remote/on_press.yaml`](entities/automation/remote/office_hue_remote/on_press.yaml)
</details>

<details><summary><code>/remote/office-hue-remote/up-press</code></summary>

**Entity ID: `automation.remote_office_hue_remote_up_press`**

> *No description provided*

- Alias: /remote/office-hue-remote/up-press
- ID: `remote_office_hue_remote_up_press`
- Mode: `single`

File: [`automation/remote/office_hue_remote/up_press.yaml`](entities/automation/remote/office_hue_remote/up_press.yaml)
</details>

<details><summary><code>/remote/prusa-i3-mk3-power/double-press</code></summary>

**Entity ID: `automation.remote_prusa_i3_mk3_power_double_press`**

> *No description provided*

- Alias: /remote/prusa-i3-mk3-power/double-press
- ID: `remote_prusa_i3_mk3_power_double_press`
- Mode: `single`

File: [`automation/remote/prusa_i3_mk3_power/double_press.yaml`](entities/automation/remote/prusa_i3_mk3_power/double_press.yaml)
</details>

<details><summary><code>/remote/prusa-i3-mk3-power/single-press</code></summary>

**Entity ID: `automation.remote_prusa_i3_mk3_power_single_press`**

> *No description provided*

- Alias: /remote/prusa-i3-mk3-power/single-press
- ID: `remote_prusa_i3_mk3_power_single_press`
- Mode: `single`

File: [`automation/remote/prusa_i3_mk3_power/single_press.yaml`](entities/automation/remote/prusa_i3_mk3_power/single_press.yaml)
</details>

<details><summary><code>/remote/spare-room/ball-lamp-remote/brightness-move-down</code></summary>

**Entity ID: `automation.remote_spare_room_ball_lamp_remote_brightness_move_down`**

> *No description provided*

- Alias: /remote/spare-room/ball-lamp-remote/brightness-move-down
- ID: `remote_spare_room_ball_lamp_remote_brightness_move_down`
- Mode: `single`

File: [`automation/remote/spare_room/ball_lamp_remote/brightness_move_down.yaml`](entities/automation/remote/spare_room/ball_lamp_remote/brightness_move_down.yaml)
</details>

<details><summary><code>/remote/spare-room/ball-lamp-remote/brightness-move-up</code></summary>

**Entity ID: `automation.remote_spare_room_ball_lamp_remote_brightness_move_up`**

> *No description provided*

- Alias: /remote/spare-room/ball-lamp-remote/brightness-move-up
- ID: `remote_spare_room_ball_lamp_remote_brightness_move_up`
- Mode: `single`

File: [`automation/remote/spare_room/ball_lamp_remote/brightness_move_up.yaml`](entities/automation/remote/spare_room/ball_lamp_remote/brightness_move_up.yaml)
</details>

<details><summary><code>/remote/spare-room/ball-lamp-remote/off</code></summary>

**Entity ID: `automation.remote_spare_room_ball_lamp_remote_off`**

> *No description provided*

- Alias: /remote/spare-room/ball-lamp-remote/off
- ID: `remote_spare_room_ball_lamp_remote_off`
- Mode: `single`

File: [`automation/remote/spare_room/ball_lamp_remote/off.yaml`](entities/automation/remote/spare_room/ball_lamp_remote/off.yaml)
</details>

<details><summary><code>/remote/spare-room/ball-lamp-remote/on</code></summary>

**Entity ID: `automation.remote_spare_room_ball_lamp_remote_on`**

> *No description provided*

- Alias: /remote/spare-room/ball-lamp-remote/on
- ID: `remote_spare_room_ball_lamp_remote_on`
- Mode: `single`

File: [`automation/remote/spare_room/ball_lamp_remote/on.yaml`](entities/automation/remote/spare_room/ball_lamp_remote/on.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/down-press</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_down_press`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/down-press
- ID: `remote_spare_room_hue_remote_down_press`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/down_press.yaml`](entities/automation/remote/spare_room/hue_remote/down_press.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/off-hold</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_off_hold`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/off-hold
- ID: `remote_spare_room_hue_remote_off_hold`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/off_hold.yaml`](entities/automation/remote/spare_room/hue_remote/off_hold.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/off-press</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_off_press`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/off-press
- ID: `remote_spare_room_hue_remote_off_press`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/off_press.yaml`](entities/automation/remote/spare_room/hue_remote/off_press.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/on-hold</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_on_hold`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/on-hold
- ID: `remote_spare_room_hue_remote_on_hold`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/on_hold.yaml`](entities/automation/remote/spare_room/hue_remote/on_hold.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/on-press</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_on_press`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/on-press
- ID: `remote_spare_room_hue_remote_on_press`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/on_press.yaml`](entities/automation/remote/spare_room/hue_remote/on_press.yaml)
</details>

<details><summary><code>/remote/spare-room/hue-remote/up-press</code></summary>

**Entity ID: `automation.remote_spare_room_hue_remote_up_press`**

> *No description provided*

- Alias: /remote/spare-room/hue-remote/up-press
- ID: `remote_spare_room_hue_remote_up_press`
- Mode: `single`

File: [`automation/remote/spare_room/hue_remote/up_press.yaml`](entities/automation/remote/spare_room/hue_remote/up_press.yaml)
</details>

<details><summary><code>/remote/vic-s-desk-remote/brightness-move-down</code></summary>

**Entity ID: `automation.remote_vic_s_desk_remote_brightness_move_down`**

> *No description provided*

- Alias: /remote/vic-s-desk-remote/brightness-move-down
- ID: `remote_vic_s_desk_remote_brightness_move_down`
- Mode: `single`

File: [`automation/remote/vic_s_desk_remote/brightness_move_down.yaml`](entities/automation/remote/vic_s_desk_remote/brightness_move_down.yaml)
</details>

<details><summary><code>/remote/vic-s-desk-remote/brightness-move-up</code></summary>

**Entity ID: `automation.remote_vic_s_desk_remote_brightness_move_up`**

> *No description provided*

- Alias: /remote/vic-s-desk-remote/brightness-move-up
- ID: `remote_vic_s_desk_remote_brightness_move_up`
- Mode: `single`

File: [`automation/remote/vic_s_desk_remote/brightness_move_up.yaml`](entities/automation/remote/vic_s_desk_remote/brightness_move_up.yaml)
</details>

<details><summary><code>/remote/vic-s-desk-remote/off</code></summary>

**Entity ID: `automation.remote_vic_s_desk_remote_off`**

> *No description provided*

- Alias: /remote/vic-s-desk-remote/off
- ID: `remote_vic_s_desk_remote_off`
- Mode: `single`

File: [`automation/remote/vic_s_desk_remote/off.yaml`](entities/automation/remote/vic_s_desk_remote/off.yaml)
</details>

<details><summary><code>/remote/vic-s-desk-remote/on</code></summary>

**Entity ID: `automation.remote_vic_s_desk_remote_on`**

> *No description provided*

- Alias: /remote/vic-s-desk-remote/on
- ID: `remote_vic_s_desk_remote_on`
- Mode: `single`

File: [`automation/remote/vic_s_desk_remote/on.yaml`](entities/automation/remote/vic_s_desk_remote/on.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/down-press</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_down_press`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/down-press
- ID: `remote_vic_s_office_hue_remote_down_press`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/down_press.yaml`](entities/automation/remote/vic_s_office_hue_remote/down_press.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/off-hold</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_off_hold`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/off-hold
- ID: `remote_vic_s_office_hue_remote_off_hold`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/off_hold.yaml`](entities/automation/remote/vic_s_office_hue_remote/off_hold.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/off-press</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_off_press`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/off-press
- ID: `remote_vic_s_office_hue_remote_off_press`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/off_press.yaml`](entities/automation/remote/vic_s_office_hue_remote/off_press.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/on-hold</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_on_hold`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/on-hold
- ID: `remote_vic_s_office_hue_remote_on_hold`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/on_hold.yaml`](entities/automation/remote/vic_s_office_hue_remote/on_hold.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/on-press</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_on_press`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/on-press
- ID: `remote_vic_s_office_hue_remote_on_press`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/on_press.yaml`](entities/automation/remote/vic_s_office_hue_remote/on_press.yaml)
</details>

<details><summary><code>/remote/vic-s-office-hue-remote/up-press</code></summary>

**Entity ID: `automation.remote_vic_s_office_hue_remote_up_press`**

> *No description provided*

- Alias: /remote/vic-s-office-hue-remote/up-press
- ID: `remote_vic_s_office_hue_remote_up_press`
- Mode: `single`

File: [`automation/remote/vic_s_office_hue_remote/up_press.yaml`](entities/automation/remote/vic_s_office_hue_remote/up_press.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-1/double</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_1_double`**

> *No description provided*

- Alias: /remote/will-s-desk/button-1/double
- ID: `remote_will_s_desk_button_1_double`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_1/double.yaml`](entities/automation/remote/will_s_desk/button_1/double.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-1/hold</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_1_hold`**

> *No description provided*

- Alias: /remote/will-s-desk/button-1/hold
- ID: `remote_will_s_desk_button_1_hold`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_1/hold.yaml`](entities/automation/remote/will_s_desk/button_1/hold.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-1/single</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_1_single`**

> *No description provided*

- Alias: /remote/will-s-desk/button-1/single
- ID: `remote_will_s_desk_button_1_single`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_1/single.yaml`](entities/automation/remote/will_s_desk/button_1/single.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-2/double</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_2_double`**

> *No description provided*

- Alias: /remote/will-s-desk/button-2/double
- ID: `remote_will_s_desk_button_2_double`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_2/double.yaml`](entities/automation/remote/will_s_desk/button_2/double.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-2/hold</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_2_hold`**

> *No description provided*

- Alias: /remote/will-s-desk/button-2/hold
- ID: `remote_will_s_desk_button_2_hold`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_2/hold.yaml`](entities/automation/remote/will_s_desk/button_2/hold.yaml)
</details>

<details><summary><code>/remote/will-s-desk/button-2/single</code></summary>

**Entity ID: `automation.remote_will_s_desk_button_2_single`**

> *No description provided*

- Alias: /remote/will-s-desk/button-2/single
- ID: `remote_will_s_desk_button_2_single`
- Mode: `single`

File: [`automation/remote/will_s_desk/button_2/single.yaml`](entities/automation/remote/will_s_desk/button_2/single.yaml)
</details>

<details><summary><code>/remote/will-s-office/doorbell/single-press</code></summary>

**Entity ID: `automation.remote_will_s_office_doorbell_single_press`**

> *No description provided*

- Alias: /remote/will-s-office/doorbell/single-press
- ID: `remote_will_s_office_doorbell_single_press`
- Mode: `single`

File: [`automation/remote/will_s_office/doorbell/single_press.yaml`](entities/automation/remote/will_s_office/doorbell/single_press.yaml)
</details>

<details><summary><code>/schedule/bedroom-heating-schedule/off</code></summary>

**Entity ID: `automation.schedule_bedroom_heating_schedule_off`**

> Turn off bedroom radiators when bedroom heating schedule turns off

- Alias: /schedule/bedroom-heating-schedule/off
- ID: `schedule_bedroom_heating_schedule_off`
- Mode: `single`

File: [`automation/schedule/bedroom_heating_schedule/off.yaml`](entities/automation/schedule/bedroom_heating_schedule/off.yaml)
</details>

<details><summary><code>/schedule/bedroom-heating-schedule/on</code></summary>

**Entity ID: `automation.schedule_bedroom_heating_schedule_on`**

> Activate bedroom heating when schedule turns on

- Alias: /schedule/bedroom-heating-schedule/on
- ID: `schedule_bedroom_heating_schedule_on`
- Mode: `single`

File: [`automation/schedule/bedroom_heating_schedule/on.yaml`](entities/automation/schedule/bedroom_heating_schedule/on.yaml)
</details>

<details><summary><code>/schedule/hot-water/off</code></summary>

**Entity ID: `automation.schedule_hot_water_off`**

> Turn off hot water when schedule turns off

- Alias: /schedule/hot-water/off
- ID: `schedule_hot_water_off`
- Mode: `single`

File: [`automation/schedule/hot_water/off.yaml`](entities/automation/schedule/hot_water/off.yaml)
</details>

<details><summary><code>/schedule/hot-water/on</code></summary>

**Entity ID: `automation.schedule_hot_water_on`**

> *No description provided*

- Alias: /schedule/hot-water/on
- ID: `schedule_hot_water_on`
- Mode: `single`

File: [`automation/schedule/hot_water/on.yaml`](entities/automation/schedule/hot_water/on.yaml)
</details>

<details><summary><code>/sensor/bedroom-climate-sensor-temperature/sync-radiator-trv</code></summary>

**Entity ID: `automation.sensor_bedroom_climate_sensor_temperature_sync_radiator_trv`**

> Sync radiator TRV external temperature input when bedroom climate sensor temperature updates

- Alias: /sensor/bedroom-climate-sensor-temperature/sync-radiator-trv
- ID: `sensor_bedroom_climate_sensor_temperature_sync_radiator_trv`
- Mode: `single`

File: [`automation/sensor/bedroom_climate_sensor_temperature/sync_radiator_trv.yaml`](entities/automation/sensor/bedroom_climate_sensor_temperature/sync_radiator_trv.yaml)
</details>

<details><summary><code>/sensor/kitchen-air-quality-sensor-temperature/sync-radiator-trv</code></summary>

**Entity ID: `automation.sensor_kitchen_air_quality_sensor_temperature_sync_radiator_trv`**

> Sync radiator TRV external temperature input when kitchen climate sensor temperature updates

- Alias: /sensor/kitchen-air-quality-sensor-temperature/sync-radiator-trv
- ID: `sensor_kitchen_air_quality_sensor_temperature_sync_radiator_trv`
- Mode: `single`

File: [`automation/sensor/kitchen_air_quality_sensor_temperature/sync_radiator_trv.yaml`](entities/automation/sensor/kitchen_air_quality_sensor_temperature/sync_radiator_trv.yaml)
</details>

<details><summary><code>/sensor/lighting-modifier/state</code></summary>

**Entity ID: `automation.sensor_lighting_modifier_state`**

> Sync entities with lighting modifier label when lighting modifier changes

- Alias: /sensor/lighting-modifier/state
- ID: `sensor_lighting_modifier_state`
- Mode: `queued`
- Variables:

```json
{
  "new_brightness": "{{ states('sensor.lighting_modifier') | int(-1) }}",
  "labeled_entities": "{{ label_entities('sync_with_lighting_modifier') }}"
}
```
File: [`automation/sensor/lighting_modifier/state.yaml`](entities/automation/sensor/lighting_modifier/state.yaml)
</details>

<details><summary><code>/sensor/storage-cc-ssd-transient-qbt-disk-used-percentage-notify-and-clear</code></summary>

**Entity ID: `automation.sensor_storage_cc_ssd_transient_qbt_disk_used_percentage_notify_and_clear`**

> Notify and clear notification for qBittorrent SSD storage usage thresholds

- Alias: /sensor/storage-cc-ssd-transient-qbt-disk-used-percentage-notify-and-clear
- ID: `sensor_storage_cc_ssd_transient_qbt_disk_used_percentage_notify_and_clear`
- Mode: `single`

File: [`automation/sensor/storage_cc_ssd_transient_qbt_disk_used_percentage_notify_and_clear.yaml`](entities/automation/sensor/storage_cc_ssd_transient_qbt_disk_used_percentage_notify_and_clear.yaml)
</details>

<details><summary><code>/sensor/vic-s-office-climate-sensor-temperature/sync-radiator-trv</code></summary>

**Entity ID: `automation.sensor_vic_s_office_climate_sensor_temperature_sync_radiator_trv`**

> Sync radiator TRV external temperature input when vic's office climate sensor temperature updates

- Alias: /sensor/vic-s-office-climate-sensor-temperature/sync-radiator-trv
- ID: `sensor_vic_s_office_climate_sensor_temperature_sync_radiator_trv`
- Mode: `single`

File: [`automation/sensor/vic_s_office_climate_sensor_temperature/sync_radiator_trv.yaml`](entities/automation/sensor/vic_s_office_climate_sensor_temperature/sync_radiator_trv.yaml)
</details>

<details><summary><code>/sensor/will-s-office-climate-sensor-temperature/sync-radiator-trv</code></summary>

**Entity ID: `automation.sensor_will_s_office_climate_sensor_temperature_sync_radiator_trv`**

> Sync radiator TRV external temperature input when office climate sensor temperature updates

- Alias: /sensor/will-s-office-climate-sensor-temperature/sync-radiator-trv
- ID: `sensor_will_s_office_climate_sensor_temperature_sync_radiator_trv`
- Mode: `single`

File: [`automation/sensor/will_s_office_climate_sensor_temperature/sync_radiator_trv.yaml`](entities/automation/sensor/will_s_office_climate_sensor_temperature/sync_radiator_trv.yaml)
</details>

<details><summary><code>/sensor/will-s-pixel-6-pro-weight/update</code></summary>

**Entity ID: `automation.sensor_will_s_pixel_6_pro_weight_update`**

> Submit weight entry to wger when weight sensor updates

- Alias: /sensor/will-s-pixel-6-pro-weight/update
- ID: `sensor_will_s_pixel_6_pro_weight_update`
- Mode: `single`
- Variables:

```json
{
  "today_date": "{{ today_at(0).strftime('%Y-%m-%d') }}",
  "weight": "{{ states('sensor.will_s_pixel_6_pro_weight') | float(0) | round(2) }}",
  "weigh_in_date": "{{\n  (\n    trigger.to_state.attributes.date | as_datetime(now() - timedelta(days=999))\n  ).date().isoformat()\n}}"
}
```
File: [`automation/sensor/will_s_pixel_6_pro_weight/update.yaml`](entities/automation/sensor/will_s_pixel_6_pro_weight/update.yaml)
</details>

<details><summary><code>/switch/air-freshener/timeout</code></summary>

**Entity ID: `automation.switch_air_freshener_timeout`**

> *No description provided*

- Alias: /switch/air-freshener/timeout
- ID: `switch_air_freshener_timeout`
- Mode: `single`

File: [`automation/switch/air_freshener/timeout.yaml`](entities/automation/switch/air_freshener/timeout.yaml)
</details>

<details><summary><code>/switch/air-freshener/turn-on</code></summary>

**Entity ID: `automation.switch_air_freshener_turn_on`**

> Turn the air freshener on when the AQI is high and the Air Purifier is on: if the purifier is off then it's because something that smells nice (e.g. diffuser, incense) is on, so the freshener isn't needed; if it's on, then assume the AQI is high because of e.g. cooking, so the freshener is needed

- Alias: /switch/air-freshener/turn-on
- ID: `switch_air_freshener_turn_on`
- Mode: `single`

File: [`automation/switch/air_freshener/turn_on.yaml`](entities/automation/switch/air_freshener/turn_on.yaml)
</details>

<details><summary><code>/switch/central-heating/off</code></summary>

**Entity ID: `automation.switch_central_heating_off`**

> Turn off all radiators when central heating is turned off

- Alias: /switch/central-heating/off
- ID: `switch_central_heating_off`
- Mode: `single`

File: [`automation/switch/central_heating/off.yaml`](entities/automation/switch/central_heating/off.yaml)
</details>

<details><summary><code>/switch/central-heating/on</code></summary>

**Entity ID: `automation.switch_central_heating_on`**

> Create persistent notification when central heating turns on

- Alias: /switch/central-heating/on
- ID: `switch_central_heating_on`
- Mode: `single`

File: [`automation/switch/central_heating/on.yaml`](entities/automation/switch/central_heating/on.yaml)
</details>

<details><summary><code>/switch/central-heating/vic-office-preheat</code></summary>

**Entity ID: `automation.switch_central_heating_vic_office_preheat`**

> Preheat Vic's office when central heating turns on during workday mornings, unless it's a holiday day. This does not turn the heating on, it's just to piggy-back off other automations if the heating is already on anyway.

- Alias: /switch/central-heating/vic-office-preheat
- ID: `switch_central_heating_vic_office_preheat`
- Mode: `single`

File: [`automation/switch/central_heating/vic_office_preheat.yaml`](entities/automation/switch/central_heating/vic_office_preheat.yaml)
</details>

<details><summary><code>/switch/charging-hub/turn-off</code></summary>

**Entity ID: `automation.switch_charging_hub_turn_off`**

> Turn off the charging hub when everything has finished charging

- Alias: /switch/charging-hub/turn-off
- ID: `switch_charging_hub_turn_off`
- Mode: `single`

File: [`automation/switch/charging_hub/turn_off.yaml`](entities/automation/switch/charging_hub/turn_off.yaml)
</details>

<details><summary><code>/switch/charging-hub/turn-on-daily</code></summary>

**Entity ID: `automation.switch_charging_hub_turn_on_daily`**

> Turn on the charging hub daily at 2 AM, and turn it off if power consumption remains below the threshold. This is mainly for when I plug something in to charge overnight and forget to turn it on

- Alias: /switch/charging-hub/turn-on-daily
- ID: `switch_charging_hub_turn_on_daily`
- Mode: `single`

File: [`automation/switch/charging_hub/turn_on_daily.yaml`](entities/automation/switch/charging_hub/turn_on_daily.yaml)
</details>

<details><summary><code>/switch/dry-box-dehumidifier/timeout</code></summary>

**Entity ID: `automation.switch_dry_box_dehumidifier_timeout`**

> *No description provided*

- Alias: /switch/dry-box-dehumidifier/timeout
- ID: `switch_dry_box_dehumidifier_timeout`
- Mode: `single`

File: [`automation/switch/dry_box_dehumidifier/timeout.yaml`](entities/automation/switch/dry_box_dehumidifier/timeout.yaml)
</details>

<details><summary><code>/switch/dry-box-dehumidifier/turn-on</code></summary>

**Entity ID: `automation.switch_dry_box_dehumidifier_turn_on`**

> Turn the dry box dehumidifier on when the humidity is above the threshold

- Alias: /switch/dry-box-dehumidifier/turn-on
- ID: `switch_dry_box_dehumidifier_turn_on`
- Mode: `single`

File: [`automation/switch/dry_box_dehumidifier/turn_on.yaml`](entities/automation/switch/dry_box_dehumidifier/turn_on.yaml)
</details>

<details><summary><code>/switch/hot-water/proximity/off</code></summary>

**Entity ID: `automation.switch_hot_water_proximity_off`**

> Turn off hot water when someone moves away from home beyond threshold distance

- Alias: /switch/hot-water/proximity/off
- ID: `switch_hot_water_proximity_off`
- Mode: `single`

File: [`automation/switch/hot_water/proximity/off.yaml`](entities/automation/switch/hot_water/proximity/off.yaml)
</details>

<details><summary><code>/switch/hot-water/proximity/on</code></summary>

**Entity ID: `automation.switch_hot_water_proximity_on`**

> Turn on hot water when someone is approaching home and schedule is active

- Alias: /switch/hot-water/proximity/on
- ID: `switch_hot_water_proximity_on`
- Mode: `single`

File: [`automation/switch/hot_water/proximity/on.yaml`](entities/automation/switch/hot_water/proximity/on.yaml)
</details>

<details><summary><code>/switch/lounge-christmas-tree/lounge-vacancy-timeout</code></summary>

**Entity ID: `automation.switch_lounge_christmas_tree_lounge_vacancy_timeout`**

> Turn off lounge Christmas tree when lounge has been empty for 2 hours

- Alias: /switch/lounge-christmas-tree/lounge-vacancy-timeout
- ID: `switch_lounge_christmas_tree_lounge_vacancy_timeout`
- Mode: `single`

File: [`automation/switch/lounge_christmas_tree/lounge_vacancy_timeout.yaml`](entities/automation/switch/lounge_christmas_tree/lounge_vacancy_timeout.yaml)
</details>

<details><summary><code>/switch/lounge-diffuser/state-change</code></summary>

**Entity ID: `automation.switch_lounge_diffuser_state_change`**

> Keep the diffuser's light in sync with the diffuser state

- Alias: /switch/lounge-diffuser/state-change
- ID: `switch_lounge_diffuser_state_change`
- Mode: `single`

File: [`automation/switch/lounge_diffuser/state_change.yaml`](entities/automation/switch/lounge_diffuser/state_change.yaml)
</details>

<details><summary><code>/switch/mtrxpi-power/off</code></summary>

**Entity ID: `automation.switch_mtrxpi_power_off`**

> *No description provided*

- Alias: /switch/mtrxpi-power/off
- ID: `switch_mtrxpi_power_off`
- Mode: `single`

File: [`automation/switch/mtrxpi_power/off.yaml`](entities/automation/switch/mtrxpi_power/off.yaml)
</details>

<details><summary><code>/switch/mtrxpi-power/on</code></summary>

**Entity ID: `automation.switch_mtrxpi_power_on`**

> *No description provided*

- Alias: /switch/mtrxpi-power/on
- ID: `switch_mtrxpi_power_on`
- Mode: `single`

File: [`automation/switch/mtrxpi_power/on.yaml`](entities/automation/switch/mtrxpi_power/on.yaml)
</details>

<details><summary><code>/switch/prusa-i3-mk3-power/off</code></summary>

**Entity ID: `automation.switch_prusa_i3_mk3_power_off`**

> *No description provided*

- Alias: /switch/prusa-i3-mk3-power/off
- ID: `switch_prusa_i3_mk3_power_off`
- Mode: `single`

File: [`automation/switch/prusa_i3_mk3_power/off.yaml`](entities/automation/switch/prusa_i3_mk3_power/off.yaml)
</details>

<details><summary><code>/switch/prusa-i3-mk3-power/timeout</code></summary>

**Entity ID: `automation.switch_prusa_i3_mk3_power_timeout`**

> *No description provided*

- Alias: /switch/prusa-i3-mk3-power/timeout
- ID: `switch_prusa_i3_mk3_power_timeout`
- Mode: `single`
- Variables:

```json
{
  "timeout_mins": "{{ states('input_number.prusa_i3_power_timeout') | int(15) }}",
  "last_change_bed": "{{ states.number.prusa_i3_target_bed_temperature.last_updated | default(utcnow()) }}",
  "last_change_hotend": "{{ states.number.prusa_i3_target_hotend_temperature.last_updated | default(utcnow()) }}",
  "change_threshold": "{{ now() - timedelta(minutes=timeout_mins) }}"
}
```
File: [`automation/switch/prusa_i3_mk3_power/timeout.yaml`](entities/automation/switch/prusa_i3_mk3_power/timeout.yaml)
</details>

<details><summary><code>/switch/vic-s-electric-blanket/hard-timeout</code></summary>

**Entity ID: `automation.switch_vic_s_electric_blanket_hard_timeout`**

> Hard timeout - turn off Vic's electric blanket after 8 hours

- Alias: /switch/vic-s-electric-blanket/hard-timeout
- ID: `switch_vic_s_electric_blanket_hard_timeout`
- Mode: `single`

File: [`automation/switch/vic_s_electric_blanket/hard_timeout.yaml`](entities/automation/switch/vic_s_electric_blanket/hard_timeout.yaml)
</details>

<details><summary><code>/switch/vic-s-electric-blanket/timeout</code></summary>

**Entity ID: `automation.switch_vic_s_electric_blanket_timeout`**

> Turn off Vic's electric blanket after timeout based on level

- Alias: /switch/vic-s-electric-blanket/timeout
- ID: `switch_vic_s_electric_blanket_timeout`
- Mode: `restart`
- Variables:

```json
{
  "level": "{{ states('sensor.vic_s_electric_blanket_level') | int(-1) }}"
}
```
File: [`automation/switch/vic_s_electric_blanket/timeout.yaml`](entities/automation/switch/vic_s_electric_blanket/timeout.yaml)
</details>

<details><summary><code>/switch/will-s-electric-blanket/hard-timeout</code></summary>

**Entity ID: `automation.switch_will_s_electric_blanket_hard_timeout`**

> Hard timeout - turn off Will's electric blanket after 8 hours

- Alias: /switch/will-s-electric-blanket/hard-timeout
- ID: `switch_will_s_electric_blanket_hard_timeout`
- Mode: `single`

File: [`automation/switch/will_s_electric_blanket/hard_timeout.yaml`](entities/automation/switch/will_s_electric_blanket/hard_timeout.yaml)
</details>

<details><summary><code>/switch/will-s-electric-blanket/timeout</code></summary>

**Entity ID: `automation.switch_will_s_electric_blanket_timeout`**

> Turn off Will's electric blanket after timeout based on level

- Alias: /switch/will-s-electric-blanket/timeout
- ID: `switch_will_s_electric_blanket_timeout`
- Mode: `restart`
- Variables:

```json
{
  "level": "{{ states('sensor.will_s_electric_blanket_level') | int(-1) }}"
}
```
File: [`automation/switch/will_s_electric_blanket/timeout.yaml`](entities/automation/switch/will_s_electric_blanket/timeout.yaml)
</details>

<details><summary><code>/tag/cosmo/basement</code></summary>

**Entity ID: `automation.tag_cosmo_basement`**

> *No description provided*

- Alias: /tag/cosmo/basement
- ID: `tag_cosmo_basement`
- Mode: `single`

File: [`automation/tag/cosmo/basement.yaml`](entities/automation/tag/cosmo/basement.yaml)
</details>

<details><summary><code>/tag/cosmo/first-floor</code></summary>

**Entity ID: `automation.tag_cosmo_first_floor`**

> *No description provided*

- Alias: /tag/cosmo/first-floor
- ID: `tag_cosmo_first_floor`
- Mode: `single`

File: [`automation/tag/cosmo/first_floor.yaml`](entities/automation/tag/cosmo/first_floor.yaml)
</details>

<details><summary><code>/tag/cosmo/ground-floor</code></summary>

**Entity ID: `automation.tag_cosmo_ground_floor`**

> *No description provided*

- Alias: /tag/cosmo/ground-floor
- ID: `tag_cosmo_ground_floor`
- Mode: `single`

File: [`automation/tag/cosmo/ground_floor.yaml`](entities/automation/tag/cosmo/ground_floor.yaml)
</details>

<details><summary><code>/var/vic-s-office-state-manager/attribute-timeout</code></summary>

**Entity ID: `automation.var_vic_s_office_state_manager_attribute_timeout`**

> Timeout for "should be" on/off attributes of Vic's desk state manager

- Alias: /var/vic-s-office-state-manager/attribute-timeout
- ID: `var_vic_s_office_state_manager_attribute_timeout`
- Mode: `single`

File: [`automation/var/vic_s_office_state_manager/attribute_timeout.yaml`](entities/automation/var/vic_s_office_state_manager/attribute_timeout.yaml)
</details>

<details><summary><code>/var/will-s-office-state-manager/attribute-timeout</code></summary>

**Entity ID: `automation.var_will_s_office_state_manager_attribute_timeout`**

> Timeout for "should be" on/off attributes of Will's desk state manager

- Alias: /var/will-s-office-state-manager/attribute-timeout
- ID: `var_will_s_office_state_manager_attribute_timeout`
- Mode: `single`

File: [`automation/var/will_s_office_state_manager/attribute_timeout.yaml`](entities/automation/var/will_s_office_state_manager/attribute_timeout.yaml)
</details>

<details><summary><code>/webhook/get-latest-appdaemon-release</code></summary>

**Entity ID: `automation.webhook_get_latest_appdaemon_release`**

> *No description provided*

- Alias: /webhook/get-latest-appdaemon-release
- ID: `webhook_get_latest_appdaemon_release`
- Mode: `queued`

File: [`automation/webhook/get_latest_appdaemon_release.yaml`](entities/automation/webhook/get_latest_appdaemon_release.yaml)
</details>

<details><summary><code>/webhook/git-branch-or-tag-created</code></summary>

**Entity ID: `automation.webhook_git_branch_or_tag_created`**

> *No description provided*

- Alias: /webhook/git-branch-or-tag-created
- ID: `webhook_git_branch_or_tag_created`
- Mode: `queued`
- Variables:

```json
{
  "img_url": "{{ trigger.json[\"sender\"][\"avatar_url\"] }}",
  "repository": "{{ trigger.json[\"repository\"][\"name\"] }}",
  "ref": "{{ trigger.json[\"ref\"] }}",
  "ref_type": "{{ trigger.json[\"ref_type\"] }}",
  "repo_url": "{{ trigger.json[\"repository\"][\"html_url\"] }}"
}
```
File: [`automation/webhook/git_branch_or_tag_created.yaml`](entities/automation/webhook/git_branch_or_tag_created.yaml)
</details>

<details><summary><code>/webhook/git-branch-or-tag-deleted</code></summary>

**Entity ID: `automation.webhook_git_branch_or_tag_deleted`**

> *No description provided*

- Alias: /webhook/git-branch-or-tag-deleted
- ID: `webhook_git_branch_or_tag_deleted`
- Mode: `queued`
- Variables:

```json
{
  "img_url": "{{ trigger.json[\"sender\"][\"avatar_url\"] }}",
  "repository": "{{ trigger.json[\"repository\"][\"name\"] }}",
  "ref": "{{ trigger.json[\"ref\"] }}",
  "ref_type": "{{ trigger.json[\"ref_type\"] }}"
}
```
File: [`automation/webhook/git_branch_or_tag_deleted.yaml`](entities/automation/webhook/git_branch_or_tag_deleted.yaml)
</details>

<details><summary><code>/webhook/update-pull-request-sensor</code></summary>

**Entity ID: `automation.webhook_update_pull_request_sensor`**

> *No description provided*

- Alias: /webhook/update-pull-request-sensor
- ID: `webhook_update_pull_request_sensor`
- Mode: `queued`

File: [`automation/webhook/update_pull_request_sensor.yaml`](entities/automation/webhook/update_pull_request_sensor.yaml)
</details>

</details>

## Command Line

<details><summary><h3>Entities (26)</h3></summary>

<details><summary><strong>AppDaemon Status</strong></summary>

**Entity ID: `sensor.appdaemon_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/a0d7b954_appdaemon/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/appdaemon_status.yaml`](entities/command_line/sensor/addons/appdaemon_status.yaml)
</details>

<details><summary><strong>CastSponsorSkip Status</strong></summary>

**Entity ID: `sensor.castsponsorskip_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/db21ed7f_sponsorblockcast/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/castsponsorskip_status.yaml`](entities/command_line/sensor/addons/castsponsorskip_status.yaml)
</details>

<details><summary><strong>ESPHome Add-on Status</strong></summary>

**Entity ID: `sensor.esphome_add_on_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/5c53de3b_esphome/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/esphome_add_on_status.yaml`](entities/command_line/sensor/addons/esphome_add_on_status.yaml)
</details>

<details><summary><strong>Item Warehouse API Status</strong></summary>

**Entity ID: `sensor.item_warehouse_api_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/431930c3_item_warehouse_api/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/item_warehouse_api.yaml`](entities/command_line/sensor/addons/item_warehouse_api.yaml)
</details>

<details><summary><strong>Item Warehouse Website Status</strong></summary>

**Entity ID: `sensor.item_warehouse_website_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/86912a13_item_warehouse_website/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/item_warehouse_website.yaml`](entities/command_line/sensor/addons/item_warehouse_website.yaml)
</details>

<details><summary><strong>Terminal & SSH Add-on Status</strong></summary>

**Entity ID: `sensor.terminal_ssh_add_on_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/core_ssh/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/terminal_ssh_add_on_status.yaml`](entities/command_line/sensor/addons/terminal_ssh_add_on_status.yaml)
</details>

<details><summary><strong>Visual Studio Code Add-on Status</strong></summary>

**Entity ID: `sensor.visual_studio_code_add_on_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/a0d7b954_vscode/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/visual_studio_code_add_on_status.yaml`](entities/command_line/sensor/addons/visual_studio_code_add_on_status.yaml)
</details>

<details><summary><strong>YAS-209 Bridge Status</strong></summary>

**Entity ID: `sensor.yas_209_bridge_status`**

- Command: `curl -sSL -H "Authorization: Bearer abc123" http://supervisor/addons/2c04ba34_yas_209_bridge/stats`
- Scan Interval: 60

File: [`command_line/sensor/addons/yas_209_bridge_status.yaml`](entities/command_line/sensor/addons/yas_209_bridge_status.yaml)
</details>

<details><summary><strong>Current GH CLI User</strong></summary>

**Entity ID: `sensor.current_gh_cli_user`**

- Command: `/config/resources/gh_cli/bin/gh api user -q .login`
- Scan Interval: 120

File: [`command_line/sensor/current_gh_cli_user.yaml`](entities/command_line/sensor/current_gh_cli_user.yaml)
</details>

<details><summary><strong>Current Git Branch</strong></summary>

**Entity ID: `sensor.current_git_branch`**

- Command: `cd /config && git rev-parse --abbrev-ref HEAD`
- Scan Interval: 120

File: [`command_line/sensor/current_git_branch.yaml`](entities/command_line/sensor/current_git_branch.yaml)
</details>

<details><summary><strong>Current Git Ref</strong></summary>

**Entity ID: `sensor.current_git_ref`**

- Command: `cd /config && git describe --tags --exact-match 2>/dev/null || git rev-parse --short HEAD`
- Scan Interval: 120

File: [`command_line/sensor/current_git_ref.yaml`](entities/command_line/sensor/current_git_ref.yaml)
</details>

<details><summary><strong>Add-on: Item Warehouse Pull Requests</strong></summary>

**Entity ID: `sensor.add_on_item_warehouse_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh addon-item-warehouse`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/add_on_item_warehouse.yaml`](entities/command_line/sensor/github_pull_requests/add_on_item_warehouse.yaml)
</details>

<details><summary><strong>Add-on: RSS Log Feed Pull Requests</strong></summary>

**Entity ID: `sensor.add_on_rss_log_feed_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh addon-rss-log-feed`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/add_on_rss_log_feed_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/add_on_rss_log_feed_pull_requests.yaml)
</details>

<details><summary><strong>Add-on: YAS-209 Bridge Pull Requests</strong></summary>

**Entity ID: `sensor.add_on_yas_209_bridge_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh addon-yas-209-bridge`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/add_on_yas_209_bridge_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/add_on_yas_209_bridge_pull_requests.yaml)
</details>

<details><summary><strong>GitHub Config Files Pull Requests</strong></summary>

**Entity ID: `sensor.github_config_files_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh github-config-files`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/github_config_files_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/github_config_files_pull_requests.yaml)
</details>

<details><summary><strong>Home Assistant Config Validator Pull Requests</strong></summary>

**Entity ID: `sensor.home_assistant_config_validator_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh home-assistant-config-validator`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/home_assistant_config_validator_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/home_assistant_config_validator_pull_requests.yaml)
</details>

<details><summary><strong>Home Assistant Pull Requests</strong></summary>

**Entity ID: `sensor.home_assistant_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh home-assistant`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/home_assistant_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/home_assistant_pull_requests.yaml)
</details>

<details><summary><strong>LED Matrix Now Playing Pull Requests</strong></summary>

**Entity ID: `sensor.led_matrix_now_playing_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh led-matrix-now-playing`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/led_matrix_now_playing_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/led_matrix_now_playing_pull_requests.yaml)
</details>

<details><summary><strong>Plant Monitor Pull Requests</strong></summary>

**Entity ID: `sensor.plant_monitor_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh plant-monitor`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/plant_monitor_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/plant_monitor_pull_requests.yaml)
</details>

<details><summary><strong>Python Template Pull Requests</strong></summary>

**Entity ID: `sensor.python_template_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh python-template`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/python_template_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/python_template_pull_requests.yaml)
</details>

<details><summary><strong>Smart Mini CRT Interface Pull Requests</strong></summary>

**Entity ID: `sensor.smart_mini_crt_interface_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh smart-mini-crt-interface`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/smart_mini_crt_interface_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/smart_mini_crt_interface_pull_requests.yaml)
</details>

<details><summary><strong>Very Slow Movie Player Pull Requests</strong></summary>

**Entity ID: `sensor.very_slow_movie_player_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh very-slow-movie-player`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/very_slow_movie_player_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/very_slow_movie_player_pull_requests.yaml)
</details>

<details><summary><strong>WG Scripts Pull Requests</strong></summary>

**Entity ID: `sensor.wg_scripts_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh wg-scripts`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/wg_scripts_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/wg_scripts_pull_requests.yaml)
</details>

<details><summary><strong>WG Utilities Pull Requests</strong></summary>

**Entity ID: `sensor.wg_utilities_pull_requests`**

- Command: `sh /config/resources/shell_command/gh_cli/get_pull_requests.sh wg-utilities`
- Scan Interval: 3600

File: [`command_line/sensor/github_pull_requests/wg_utilities_pull_requests.yaml`](entities/command_line/sensor/github_pull_requests/wg_utilities_pull_requests.yaml)
</details>

<details><summary><strong>Companion Cube | CPU Temperature</strong></summary>

**Entity ID: `sensor.companion_cube_cpu_temperature`**

- Command: `ssh -i /config/.ssh/pve root@192.168.68.199 -o StrictHostKeyChecking=no sensors | grep 'Package id 0:' | awk '{print $4}' | tr -d '+°C'`
- Scan Interval: 60

File: [`command_line/sensor/pve/companion_cube_cpu_temperature.yaml`](entities/command_line/sensor/pve/companion_cube_cpu_temperature.yaml)
</details>

<details><summary><strong>Remote Git Branches</strong></summary>

**Entity ID: `sensor.remote_git_branches`**

- Command: `cd /config && git ls-remote --heads https://github.com/worgarside/home-assistant | awk '{print $2}' | sed 's/refs\/heads\///' | jq -R -s -c '{"branches": (split("\n")[:-1])}'`
- Scan Interval: 1800

File: [`command_line/sensor/remote_git_branches.yaml`](entities/command_line/sensor/remote_git_branches.yaml)
</details>

</details>

## Cover

<details><summary><h3>Entities (1)</h3></summary>

<details><summary><strong>Office Desk</strong></summary>

**Entity ID: `cover.office_desk`**

File: [`cover/office/office_desk.yaml`](entities/cover/office/office_desk.yaml)
</details>

</details>

## Device Tracker

<details><summary><h3>Entities (2)</h3></summary>

<details><summary><code>device_tracker.primary_gmail_address</code></summary>

- Platform: `google_maps`

File: [`device_tracker/google_maps/primary_gmail_address.yaml`](entities/device_tracker/google_maps/primary_gmail_address.yaml)
</details>

<details><summary><code>device_tracker.openwrt_vm</code></summary>

- Platform: `luci`

File: [`device_tracker/luci/openwrt_vm.yaml`](entities/device_tracker/luci/openwrt_vm.yaml)
</details>

</details>

## Input Boolean

<details><summary><h3>Entities (30)</h3></summary>

<details><summary><strong>Air Purifier | Quiet Mode</strong></summary>

**Entity ID: `input_boolean.air_purifier_quiet_mode`**

- Icon: [`mdi:air-purifier`](https://pictogrammers.com/library/mdi/icon/air-purifier/)

File: [`input_boolean/air_purifier/air_purifier_quiet_mode.yaml`](entities/input_boolean/air_purifier/air_purifier_quiet_mode.yaml)
</details>

<details><summary><strong>Apollo OTA Mode</strong></summary>

**Entity ID: `input_boolean.apollo_ota_mode`**

- Icon: [`mdi:sleep-off`](https://pictogrammers.com/library/mdi/icon/sleep-off/)

File: [`input_boolean/apollo_ota_mode.yaml`](entities/input_boolean/apollo_ota_mode.yaml)
</details>

<details><summary><strong>AD: Monzo Auto-Save</strong></summary>

**Entity ID: `input_boolean.ad_monzo_auto_save`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_boolean/appdaemon_trigger/ad_monzo_auto_save.yaml`](entities/input_boolean/appdaemon_trigger/ad_monzo_auto_save.yaml)
</details>

<details><summary><strong>Auto-Reload | Automation</strong></summary>

**Entity ID: `input_boolean.auto_reload_automation`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_automation.yaml`](entities/input_boolean/auto_reload/auto_reload_automation.yaml)
</details>

<details><summary><strong>Auto-Reload | Command Line</strong></summary>

**Entity ID: `input_boolean.auto_reload_command_line`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_command_line.yaml`](entities/input_boolean/auto_reload/auto_reload_command_line.yaml)
</details>

<details><summary><strong>Auto-Reload | Conversation</strong></summary>

**Entity ID: `input_boolean.auto_reload_conversation`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_conversation.yaml`](entities/input_boolean/auto_reload/auto_reload_conversation.yaml)
</details>

<details><summary><strong>Auto-Reload | Group</strong></summary>

**Entity ID: `input_boolean.auto_reload_group`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_group.yaml`](entities/input_boolean/auto_reload/auto_reload_group.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Boolean</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_boolean`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_boolean.yaml`](entities/input_boolean/auto_reload/auto_reload_input_boolean.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Button</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_button`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_button.yaml`](entities/input_boolean/auto_reload/auto_reload_input_button.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Datetime</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_datetime`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_datetime.yaml`](entities/input_boolean/auto_reload/auto_reload_input_datetime.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Number</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_number`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_number.yaml`](entities/input_boolean/auto_reload/auto_reload_input_number.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Select</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_select`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_select.yaml`](entities/input_boolean/auto_reload/auto_reload_input_select.yaml)
</details>

<details><summary><strong>Auto-Reload | Input Text</strong></summary>

**Entity ID: `input_boolean.auto_reload_input_text`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_input_text.yaml`](entities/input_boolean/auto_reload/auto_reload_input_text.yaml)
</details>

<details><summary><strong>Auto-Reload | MQTT</strong></summary>

**Entity ID: `input_boolean.auto_reload_mqtt`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_mqtt.yaml`](entities/input_boolean/auto_reload/auto_reload_mqtt.yaml)
</details>

<details><summary><strong>Auto-Reload | REST</strong></summary>

**Entity ID: `input_boolean.auto_reload_rest`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_rest.yaml`](entities/input_boolean/auto_reload/auto_reload_rest.yaml)
</details>

<details><summary><strong>Auto-Reload | REST Command</strong></summary>

**Entity ID: `input_boolean.auto_reload_rest_command`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_rest_command.yaml`](entities/input_boolean/auto_reload/auto_reload_rest_command.yaml)
</details>

<details><summary><strong>Auto-Reload | Scene</strong></summary>

**Entity ID: `input_boolean.auto_reload_scene`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_scene.yaml`](entities/input_boolean/auto_reload/auto_reload_scene.yaml)
</details>

<details><summary><strong>Auto-Reload | Schedule</strong></summary>

**Entity ID: `input_boolean.auto_reload_schedule`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_schedule.yaml`](entities/input_boolean/auto_reload/auto_reload_schedule.yaml)
</details>

<details><summary><strong>Auto-Reload | Script</strong></summary>

**Entity ID: `input_boolean.auto_reload_script`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_script.yaml`](entities/input_boolean/auto_reload/auto_reload_script.yaml)
</details>

<details><summary><strong>Auto-Reload | Template</strong></summary>

**Entity ID: `input_boolean.auto_reload_template`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_template.yaml`](entities/input_boolean/auto_reload/auto_reload_template.yaml)
</details>

<details><summary><strong>Auto-Reload | Timer</strong></summary>

**Entity ID: `input_boolean.auto_reload_timer`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_timer.yaml`](entities/input_boolean/auto_reload/auto_reload_timer.yaml)
</details>

<details><summary><strong>Auto-Reload | Universal</strong></summary>

**Entity ID: `input_boolean.auto_reload_universal`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_universal.yaml`](entities/input_boolean/auto_reload/auto_reload_universal.yaml)
</details>

<details><summary><strong>Auto-Reload | Var</strong></summary>

**Entity ID: `input_boolean.auto_reload_var`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_var.yaml`](entities/input_boolean/auto_reload/auto_reload_var.yaml)
</details>

<details><summary><strong>Auto-Reload | Zone</strong></summary>

**Entity ID: `input_boolean.auto_reload_zone`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)

File: [`input_boolean/auto_reload/auto_reload_zone.yaml`](entities/input_boolean/auto_reload/auto_reload_zone.yaml)
</details>

<details><summary><strong>Debug with Persistent Notifications</strong></summary>

**Entity ID: `input_boolean.debug_with_persistent_notifications`**

- Icon: [`mdi:message-badge-outline`](https://pictogrammers.com/library/mdi/icon/message-badge-outline/)

File: [`input_boolean/debug_with_persistent_notifications.yaml`](entities/input_boolean/debug_with_persistent_notifications.yaml)
</details>

<details><summary><strong>Lounge | Lights: Exercise Mode</strong></summary>

**Entity ID: `input_boolean.lounge_lights_exercise_mode`**

- Icon: [`mdi:dumbbell`](https://pictogrammers.com/library/mdi/icon/dumbbell/)

File: [`input_boolean/lounge_lights_exercise_mode.yaml`](entities/input_boolean/lounge_lights_exercise_mode.yaml)
</details>

<details><summary><strong>Mini CRT Fan</strong></summary>

**Entity ID: `input_boolean.mini_crt_fan`**

- Icon: [`mdi:fan`](https://pictogrammers.com/library/mdi/icon/fan/)

File: [`input_boolean/mini_crt_fan.yaml`](entities/input_boolean/mini_crt_fan.yaml)
</details>

<details><summary><strong>Mini CRT Power</strong></summary>

**Entity ID: `input_boolean.mini_crt_power`**

- Icon: [`mdi:television-classic`](https://pictogrammers.com/library/mdi/icon/television-classic/)

File: [`input_boolean/mini_crt_power.yaml`](entities/input_boolean/mini_crt_power.yaml)
</details>

<details><summary><strong>Topaz SR10: Is Volume Muted</strong></summary>

**Entity ID: `input_boolean.topaz_sr10_is_volume_muted`**

- Icon: [`mdi:volume-off`](https://pictogrammers.com/library/mdi/icon/volume-off/)

File: [`input_boolean/topaz_sr10/topaz_sr10_is_volume_muted.yaml`](entities/input_boolean/topaz_sr10/topaz_sr10_is_volume_muted.yaml)
</details>

<details><summary><strong>Turn Off Bedroom Fan for Scheduled Heating</strong></summary>

**Entity ID: `input_boolean.turn_off_bedroom_fan_for_scheduled_heating`**

- Icon: [`mdi:fan-off`](https://pictogrammers.com/library/mdi/icon/fan-off/)

File: [`input_boolean/turn_off_bedroom_fan_for_scheduled_heating.yaml`](entities/input_boolean/turn_off_bedroom_fan_for_scheduled_heating.yaml)
</details>

</details>

## Input Datetime

<details><summary><h3>Entities (5)</h3></summary>

<details><summary><strong>Cosmo Nightly Kitchen Clean Time</strong></summary>

**Entity ID: `input_datetime.cosmo_nightly_kitchen_clean_time`**

- Has Time: `true`
- Icon: [`mdi:weather-night`](https://pictogrammers.com/library/mdi/icon/weather-night/)

File: [`input_datetime/cosmo_nightly_kitchen_clean_time.yaml`](entities/input_datetime/cosmo_nightly_kitchen_clean_time.yaml)
</details>

<details><summary><strong>Home Assistant Start Time</strong></summary>

**Entity ID: `input_datetime.home_assistant_start_time`**

- Has Date: `true`
- Has Time: `true`
- Icon: [`mdi:power`](https://pictogrammers.com/library/mdi/icon/power/)

File: [`input_datetime/home_assistant_start_time.yaml`](entities/input_datetime/home_assistant_start_time.yaml)
</details>

<details><summary><strong>Last Auto-Save</strong></summary>

**Entity ID: `input_datetime.last_auto_save`**

- Has Date: `true`
- Has Time: `true`
- Icon: [`mdi:bank-transfer`](https://pictogrammers.com/library/mdi/icon/bank-transfer/)

File: [`input_datetime/last_auto_save.yaml`](entities/input_datetime/last_auto_save.yaml)
</details>

<details><summary><strong>Next Bedroom Sunrise</strong></summary>

**Entity ID: `input_datetime.next_bedroom_sunrise`**

- Has Date: `true`
- Has Time: `true`
- Icon: [`mdi:weather-sunset-up`](https://pictogrammers.com/library/mdi/icon/weather-sunset-up/)

File: [`input_datetime/next_bedroom_sunrise.yaml`](entities/input_datetime/next_bedroom_sunrise.yaml)
</details>

<details><summary><strong>Rain Flash Cooldown</strong></summary>

**Entity ID: `input_datetime.rain_flash_cooldown`**

- Has Date: `true`
- Has Time: `true`
- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)

File: [`input_datetime/rain_flash_cooldown.yaml`](entities/input_datetime/rain_flash_cooldown.yaml)
</details>

</details>

## Input Number

<details><summary><h3>Entities (59)</h3></summary>

<details><summary><strong>Auto-Save Debit Transaction Percentage</strong></summary>

**Entity ID: `input_number.auto_save_debit_transaction_percentage`**

- Icon: [`mdi:sack-percent`](https://pictogrammers.com/library/mdi/icon/sack-percent/)
- Max: 100
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/auto_save_debit_transaction_percentage.yaml`](entities/input_number/auto_save_debit_transaction_percentage.yaml)
</details>

<details><summary><strong>Auto-Save Minimum</strong></summary>

**Entity ID: `input_number.auto_save_minimum`**

- Icon: [`mdi:arrow-collapse-down`](https://pictogrammers.com/library/mdi/icon/arrow-collapse-down/)
- Max: 1000
- Mode: `box`
- Unit Of Measurement: GBP

File: [`input_number/auto_save_minimum.yaml`](entities/input_number/auto_save_minimum.yaml)
</details>

<details><summary><strong>Auto-Save Naughty Transaction Percentage</strong></summary>

**Entity ID: `input_number.auto_save_naughty_transaction_percentage`**

- Icon: [`mdi:sack-percent`](https://pictogrammers.com/library/mdi/icon/sack-percent/)
- Max: 100
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/auto_save_naughty_transaction_percentage.yaml`](entities/input_number/auto_save_naughty_transaction_percentage.yaml)
</details>

<details><summary><strong>Bedroom Sunrise Duration</strong></summary>

**Entity ID: `input_number.bedroom_sunrise_duration`**

- Max: 120
- Min: 5
- Mode: `slider`
- Unit Of Measurement: `min`

File: [`input_number/bedroom_sunrise_duration.yaml`](entities/input_number/bedroom_sunrise_duration.yaml)
</details>

<details><summary><strong>Bedroom Sunrise Max Brightness</strong></summary>

**Entity ID: `input_number.bedroom_sunrise_max_brightness`**

- Max: 100
- Min: 1
- Mode: `slider`
- Unit Of Measurement: %

File: [`input_number/bedroom_sunrise_max_brightness.yaml`](entities/input_number/bedroom_sunrise_max_brightness.yaml)
</details>

<details><summary><strong>Credit Card Pot Top-Up | Maximum Auto Top-Up</strong></summary>

**Entity ID: `input_number.credit_card_pot_top_up_maximum_auto_top_up`**

- Icon: [`mdi:bank-transfer`](https://pictogrammers.com/library/mdi/icon/bank-transfer/)
- Max: 10000
- Mode: `box`
- Unit Of Measurement: GBP

File: [`input_number/cc_pot_top_up/credit_card_pot_top_up_maximum_auto_top_up.yaml`](entities/input_number/cc_pot_top_up/credit_card_pot_top_up_maximum_auto_top_up.yaml)
</details>

<details><summary><strong>Credit Card Pot Top-Up | Minimum Remainder</strong></summary>

**Entity ID: `input_number.credit_card_pot_top_up_minimum_remainder`**

- Icon: [`mdi:download-multiple`](https://pictogrammers.com/library/mdi/icon/download-multiple/)
- Max: 10000
- Mode: `box`
- Unit Of Measurement: GBP

File: [`input_number/cc_pot_top_up/credit_card_pot_top_up_minimum_remainder.yaml`](entities/input_number/cc_pot_top_up/credit_card_pot_top_up_minimum_remainder.yaml)
</details>

<details><summary><strong>Dry Box | Max Humidity</strong></summary>

**Entity ID: `input_number.dry_box_max_humidity`**

- Max: 100
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/dry_box/dry_box_max_humidity.yaml`](entities/input_number/dry_box/dry_box_max_humidity.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 1</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_1`**

- Icon: [`mdi:timer-outline`](https://pictogrammers.com/library/mdi/icon/timer-outline/)
- Max: 480
- Min: 1
- Mode: `box`
- Unit Of Measurement: `min`

File: [`input_number/electric_blanket_timeout_level_1.yaml`](entities/input_number/electric_blanket_timeout_level_1.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 2</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_2`**

- Icon: [`mdi:timer-outline`](https://pictogrammers.com/library/mdi/icon/timer-outline/)
- Max: 480
- Min: 1
- Mode: `slider`
- Unit Of Measurement: `min`

File: [`input_number/electric_blanket_timeout_level_2.yaml`](entities/input_number/electric_blanket_timeout_level_2.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 3</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_3`**

- Icon: [`mdi:timer-outline`](https://pictogrammers.com/library/mdi/icon/timer-outline/)
- Max: 480
- Min: 1
- Mode: `slider`
- Unit Of Measurement: `min`

File: [`input_number/electric_blanket_timeout_level_3.yaml`](entities/input_number/electric_blanket_timeout_level_3.yaml)
</details>

<details><summary><strong>Hot Water | Proximity Distance</strong></summary>

**Entity ID: `input_number.hot_water_proximity_distance`**

- Icon: [`mdi:map-marker-distance`](https://pictogrammers.com/library/mdi/icon/map-marker-distance/)
- Max: 10
- Min: 0.5
- Mode: `box`
- Unit Of Measurement: `mi`

File: [`input_number/hot_water_proximity_distance.yaml`](entities/input_number/hot_water_proximity_distance.yaml)
</details>

<details><summary><strong>Lighting Modifier | Maximum</strong></summary>

**Entity ID: `input_number.lighting_modifier_maximum`**

- Max: 100
- Min: 1
- Mode: `slider`
- Unit Of Measurement: %

File: [`input_number/lighting_modifier_maximum.yaml`](entities/input_number/lighting_modifier_maximum.yaml)
</details>

<details><summary><strong>Lighting Modifier | Minimum</strong></summary>

**Entity ID: `input_number.lighting_modifier_minimum`**

- Max: 100
- Min: 1
- Mode: `slider`
- Unit Of Measurement: %

File: [`input_number/lighting_modifier_minimum.yaml`](entities/input_number/lighting_modifier_minimum.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Maximum Rain Intensity</strong></summary>

**Entity ID: `input_number.mtrxpi_raining_grid_maximum_rain_intensity`**

- Icon: [`mdi:weather-pouring`](https://pictogrammers.com/library/mdi/icon/weather-pouring/)
- Max: 1000
- Min: 10
- Mode: `box`
- Unit Of Measurement: mm/hr

File: [`input_number/mtrxpi/mtrxpi_raining_grid_maximum_rain_intensity.yaml`](entities/input_number/mtrxpi/mtrxpi_raining_grid_maximum_rain_intensity.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_audio_visualiser_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_audio_visualiser_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_audio_visualiser_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Clock: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_clock_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_clock_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_clock_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | GIF (Alert Bell): Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_gif_alert_bell_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_gif_alert_bell_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_gif_alert_bell_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | GIF (Door Animated): Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_gif_door_animated_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_gif_door_animated_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_gif_door_animated_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Image (Door Closed): Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_image_door_closed_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_image_door_closed_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_image_door_closed_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Now Playing: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_now_playing_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_now_playing_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_now_playing_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_raining_grid_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_raining_grid_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_raining_grid_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_snake_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_snake_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_snake_queue_position.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Queue Position</strong></summary>

**Entity ID: `input_number.mtrxpi_sorter_queue_position`**

- Icon: [`mdi:tray-plus`](https://pictogrammers.com/library/mdi/icon/tray-plus/)
- Max: 10000
- Min: -10000
- Mode: `box`
- Unit Of Measurement:

File: [`input_number/mtrxpi/queue_position/mtrxpi_sorter_queue_position.yaml`](entities/input_number/mtrxpi/queue_position/mtrxpi_sorter_queue_position.yaml)
</details>

<details><summary><strong>Nightly Kitchen Clean Suction Level</strong></summary>

**Entity ID: `input_number.nightly_kitchen_clean_suction_level`**

- Icon: [`mdi:robot-vacuum`](https://pictogrammers.com/library/mdi/icon/robot-vacuum/)
- Max: 3
- Mode: `slider`
- Unit Of Measurement: `level`

File: [`input_number/nightly_kitchen_clean_suction_level.yaml`](entities/input_number/nightly_kitchen_clean_suction_level.yaml)
</details>

<details><summary><strong>Office Desk Sitting Height</strong></summary>

**Entity ID: `input_number.office_desk_sitting_height`**

- Icon: [`mdi:arrow-collapse-down`](https://pictogrammers.com/library/mdi/icon/arrow-collapse-down/)
- Max: 100
- Min: 10
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/office_desk_sitting_height.yaml`](entities/input_number/office_desk_sitting_height.yaml)
</details>

<details><summary><strong>Office Desk Standing Height</strong></summary>

**Entity ID: `input_number.office_desk_standing_height`**

- Icon: [`mdi:arrow-collapse-up`](https://pictogrammers.com/library/mdi/icon/arrow-collapse-up/)
- Max: 100
- Min: 10
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/office_desk_standing_height.yaml`](entities/input_number/office_desk_standing_height.yaml)
</details>

<details><summary><strong>Office Desk Standing Mode Percentage Target</strong></summary>

**Entity ID: `input_number.office_desk_standing_mode_percentage_target`**

- Icon: [`mdi:bullseye-arrow`](https://pictogrammers.com/library/mdi/icon/bullseye-arrow/)
- Max: 100
- Mode: `box`
- Unit Of Measurement: %

File: [`input_number/office_desk_standing_mode_percentage_target.yaml`](entities/input_number/office_desk_standing_mode_percentage_target.yaml)
</details>

<details><summary><strong>Charging Hub: Auto-Off Threshold</strong></summary>

**Entity ID: `input_number.charging_hub_auto_off_threshold`**

- Max: 100
- Min: 1
- Mode: `box`
- Unit Of Measurement: W

File: [`input_number/threshold/charging_hub/charging_hub_auto_off_threshold.yaml`](entities/input_number/threshold/charging_hub/charging_hub_auto_off_threshold.yaml)
</details>

<details><summary><strong>CRTPi: Fan Auto-On Threshold</strong></summary>

**Entity ID: `input_number.crtpi_fan_auto_on_threshold`**

- Max: 100
- Min: 20
- Mode: `box`
- Unit Of Measurement: °C

File: [`input_number/threshold/crtpi_fan/crtpi_fan_auto_on_threshold.yaml`](entities/input_number/threshold/crtpi_fan/crtpi_fan_auto_on_threshold.yaml)
</details>

<details><summary><strong>Kitchen Extractor Vent: PM2.5 Threshold</strong></summary>

**Entity ID: `input_number.kitchen_extractor_vent_pm2_5_threshold`**

- Max: 998
- Min: 1
- Mode: `box`
- Unit Of Measurement: µg/m³

File: [`input_number/threshold/kitchen_extractor_vent/kitchen_extractor_vent_pm2_5_threshold.yaml`](entities/input_number/threshold/kitchen_extractor_vent/kitchen_extractor_vent_pm2_5_threshold.yaml)
</details>

<details><summary><strong>Kitchen Extractor Vent: VOC Index Threshold</strong></summary>

**Entity ID: `input_number.kitchen_extractor_vent_voc_index_threshold`**

- Max: 998
- Min: 1
- Mode: `box`

File: [`input_number/threshold/kitchen_extractor_vent/kitchen_extractor_vent_voc_index_threshold.yaml`](entities/input_number/threshold/kitchen_extractor_vent/kitchen_extractor_vent_voc_index_threshold.yaml)
</details>

<details><summary><strong>OctoPi Fan Auto-On Threshold</strong></summary>

**Entity ID: `input_number.octopi_fan_auto_on_threshold`**

- Max: 100
- Min: 20
- Mode: `box`
- Unit Of Measurement: °C

File: [`input_number/threshold/octopi_fan/octopi_fan_auto_on_threshold.yaml`](entities/input_number/threshold/octopi_fan/octopi_fan_auto_on_threshold.yaml)
</details>

<details><summary><strong>Vic's Office Fan: PM2.5 Threshold</strong></summary>

**Entity ID: `input_number.vic_s_office_fan_pm2_5_threshold`**

- Max: 1000
- Min: 25
- Mode: `box`
- Unit Of Measurement: µg/m³

File: [`input_number/threshold/vic_s_office_fan/vic_s_office_fan_pm2_5_threshold.yaml`](entities/input_number/threshold/vic_s_office_fan/vic_s_office_fan_pm2_5_threshold.yaml)
</details>

<details><summary><strong>Vic's Office | Fan: Purifier Speed</strong></summary>

**Entity ID: `input_number.vic_s_office_fan_purifier_speed`**

- Max: 100
- Min: 10
- Mode: `slider`
- Unit Of Measurement: %

File: [`input_number/threshold/vic_s_office_fan/vic_s_office_fan_purifier_speed.yaml`](entities/input_number/threshold/vic_s_office_fan/vic_s_office_fan_purifier_speed.yaml)
</details>

<details><summary><strong>Vic's Office Fan: VOC Index Threshold</strong></summary>

**Entity ID: `input_number.vic_s_office_fan_voc_index_threshold`**

- Max: 10
- Min: 0.5
- Mode: `box`

File: [`input_number/threshold/vic_s_office_fan/vic_s_office_fan_voc_index_threshold.yaml`](entities/input_number/threshold/vic_s_office_fan/vic_s_office_fan_voc_index_threshold.yaml)
</details>

<details><summary><strong>Will's Office Fan: PM2.5 Threshold</strong></summary>

**Entity ID: `input_number.will_s_office_fan_pm2_5_threshold`**

- Max: 1000
- Min: 25
- Mode: `box`
- Unit Of Measurement: µg/m³

File: [`input_number/threshold/will_s_office_fan/will_s_office_fan_pm2_5_threshold.yaml`](entities/input_number/threshold/will_s_office_fan/will_s_office_fan_pm2_5_threshold.yaml)
</details>

<details><summary><strong>Will's Office | Fan: Purifier Speed</strong></summary>

**Entity ID: `input_number.will_s_office_fan_purifier_speed`**

- Max: 100
- Min: 10
- Mode: `slider`
- Unit Of Measurement: %

File: [`input_number/threshold/will_s_office_fan/will_s_office_fan_purifier_speed.yaml`](entities/input_number/threshold/will_s_office_fan/will_s_office_fan_purifier_speed.yaml)
</details>

<details><summary><strong>Will's Office Fan: VOC Index Threshold</strong></summary>

**Entity ID: `input_number.will_s_office_fan_voc_index_threshold`**

- Max: 10
- Min: 0.5
- Mode: `box`

File: [`input_number/threshold/will_s_office_fan/will_s_office_fan_voc_index_threshold.yaml`](entities/input_number/threshold/will_s_office_fan/will_s_office_fan_voc_index_threshold.yaml)
</details>

<details><summary><strong>Air Freshener | Timeout</strong></summary>

**Entity ID: `input_number.air_freshener_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 300
- Min: 10
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/air_freshener_timeout.yaml`](entities/input_number/timeout/air_freshener_timeout.yaml)
</details>

<details><summary><strong>Basement Lights | Timeout</strong></summary>

**Entity ID: `input_number.basement_lights_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 300
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/basement_lights_timeout.yaml`](entities/input_number/timeout/basement_lights_timeout.yaml)
</details>

<details><summary><strong>Basement | Room Vacancy Light Timeout</strong></summary>

**Entity ID: `input_number.basement_room_vacancy_light_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 60
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/basement_room_vacancy_light_timeout.yaml`](entities/input_number/timeout/basement_room_vacancy_light_timeout.yaml)
</details>

<details><summary><strong>Dry Box | Dehumidifier Timeout</strong></summary>

**Entity ID: `input_number.dry_box_dehumidifier_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 720
- Min: 10
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/dry_box_dehumidifier_timeout.yaml`](entities/input_number/timeout/dry_box_dehumidifier_timeout.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 1</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_1`**

- Max: 480
- Min: 1
- Mode: `box`
- Unit Of Measurement: `min`

File: [`input_number/timeout/electric_blanket_timeout_level_1.yaml`](entities/input_number/timeout/electric_blanket_timeout_level_1.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 2</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_2`**

- Max: 480
- Min: 1
- Mode: `box`
- Unit Of Measurement: `min`

File: [`input_number/timeout/electric_blanket_timeout_level_2.yaml`](entities/input_number/timeout/electric_blanket_timeout_level_2.yaml)
</details>

<details><summary><strong>Electric Blanket Timeout: Level 3</strong></summary>

**Entity ID: `input_number.electric_blanket_timeout_level_3`**

- Max: 480
- Min: 1
- Mode: `box`
- Unit Of Measurement: `min`

File: [`input_number/timeout/electric_blanket_timeout_level_3.yaml`](entities/input_number/timeout/electric_blanket_timeout_level_3.yaml)
</details>

<details><summary><strong>Hallway Lights | Timeout</strong></summary>

**Entity ID: `input_number.hallway_lights_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 300
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/hallway_lights_timeout.yaml`](entities/input_number/timeout/hallway_lights_timeout.yaml)
</details>

<details><summary><strong>Lounge | Diffuser: Timeout</strong></summary>

**Entity ID: `input_number.lounge_diffuser_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 86400
- Min: 15
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/lounge_diffuser_timeout.yaml`](entities/input_number/timeout/lounge_diffuser_timeout.yaml)
</details>

<details><summary><strong>Lounge | Lights: Timeout</strong></summary>

**Entity ID: `input_number.lounge_lights_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 300
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/lounge_lights_timeout.yaml`](entities/input_number/timeout/lounge_lights_timeout.yaml)
</details>

<details><summary><strong>Lounge | Room Timeout</strong></summary>

**Entity ID: `input_number.lounge_room_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 120
- Min: 5
- Mode: `box`
- Unit Of Measurement: `min`

File: [`input_number/timeout/lounge_room_timeout.yaml`](entities/input_number/timeout/lounge_room_timeout.yaml)
</details>

<details><summary><strong>Prusa i3 Bed | Timeout</strong></summary>

**Entity ID: `input_number.prusa_i3_bed_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 60
- Min: 10
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/prusa_i3_bed_timeout.yaml`](entities/input_number/timeout/prusa_i3_bed_timeout.yaml)
</details>

<details><summary><strong>Prusa i3 Hotend | Timeout</strong></summary>

**Entity ID: `input_number.prusa_i3_hotend_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 60
- Min: 10
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/prusa_i3_hotend_timeout.yaml`](entities/input_number/timeout/prusa_i3_hotend_timeout.yaml)
</details>

<details><summary><strong>Prusa i3 Power | Timeout</strong></summary>

**Entity ID: `input_number.prusa_i3_power_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 300
- Min: 10
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/timeout/prusa_i3_power_timeout.yaml`](entities/input_number/timeout/prusa_i3_power_timeout.yaml)
</details>

<details><summary><strong>Wardrobe Lights | Timeout</strong></summary>

**Entity ID: `input_number.wardrobe_lights_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 900
- Min: 5
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/wardrobe_lights_timeout.yaml`](entities/input_number/timeout/wardrobe_lights_timeout.yaml)
</details>

<details><summary><strong>Will's Office | Heating: External Opening Timeout</strong></summary>

**Entity ID: `input_number.will_s_office_heating_external_opening_timeout`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 600
- Min: 5
- Mode: `box`
- Unit Of Measurement: `s`

File: [`input_number/timeout/will_s_office_heating_external_opening_timeout.yaml`](entities/input_number/timeout/will_s_office_heating_external_opening_timeout.yaml)
</details>

<details><summary><strong>Topaz SR10 | Power Off Timeout</strong></summary>

**Entity ID: `input_number.topaz_sr10_power_off_timeout`**

- Icon: [`mdi:timer-music-outline`](https://pictogrammers.com/library/mdi/icon/timer-music-outline/)
- Max: 120
- Min: 1
- Mode: `box`
- Unit Of Measurement: `minutes`

File: [`input_number/topaz_sr10/topaz_sr10_power_off_timeout.yaml`](entities/input_number/topaz_sr10/topaz_sr10_power_off_timeout.yaml)
</details>

<details><summary><strong>Topaz SR10 | Volume Level</strong></summary>

**Entity ID: `input_number.topaz_sr10_volume_level`**

- Icon: [`mdi:volume-high`](https://pictogrammers.com/library/mdi/icon/volume-high/)
- Min: -80
- Mode: `box`
- Unit Of Measurement: dB

File: [`input_number/topaz_sr10/topaz_sr10_volume_level.yaml`](entities/input_number/topaz_sr10/topaz_sr10_volume_level.yaml)
</details>

<details><summary><strong>Will's Office | Grow Light: Daytime Light Level Threshold</strong></summary>

**Entity ID: `input_number.will_s_office_grow_light_daytime_light_level_threshold`**

- Icon: [`mdi:brightness-6`](https://pictogrammers.com/library/mdi/icon/brightness-6/)
- Max: 5000
- Mode: `box`
- Unit Of Measurement: `lx`

File: [`input_number/will_s_office_grow_light_daytime_light_level_threshold.yaml`](entities/input_number/will_s_office_grow_light_daytime_light_level_threshold.yaml)
</details>

<details><summary><strong>Will's Office | Grow Light: Trigger Delay</strong></summary>

**Entity ID: `input_number.will_s_office_grow_light_trigger_delay`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Max: 60
- Mode: `box`
- Unit Of Measurement: `mins`

File: [`input_number/will_s_office_grow_light_trigger_delay.yaml`](entities/input_number/will_s_office_grow_light_trigger_delay.yaml)
</details>

</details>

## Input Select

<details><summary><h3>Entities (8)</h3></summary>

<details><summary><strong>Add-on Stats Legend Sensor Type</strong></summary>

**Entity ID: `input_select.add_on_stats_legend_sensor_type`**

- Icon: [`mdi:docker`](https://pictogrammers.com/library/mdi/icon/docker/)

File: [`input_select/add_on_stats_legend_sensor_type.yaml`](entities/input_select/add_on_stats_legend_sensor_type.yaml)
</details>

<details><summary><strong>CRTPi | Media Player Source</strong></summary>

**Entity ID: `input_select.crtpi_media_player_source`**

- Icon: [`mdi:disc-player`](https://pictogrammers.com/library/mdi/icon/disc-player/)

File: [`input_select/crtpi/crtpi_media_player_source.yaml`](entities/input_select/crtpi/crtpi_media_player_source.yaml)
</details>

<details><summary><strong>GH CLI | Active User</strong></summary>

**Entity ID: `input_select.gh_cli_active_user`**

- Icon: [`mdi:badge-account-outline`](https://pictogrammers.com/library/mdi/icon/badge-account-outline/)

File: [`input_select/gh_cli_active_user.yaml`](entities/input_select/gh_cli_active_user.yaml)
</details>

<details><summary><strong>MtrxPi | Media Player Source</strong></summary>

**Entity ID: `input_select.mtrxpi_media_player_source`**

- Icon: [`mdi:disc-player`](https://pictogrammers.com/library/mdi/icon/disc-player/)

File: [`input_select/mtrxpi/mtrxpi_media_player_source.yaml`](entities/input_select/mtrxpi/mtrxpi_media_player_source.yaml)
</details>

<details><summary><strong>Office Shapes Artwork Mapping Source</strong></summary>

**Entity ID: `input_select.office_shapes_artwork_mapping_source`**

- Icon: [`mdi:disc-player`](https://pictogrammers.com/library/mdi/icon/disc-player/)

File: [`input_select/office_shapes_artwork_mapping_source.yaml`](entities/input_select/office_shapes_artwork_mapping_source.yaml)
</details>

<details><summary><strong>Pi Stats Legend Sensor Type</strong></summary>

**Entity ID: `input_select.pi_stats_legend_sensor_type`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`input_select/pi_stats_legend_sensor_type.yaml`](entities/input_select/pi_stats_legend_sensor_type.yaml)
</details>

<details><summary><strong>Target Git Branch</strong></summary>

**Entity ID: `input_select.target_git_branch`**

- Icon: [`mdi:source-branch`](https://pictogrammers.com/library/mdi/icon/source-branch/)

File: [`input_select/target_git_branch.yaml`](entities/input_select/target_git_branch.yaml)
</details>

<details><summary><strong>Topaz SR10 Source</strong></summary>

**Entity ID: `input_select.topaz_sr10_source`**

- Icon: [`mdi:audio-input-rca`](https://pictogrammers.com/library/mdi/icon/audio-input-rca/)

File: [`input_select/topaz_sr10_source.yaml`](entities/input_select/topaz_sr10_source.yaml)
</details>

</details>

## Input Text

<details><summary><h3>Entities (20)</h3></summary>

<details><summary><strong>AD: Get Latest Release</strong></summary>

**Entity ID: `input_text.ad_get_latest_release`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)
- Pattern: ^\d+\.\d+\.\d+$

File: [`input_text/appdaemon/ad_get_latest_release.yaml`](entities/input_text/appdaemon/ad_get_latest_release.yaml)
</details>

<details><summary><strong>Monzo Auth Token (Auto Saver)</strong></summary>

**Entity ID: `input_text.monzo_auth_token_auto_saver`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/monzo_auth_token_auto_saver.yaml`](entities/input_text/appdaemon/monzo_auth_token_auto_saver.yaml)
</details>

<details><summary><strong>Monzo Auth Token (CC Pot Top-Up)</strong></summary>

**Entity ID: `input_text.monzo_auth_token_cc_pot_top_up`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/monzo_auth_token_cc_pot_top_up.yaml`](entities/input_text/appdaemon/monzo_auth_token_cc_pot_top_up.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Amex)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_amex`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_amex.yaml`](entities/input_text/appdaemon/truelayer_auth_token_amex.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Amex Auto Saver)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_amex_auto_saver`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_amex_auto_saver.yaml`](entities/input_text/appdaemon/truelayer_auth_token_amex_auto_saver.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (HSBC)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_hsbc`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_hsbc.yaml`](entities/input_text/appdaemon/truelayer_auth_token_hsbc.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Monzo)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_monzo`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_monzo.yaml`](entities/input_text/appdaemon/truelayer_auth_token_monzo.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Santander)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_santander`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_santander.yaml`](entities/input_text/appdaemon/truelayer_auth_token_santander.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Starling)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_starling`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_starling.yaml`](entities/input_text/appdaemon/truelayer_auth_token_starling.yaml)
</details>

<details><summary><strong>TrueLayer Auth Token (Starling Joint)</strong></summary>

**Entity ID: `input_text.truelayer_auth_token_starling_joint`**

- Icon: [`mdi:application-variable`](https://pictogrammers.com/library/mdi/icon/application-variable/)

File: [`input_text/appdaemon/truelayer_auth_token_starling_joint.yaml`](entities/input_text/appdaemon/truelayer_auth_token_starling_joint.yaml)
</details>

<details><summary><strong>Auto-Save Naughty Transaction Pattern</strong></summary>

**Entity ID: `input_text.auto_save_naughty_transaction_pattern`**

- Icon: [`mdi:regex`](https://pictogrammers.com/library/mdi/icon/regex/)

File: [`input_text/auto_save_naughty_transaction_pattern.yaml`](entities/input_text/auto_save_naughty_transaction_pattern.yaml)
</details>

<details><summary><strong>Cube | Entity 1</strong></summary>

**Entity ID: `input_text.cube_entity_1`**

- Icon: [`mdi:numeric-1-box`](https://pictogrammers.com/library/mdi/icon/numeric-1-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_1.yaml`](entities/input_text/cube/cube_entity_1.yaml)
</details>

<details><summary><strong>Cube | Entity 2</strong></summary>

**Entity ID: `input_text.cube_entity_2`**

- Icon: [`mdi:numeric-2-box`](https://pictogrammers.com/library/mdi/icon/numeric-2-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_2.yaml`](entities/input_text/cube/cube_entity_2.yaml)
</details>

<details><summary><strong>Cube | Entity 3</strong></summary>

**Entity ID: `input_text.cube_entity_3`**

- Icon: [`mdi:numeric-3-box`](https://pictogrammers.com/library/mdi/icon/numeric-3-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_3.yaml`](entities/input_text/cube/cube_entity_3.yaml)
</details>

<details><summary><strong>Cube | Entity 4</strong></summary>

**Entity ID: `input_text.cube_entity_4`**

- Icon: [`mdi:numeric-4-box`](https://pictogrammers.com/library/mdi/icon/numeric-4-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_4.yaml`](entities/input_text/cube/cube_entity_4.yaml)
</details>

<details><summary><strong>Cube | Entity 5</strong></summary>

**Entity ID: `input_text.cube_entity_5`**

- Icon: [`mdi:numeric-5-box`](https://pictogrammers.com/library/mdi/icon/numeric-5-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_5.yaml`](entities/input_text/cube/cube_entity_5.yaml)
</details>

<details><summary><strong>Cube | Entity 6</strong></summary>

**Entity ID: `input_text.cube_entity_6`**

- Icon: [`mdi:numeric-6-box`](https://pictogrammers.com/library/mdi/icon/numeric-6-box/)
- Pattern: ^[a-z][a-z_0-9]+\.[a-z_0-9]+$

File: [`input_text/cube/cube_entity_6.yaml`](entities/input_text/cube/cube_entity_6.yaml)
</details>

<details><summary><strong>Test MQTT Events Device Name</strong></summary>

**Entity ID: `input_text.test_mqtt_events_device_name`**

- Icon: [`mdi:identifier`](https://pictogrammers.com/library/mdi/icon/identifier/)

File: [`input_text/test_mqtt_events_device_name.yaml`](entities/input_text/test_mqtt_events_device_name.yaml)
</details>

<details><summary><strong>Vic | Work Calendar: Holiday Pattern</strong></summary>

**Entity ID: `input_text.vic_work_calendar_holiday_pattern`**

- Icon: [`mdi:regex`](https://pictogrammers.com/library/mdi/icon/regex/)

File: [`input_text/vic_work_calendar_holiday_pattern.yaml`](entities/input_text/vic_work_calendar_holiday_pattern.yaml)
</details>

<details><summary><strong>Will's Office Webcam Name</strong></summary>

**Entity ID: `input_text.will_s_office_webcam_name`**

- Icon: [`mdi:camera`](https://pictogrammers.com/library/mdi/icon/camera/)

File: [`input_text/will_s_office_webcam_name.yaml`](entities/input_text/will_s_office_webcam_name.yaml)
</details>

</details>

## Light

<details><summary><h3>Entities (1)</h3></summary>

<details><summary><strong>MtrxPi LED Matrix Brightness</strong></summary>

**Entity ID: `light.mtrxpi_led_matrix_brightness`**

File: [`light/mtrxpi_led_matrix_brightness.yaml`](entities/light/mtrxpi_led_matrix_brightness.yaml)
</details>

</details>

## Media Player

<details><summary><h3>Entities (2)</h3></summary>

<details><summary><strong>HiFi System</strong></summary>

**Entity ID: `media_player.media_player.hifi_system`**

- Platform: `universal`

File: [`media_player/hifi_system.yaml`](entities/media_player/hifi_system.yaml)
</details>

<details><summary><strong>Topaz SR10</strong></summary>

**Entity ID: `media_player.media_player.topaz_sr10`**

- Platform: `universal`

File: [`media_player/topaz_sr10.yaml`](entities/media_player/topaz_sr10.yaml)
</details>

</details>

## Mqtt

<details><summary><h3>Entities (136)</h3></summary>

<details><summary><strong>MtrxPi | Audio Visualiser: Chunk Size</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_chunk_size`**

- Icon: [`mdi:table-split-cell`](https://pictogrammers.com/library/mdi/icon/table-split-cell/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/chunk-size
- State Topic: /mtrxpi/audio-visualiser/parameter/chunk-size
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/chunk_size.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/chunk_size.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Colormap Length</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_colormap_length`**

- Icon: [`mdi:palette`](https://pictogrammers.com/library/mdi/icon/palette/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/colormap-length
- State Topic: /mtrxpi/audio-visualiser/parameter/colormap-length
- Unit Of Measurement: `colors`

File: [`mqtt/number/mtrxpi/audio_visualiser/colormap_length.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/colormap_length.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Cutoff Frequency</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_cutoff_frequency`**

- Icon: [`mdi:arrow-collapse-up`](https://pictogrammers.com/library/mdi/icon/arrow-collapse-up/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/cutoff-frequency
- State Topic: /mtrxpi/audio-visualiser/parameter/cutoff-frequency
- Unit Of Measurement: Hz

File: [`mqtt/number/mtrxpi/audio_visualiser/cutoff_frequency.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/cutoff_frequency.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: High Freq X</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_high_freq_x`**

- Icon: [`mdi:star-four-points-circle`](https://pictogrammers.com/library/mdi/icon/star-four-points-circle/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/high-freq-x
- State Topic: /mtrxpi/audio-visualiser/parameter/high-freq-x
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/high_freq_x.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/high_freq_x.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: High Freq Y</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_high_freq_y`**

- Icon: [`mdi:star-four-points-circle`](https://pictogrammers.com/library/mdi/icon/star-four-points-circle/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/high-freq-y
- State Topic: /mtrxpi/audio-visualiser/parameter/high-freq-y
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/high_freq_y.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/high_freq_y.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Low Freq X</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_low_freq_x`**

- Icon: [`mdi:star-four-points-circle-outline`](https://pictogrammers.com/library/mdi/icon/star-four-points-circle-outline/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/low-freq-x
- State Topic: /mtrxpi/audio-visualiser/parameter/low-freq-x
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/low_freq_x.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/low_freq_x.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Low Freq Y</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_low_freq_y`**

- Icon: [`mdi:star-four-points-circle-outline`](https://pictogrammers.com/library/mdi/icon/star-four-points-circle-outline/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/low-freq-y
- State Topic: /mtrxpi/audio-visualiser/parameter/low-freq-y
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/low_freq_y.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/low_freq_y.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Sample Rate</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_sample_rate`**

- Icon: [`mdi:sine-wave`](https://pictogrammers.com/library/mdi/icon/sine-wave/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/sample-rate
- State Topic: /mtrxpi/audio-visualiser/parameter/sample-rate
- Unit Of Measurement: Hz

File: [`mqtt/number/mtrxpi/audio_visualiser/sample_rate.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/sample_rate.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/x-pos
- State Topic: /mtrxpi/audio-visualiser/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/x_pos.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/y-pos
- State Topic: /mtrxpi/audio-visualiser/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/audio_visualiser/y_pos.yaml`](entities/mqtt/number/mtrxpi/audio_visualiser/y_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Clock: Scale</strong></summary>

**Entity ID: `mqtt.mtrxpi_clock_scale`**

- Icon: [`mdi:relative-scale`](https://pictogrammers.com/library/mdi/icon/relative-scale/)
- Command Topic: /mtrxpi/clock/parameter/scale
- State Topic: /mtrxpi/clock/parameter/scale
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/clock/scale.yaml`](entities/mqtt/number/mtrxpi/clock/scale.yaml)
</details>

<details><summary><strong>MtrxPi | Clock: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_clock_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/clock/parameter/x-pos
- State Topic: /mtrxpi/clock/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/clock/x_pos.yaml`](entities/mqtt/number/mtrxpi/clock/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Clock: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_clock_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/clock/parameter/y-pos
- State Topic: /mtrxpi/clock/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/clock/y_pos.yaml`](entities/mqtt/number/mtrxpi/clock/y_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Combination: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_combination_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/combination/parameter/x-pos
- State Topic: /mtrxpi/combination/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/combination/x_pos.yaml`](entities/mqtt/number/mtrxpi/combination/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Combination: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_combination_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/combination/parameter/y-pos
- State Topic: /mtrxpi/combination/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/combination/y_pos.yaml`](entities/mqtt/number/mtrxpi/combination/y_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Matrix: Brightness</strong></summary>

**Entity ID: `mqtt.mtrxpi_matrix_brightness`**

- Icon: [`mdi:brightness-percent`](https://pictogrammers.com/library/mdi/icon/brightness-percent/)
- Command Topic: /mtrxpi/matrix/parameter/brightness
- Unit Of Measurement: %

File: [`mqtt/number/mtrxpi/matrix/brightness.yaml`](entities/mqtt/number/mtrxpi/matrix/brightness.yaml)
</details>

<details><summary><strong>MtrxPi | Now Playing: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_now_playing_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/now-playing/parameter/x-pos
- State Topic: /mtrxpi/now-playing/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/now_playing/x_pos.yaml`](entities/mqtt/number/mtrxpi/now_playing/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Now Playing: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_now_playing_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/now-playing/parameter/y-pos
- State Topic: /mtrxpi/now-playing/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/now_playing/y_pos.yaml`](entities/mqtt/number/mtrxpi/now_playing/y_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Distance Between Plants</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_distance_between_plants`**

- Icon: [`mdi:flower`](https://pictogrammers.com/library/mdi/icon/flower/)
- Command Topic: /mtrxpi/raining-grid/parameter/distance-between-plants
- State Topic: /mtrxpi/raining-grid/parameter/distance-between-plants
- Unit Of Measurement: `pixels`

File: [`mqtt/number/mtrxpi/raining_grid/distance_between_plants.yaml`](entities/mqtt/number/mtrxpi/raining_grid/distance_between_plants.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Leaf Growth Chance</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_leaf_growth_chance`**

- Icon: [`mdi:flower`](https://pictogrammers.com/library/mdi/icon/flower/)
- Command Topic: /mtrxpi/raining-grid/parameter/leaf-growth-chance
- State Topic: /mtrxpi/raining-grid/parameter/leaf-growth-chance
- Unit Of Measurement: %

File: [`mqtt/number/mtrxpi/raining_grid/leaf_growth_chance.yaml`](entities/mqtt/number/mtrxpi/raining_grid/leaf_growth_chance.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Plant Decay Propagation Speed</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_plant_decay_propagation_speed`**

- Icon: [`mdi:flower`](https://pictogrammers.com/library/mdi/icon/flower/)
- Command Topic: /mtrxpi/raining-grid/parameter/plant-decay-propagation-speed
- State Topic: /mtrxpi/raining-grid/parameter/plant-decay-propagation-speed
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/raining_grid/plant_decay_propagation_speed.yaml`](entities/mqtt/number/mtrxpi/raining_grid/plant_decay_propagation_speed.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Plant Growth Chance</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_plant_growth_chance`**

- Icon: [`mdi:flower`](https://pictogrammers.com/library/mdi/icon/flower/)
- Command Topic: /mtrxpi/raining-grid/parameter/plant-growth-chance
- State Topic: /mtrxpi/raining-grid/parameter/plant-growth-chance
- Unit Of Measurement: %

File: [`mqtt/number/mtrxpi/raining_grid/plant_growth_chance.yaml`](entities/mqtt/number/mtrxpi/raining_grid/plant_growth_chance.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Plant Limit</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_plant_limit`**

- Icon: [`mdi:flower`](https://pictogrammers.com/library/mdi/icon/flower/)
- Command Topic: /mtrxpi/raining-grid/parameter/plant-limit
- State Topic: /mtrxpi/raining-grid/parameter/plant-limit
- Unit Of Measurement: `plants`

File: [`mqtt/number/mtrxpi/raining_grid/plant_limit.yaml`](entities/mqtt/number/mtrxpi/raining_grid/plant_limit.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Rain Chance</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_rain_chance`**

- Icon: [`mdi:cloud-percent-outline`](https://pictogrammers.com/library/mdi/icon/cloud-percent-outline/)
- Command Topic: /mtrxpi/raining-grid/parameter/rain-chance
- State Topic: /mtrxpi/raining-grid/parameter/rain-chance
- Unit Of Measurement: %

File: [`mqtt/number/mtrxpi/raining_grid/rain_chance.yaml`](entities/mqtt/number/mtrxpi/raining_grid/rain_chance.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Rain Speed</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_rain_speed`**

- Icon: [`mdi:speedometer`](https://pictogrammers.com/library/mdi/icon/speedometer/)
- Command Topic: /mtrxpi/raining-grid/frequency/rain-speed
- State Topic: /mtrxpi/raining-grid/frequency/rain-speed
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/raining_grid/rain_speed.yaml`](entities/mqtt/number/mtrxpi/raining_grid/rain_speed.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Splash Speed</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_splash_speed`**

- Icon: [`mdi:speedometer`](https://pictogrammers.com/library/mdi/icon/speedometer/)
- Command Topic: /mtrxpi/raining-grid/frequency/splash-speed
- State Topic: /mtrxpi/raining-grid/frequency/splash-speed
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/raining_grid/splash_speed.yaml`](entities/mqtt/number/mtrxpi/raining_grid/splash_speed.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/raining-grid/parameter/x-pos
- State Topic: /mtrxpi/raining-grid/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/raining_grid/x_pos.yaml`](entities/mqtt/number/mtrxpi/raining_grid/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Raining Grid: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_raining_grid_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/raining-grid/parameter/y-pos
- State Topic: /mtrxpi/raining-grid/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/raining_grid/y_pos.yaml`](entities/mqtt/number/mtrxpi/raining_grid/y_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Food Generation Freq</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_food_generation_freq`**

- Icon: [`mdi:food-apple`](https://pictogrammers.com/library/mdi/icon/food-apple/)
- Command Topic: /mtrxpi/snake/frequency/food-generation-freq
- State Topic: /mtrxpi/snake/frequency/food-generation-freq
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/snake/food_generation_freq.yaml`](entities/mqtt/number/mtrxpi/snake/food_generation_freq.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Iterations</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_iterations`**

- Icon: [`mdi:counter`](https://pictogrammers.com/library/mdi/icon/counter/)
- Command Topic: /mtrxpi/snake/parameter/iterations
- State Topic: /mtrxpi/snake/parameter/iterations
- Unit Of Measurement: `iterations`

File: [`mqtt/number/mtrxpi/snake/iterations.yaml`](entities/mqtt/number/mtrxpi/snake/iterations.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Iterations Remaining</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_iterations_remaining`**

- Icon: [`mdi:counter`](https://pictogrammers.com/library/mdi/icon/counter/)
- Command Topic: /mtrxpi/snake/parameter/iterations-remaining
- State Topic: /mtrxpi/snake/parameter/iterations-remaining
- Unit Of Measurement: `iterations`

File: [`mqtt/number/mtrxpi/snake/iterations_remaining.yaml`](entities/mqtt/number/mtrxpi/snake/iterations_remaining.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Snake Speed</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_snake_speed`**

- Icon: [`mdi:speedometer`](https://pictogrammers.com/library/mdi/icon/speedometer/)
- Command Topic: /mtrxpi/snake/frequency/snake-speed
- State Topic: /mtrxpi/snake/frequency/snake-speed
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/snake/snake_speed.yaml`](entities/mqtt/number/mtrxpi/snake/snake_speed.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Turn Chance</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_turn_chance`**

- Icon: [`mdi:dice-multiple`](https://pictogrammers.com/library/mdi/icon/dice-multiple/)
- Command Topic: /mtrxpi/snake/parameter/turn-chance
- State Topic: /mtrxpi/snake/parameter/turn-chance
- Unit Of Measurement: %

File: [`mqtt/number/mtrxpi/snake/turn_chance.yaml`](entities/mqtt/number/mtrxpi/snake/turn_chance.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Turn Cooldown</strong></summary>

**Entity ID: `mqtt.mtrxpi_snake_turn_cooldown`**

- Icon: [`mdi:timer-sand`](https://pictogrammers.com/library/mdi/icon/timer-sand/)
- Command Topic: /mtrxpi/snake/parameter/turn-cooldown
- State Topic: /mtrxpi/snake/parameter/turn-cooldown
- Unit Of Measurement: `ticks`

File: [`mqtt/number/mtrxpi/snake/turn_cooldown.yaml`](entities/mqtt/number/mtrxpi/snake/turn_cooldown.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Completion Display Time</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_completion_display_time`**

- Icon: [`mdi:presentation-play`](https://pictogrammers.com/library/mdi/icon/presentation-play/)
- Command Topic: /mtrxpi/sorter/parameter/completion-display-time
- State Topic: /mtrxpi/sorter/parameter/completion-display-time
- Unit Of Measurement: `s`

File: [`mqtt/number/mtrxpi/sorter/completion_display_time.yaml`](entities/mqtt/number/mtrxpi/sorter/completion_display_time.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Iterations</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_iterations`**

- Icon: [`mdi:counter`](https://pictogrammers.com/library/mdi/icon/counter/)
- Command Topic: /mtrxpi/sorter/parameter/iterations
- State Topic: /mtrxpi/sorter/parameter/iterations
- Unit Of Measurement: `iterations`

File: [`mqtt/number/mtrxpi/sorter/iterations.yaml`](entities/mqtt/number/mtrxpi/sorter/iterations.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: X Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_x_pos`**

- Icon: [`mdi:arrow-left-right`](https://pictogrammers.com/library/mdi/icon/arrow-left-right/)
- Command Topic: /mtrxpi/sorter/parameter/x-pos
- State Topic: /mtrxpi/sorter/parameter/x-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/sorter/x_pos.yaml`](entities/mqtt/number/mtrxpi/sorter/x_pos.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Y Pos</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_y_pos`**

- Icon: [`mdi:arrow-up-down`](https://pictogrammers.com/library/mdi/icon/arrow-up-down/)
- Command Topic: /mtrxpi/sorter/parameter/y-pos
- State Topic: /mtrxpi/sorter/parameter/y-pos
- Unit Of Measurement:

File: [`mqtt/number/mtrxpi/sorter/y_pos.yaml`](entities/mqtt/number/mtrxpi/sorter/y_pos.yaml)
</details>

<details><summary><strong>Prusa i3 | Target Bed Temperature</strong></summary>

**Entity ID: `mqtt.prusa_i3_target_bed_temperature`**

- Icon: [`mdi:grid`](https://pictogrammers.com/library/mdi/icon/grid/)
- Command Topic: /octopi/prusa-i3/target-bed-temperature
- State Topic: octoPrint/temperature/bed
- Unit Of Measurement: °C

File: [`mqtt/number/prusa_i3/target_bed_temperature.yaml`](entities/mqtt/number/prusa_i3/target_bed_temperature.yaml)
</details>

<details><summary><strong>Prusa i3 | Target Hotend Temperature</strong></summary>

**Entity ID: `mqtt.prusa_i3_target_hotend_temperature`**

- Icon: [`mdi:printer-3d-nozzle-heat`](https://pictogrammers.com/library/mdi/icon/printer-3d-nozzle-heat/)
- Command Topic: /octopi/prusa-i3/target-hotend-temperature
- State Topic: octoPrint/temperature/tool0
- Unit Of Measurement: °C

File: [`mqtt/number/prusa_i3/target_hotend_temperature.yaml`](entities/mqtt/number/prusa_i3/target_hotend_temperature.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Algorithm</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_algorithm`**

- Icon: [`mdi:sort`](https://pictogrammers.com/library/mdi/icon/sort/)
- Command Topic: /mtrxpi/sorter/parameter/algorithm
- State Topic: /mtrxpi/sorter/parameter/algorithm

File: [`mqtt/select/mtrxpi/sorter/algorithm.yaml`](entities/mqtt/select/mtrxpi/sorter/algorithm.yaml)
</details>

<details><summary><strong>CRTPi Active Git Ref</strong></summary>

**Entity ID: `sensor.crtpi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/active_git_ref.yaml`](entities/mqtt/sensor/crtpi/active_git_ref.yaml)
</details>

<details><summary><strong>CRTPi Ambient Humidity</strong></summary>

**Entity ID: `sensor.crtpi_ambient_humidity`**

- Icon: [`mdi:water-percent`](https://pictogrammers.com/library/mdi/icon/water-percent/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/dht22
- Unit Of Measurement: %

File: [`mqtt/sensor/crtpi/ambient_humidity.yaml`](entities/mqtt/sensor/crtpi/ambient_humidity.yaml)
</details>

<details><summary><strong>CRTPi Ambient Temperature</strong></summary>

**Entity ID: `sensor.crtpi_ambient_temperature`**

- Icon: [`mdi:thermometer`](https://pictogrammers.com/library/mdi/icon/thermometer/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/dht22
- Unit Of Measurement: °C

File: [`mqtt/sensor/crtpi/ambient_temperature.yaml`](entities/mqtt/sensor/crtpi/ambient_temperature.yaml)
</details>

<details><summary><strong>CRTPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.crtpi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/average_load_15_min.yaml`](entities/mqtt/sensor/crtpi/average_load_15_min.yaml)
</details>

<details><summary><strong>CRTPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.crtpi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/average_load_1_min.yaml`](entities/mqtt/sensor/crtpi/average_load_1_min.yaml)
</details>

<details><summary><strong>CRTPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.crtpi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/average_load_5_min.yaml`](entities/mqtt/sensor/crtpi/average_load_5_min.yaml)
</details>

<details><summary><strong>CrtPi Boot Time</strong></summary>

**Entity ID: `sensor.crtpi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/boot_time.yaml`](entities/mqtt/sensor/crtpi/boot_time.yaml)
</details>

<details><summary><strong>CRTPi CPU Temperature</strong></summary>

**Entity ID: `sensor.crtpi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/crtpi/cpu_temperature.yaml`](entities/mqtt/sensor/crtpi/cpu_temperature.yaml)
</details>

<details><summary><strong>CRTPi CPU Usage</strong></summary>

**Entity ID: `sensor.crtpi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/crtpi/cpu_usage.yaml`](entities/mqtt/sensor/crtpi/cpu_usage.yaml)
</details>

<details><summary><strong>CRTPi Disk Usage</strong></summary>

**Entity ID: `sensor.crtpi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/crtpi/disk_usage.yaml`](entities/mqtt/sensor/crtpi/disk_usage.yaml)
</details>

<details><summary><strong>CRTPi Local Git Ref</strong></summary>

**Entity ID: `sensor.crtpi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/local_git_ref.yaml`](entities/mqtt/sensor/crtpi/local_git_ref.yaml)
</details>

<details><summary><strong>CrtPi Local IP Address</strong></summary>

**Entity ID: `sensor.crtpi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/local_ip_address.yaml`](entities/mqtt/sensor/crtpi/local_ip_address.yaml)
</details>

<details><summary><strong>CRTPi Memory Usage</strong></summary>

**Entity ID: `sensor.crtpi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/crtpi/memory_usage.yaml`](entities/mqtt/sensor/crtpi/memory_usage.yaml)
</details>

<details><summary><strong>CrtPi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.crtpi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/crtpi/stats

File: [`mqtt/sensor/crtpi/pi_stats_start_time.yaml`](entities/mqtt/sensor/crtpi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>CrtPi Uptime</strong></summary>

**Entity ID: `sensor.crtpi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/crtpi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/crtpi/uptime.yaml`](entities/mqtt/sensor/crtpi/uptime.yaml)
</details>

<details><summary><strong>GrowPi Active Git Ref</strong></summary>

**Entity ID: `sensor.growpi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/active_git_ref.yaml`](entities/mqtt/sensor/growpi/active_git_ref.yaml)
</details>

<details><summary><strong>GrowPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.growpi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/average_load_15_min.yaml`](entities/mqtt/sensor/growpi/average_load_15_min.yaml)
</details>

<details><summary><strong>GrowPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.growpi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/average_load_1_min.yaml`](entities/mqtt/sensor/growpi/average_load_1_min.yaml)
</details>

<details><summary><strong>GrowPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.growpi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/average_load_5_min.yaml`](entities/mqtt/sensor/growpi/average_load_5_min.yaml)
</details>

<details><summary><strong>GrowPi Boot Time</strong></summary>

**Entity ID: `sensor.growpi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/boot_time.yaml`](entities/mqtt/sensor/growpi/boot_time.yaml)
</details>

<details><summary><strong>GrowPi CPU Temperature</strong></summary>

**Entity ID: `sensor.growpi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/growpi/cpu_temperature.yaml`](entities/mqtt/sensor/growpi/cpu_temperature.yaml)
</details>

<details><summary><strong>GrowPi CPU Usage</strong></summary>

**Entity ID: `sensor.growpi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/growpi/cpu_usage.yaml`](entities/mqtt/sensor/growpi/cpu_usage.yaml)
</details>

<details><summary><strong>GrowPi Disk Usage</strong></summary>

**Entity ID: `sensor.growpi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/growpi/disk_usage.yaml`](entities/mqtt/sensor/growpi/disk_usage.yaml)
</details>

<details><summary><strong>GrowPi Local Git Ref</strong></summary>

**Entity ID: `sensor.growpi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/local_git_ref.yaml`](entities/mqtt/sensor/growpi/local_git_ref.yaml)
</details>

<details><summary><strong>GrowPi Local IP Address</strong></summary>

**Entity ID: `sensor.growpi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/local_ip_address.yaml`](entities/mqtt/sensor/growpi/local_ip_address.yaml)
</details>

<details><summary><strong>GrowPi Memory Usage</strong></summary>

**Entity ID: `sensor.growpi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/growpi/memory_usage.yaml`](entities/mqtt/sensor/growpi/memory_usage.yaml)
</details>

<details><summary><strong>GrowPi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.growpi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/growpi/stats

File: [`mqtt/sensor/growpi/pi_stats_start_time.yaml`](entities/mqtt/sensor/growpi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>GrowPi Uptime</strong></summary>

**Entity ID: `sensor.growpi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/growpi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/growpi/uptime.yaml`](entities/mqtt/sensor/growpi/uptime.yaml)
</details>

<details><summary><strong>MtrxPi Active Git Ref</strong></summary>

**Entity ID: `sensor.mtrxpi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/active_git_ref.yaml`](entities/mqtt/sensor/mtrxpi/active_git_ref.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Processor: Max Magnitude</strong></summary>

**Entity ID: `sensor.mtrxpi_audio_processor_max_magnitude`**

- Icon: [`mdi:volume-vibrate`](https://pictogrammers.com/library/mdi/icon/volume-vibrate/)
- State Class: `measurement`
- State Topic: /mtrxpi/audio-processor/max-magnitude
- Unit Of Measurement:

File: [`mqtt/sensor/mtrxpi/audio_processor/max_magnitude.yaml`](entities/mqtt/sensor/mtrxpi/audio_processor/max_magnitude.yaml)
</details>

<details><summary><strong>MtrxPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.mtrxpi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/average_load_15_min.yaml`](entities/mqtt/sensor/mtrxpi/average_load_15_min.yaml)
</details>

<details><summary><strong>MtrxPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.mtrxpi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/average_load_1_min.yaml`](entities/mqtt/sensor/mtrxpi/average_load_1_min.yaml)
</details>

<details><summary><strong>MtrxPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.mtrxpi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/average_load_5_min.yaml`](entities/mqtt/sensor/mtrxpi/average_load_5_min.yaml)
</details>

<details><summary><strong>MtrxPi Boot Time</strong></summary>

**Entity ID: `sensor.mtrxpi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/boot_time.yaml`](entities/mqtt/sensor/mtrxpi/boot_time.yaml)
</details>

<details><summary><strong>MtrxPi | Content Queue</strong></summary>

**Entity ID: `sensor.mtrxpi_content_queue`**

- Icon: [`mdi:plus-box-multiple`](https://pictogrammers.com/library/mdi/icon/plus-box-multiple/)
- State Topic: /mtrxpi/matrix/content-queue/state
- Unit Of Measurement: `items`

File: [`mqtt/sensor/mtrxpi/content_queue.yaml`](entities/mqtt/sensor/mtrxpi/content_queue.yaml)
</details>

<details><summary><strong>MtrxPi CPU Temperature</strong></summary>

**Entity ID: `sensor.mtrxpi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/mtrxpi/cpu_temperature.yaml`](entities/mqtt/sensor/mtrxpi/cpu_temperature.yaml)
</details>

<details><summary><strong>MtrxPi CPU Usage</strong></summary>

**Entity ID: `sensor.mtrxpi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/mtrxpi/cpu_usage.yaml`](entities/mqtt/sensor/mtrxpi/cpu_usage.yaml)
</details>

<details><summary><strong>MtrxPi | Current Content</strong></summary>

**Entity ID: `sensor.mtrxpi_current_content`**

- Icon: [`mdi:animation-play-outline`](https://pictogrammers.com/library/mdi/icon/animation-play-outline/)
- State Topic: /mtrxpi/matrix/current-content

File: [`mqtt/sensor/mtrxpi/current_content.yaml`](entities/mqtt/sensor/mtrxpi/current_content.yaml)
</details>

<details><summary><strong>MtrxPi Disk Usage</strong></summary>

**Entity ID: `sensor.mtrxpi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/mtrxpi/disk_usage.yaml`](entities/mqtt/sensor/mtrxpi/disk_usage.yaml)
</details>

<details><summary><strong>MtrxPi Local Git Ref</strong></summary>

**Entity ID: `sensor.mtrxpi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/local_git_ref.yaml`](entities/mqtt/sensor/mtrxpi/local_git_ref.yaml)
</details>

<details><summary><strong>MtrxPi Local IP Address</strong></summary>

**Entity ID: `sensor.mtrxpi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/local_ip_address.yaml`](entities/mqtt/sensor/mtrxpi/local_ip_address.yaml)
</details>

<details><summary><strong>MtrxPi Memory Usage</strong></summary>

**Entity ID: `sensor.mtrxpi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/mtrxpi/memory_usage.yaml`](entities/mqtt/sensor/mtrxpi/memory_usage.yaml)
</details>

<details><summary><strong>MtrxPi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.mtrxpi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/mtrxpi/stats

File: [`mqtt/sensor/mtrxpi/pi_stats_start_time.yaml`](entities/mqtt/sensor/mtrxpi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Food Count</strong></summary>

**Entity ID: `sensor.mtrxpi_snake_food_count`**

- Icon: [`mdi:food`](https://pictogrammers.com/library/mdi/icon/food/)
- State Class: `measurement`
- State Topic: /mtrxpi/snake/parameter/food-count
- Unit Of Measurement: `bits`

File: [`mqtt/sensor/mtrxpi/snake/food_count.yaml`](entities/mqtt/sensor/mtrxpi/snake/food_count.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: High Score</strong></summary>

**Entity ID: `sensor.mtrxpi_snake_high_score`**

- Icon: [`mdi:trophy`](https://pictogrammers.com/library/mdi/icon/trophy/)
- State Class: `measurement`
- State Topic: /mtrxpi/snake/parameter/high-score
- Unit Of Measurement: `bits`

File: [`mqtt/sensor/mtrxpi/snake/high_score.yaml`](entities/mqtt/sensor/mtrxpi/snake/high_score.yaml)
</details>

<details><summary><strong>MtrxPi | Snake: Snake Length</strong></summary>

**Entity ID: `sensor.mtrxpi_snake_snake_length`**

- Icon: [`mdi:snake`](https://pictogrammers.com/library/mdi/icon/snake/)
- State Class: `measurement`
- State Topic: /mtrxpi/snake/parameter/snake-length
- Unit Of Measurement: `cells`

File: [`mqtt/sensor/mtrxpi/snake/snake_length.yaml`](entities/mqtt/sensor/mtrxpi/snake/snake_length.yaml)
</details>

<details><summary><strong>MtrxPi Uptime</strong></summary>

**Entity ID: `sensor.mtrxpi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/mtrxpi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/mtrxpi/uptime.yaml`](entities/mqtt/sensor/mtrxpi/uptime.yaml)
</details>

<details><summary><strong>OctoPi Active Git Ref</strong></summary>

**Entity ID: `sensor.octopi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/active_git_ref.yaml`](entities/mqtt/sensor/octopi/active_git_ref.yaml)
</details>

<details><summary><strong>OctoPi Ambient Humidity</strong></summary>

**Entity ID: `sensor.octopi_ambient_humidity`**

- Icon: [`mdi:water-percent`](https://pictogrammers.com/library/mdi/icon/water-percent/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/dht22
- Unit Of Measurement: %

File: [`mqtt/sensor/octopi/ambient_humidity.yaml`](entities/mqtt/sensor/octopi/ambient_humidity.yaml)
</details>

<details><summary><strong>OctoPi Ambient Temperature</strong></summary>

**Entity ID: `sensor.octopi_ambient_temperature`**

- Icon: [`mdi:thermometer`](https://pictogrammers.com/library/mdi/icon/thermometer/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/dht22
- Unit Of Measurement: °C

File: [`mqtt/sensor/octopi/ambient_temperature.yaml`](entities/mqtt/sensor/octopi/ambient_temperature.yaml)
</details>

<details><summary><strong>OctoPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.octopi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/average_load_15_min.yaml`](entities/mqtt/sensor/octopi/average_load_15_min.yaml)
</details>

<details><summary><strong>OctoPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.octopi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/average_load_1_min.yaml`](entities/mqtt/sensor/octopi/average_load_1_min.yaml)
</details>

<details><summary><strong>OctoPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.octopi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/average_load_5_min.yaml`](entities/mqtt/sensor/octopi/average_load_5_min.yaml)
</details>

<details><summary><strong>OctoPi Boot Time</strong></summary>

**Entity ID: `sensor.octopi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/boot_time.yaml`](entities/mqtt/sensor/octopi/boot_time.yaml)
</details>

<details><summary><strong>OctoPi CPU Temperature</strong></summary>

**Entity ID: `sensor.octopi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/octopi/cpu_temperature.yaml`](entities/mqtt/sensor/octopi/cpu_temperature.yaml)
</details>

<details><summary><strong>OctoPi CPU Usage</strong></summary>

**Entity ID: `sensor.octopi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/octopi/cpu_usage.yaml`](entities/mqtt/sensor/octopi/cpu_usage.yaml)
</details>

<details><summary><strong>OctoPi Disk Usage</strong></summary>

**Entity ID: `sensor.octopi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/octopi/disk_usage.yaml`](entities/mqtt/sensor/octopi/disk_usage.yaml)
</details>

<details><summary><strong>OctoPi Local Git Ref</strong></summary>

**Entity ID: `sensor.octopi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/local_git_ref.yaml`](entities/mqtt/sensor/octopi/local_git_ref.yaml)
</details>

<details><summary><strong>OctoPi Local IP Address</strong></summary>

**Entity ID: `sensor.octopi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/local_ip_address.yaml`](entities/mqtt/sensor/octopi/local_ip_address.yaml)
</details>

<details><summary><strong>OctoPi Memory Usage</strong></summary>

**Entity ID: `sensor.octopi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/octopi/memory_usage.yaml`](entities/mqtt/sensor/octopi/memory_usage.yaml)
</details>

<details><summary><strong>OctoPi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.octopi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/octopi/stats

File: [`mqtt/sensor/octopi/pi_stats_start_time.yaml`](entities/mqtt/sensor/octopi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>OctoPi Uptime</strong></summary>

**Entity ID: `sensor.octopi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/octopi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/octopi/uptime.yaml`](entities/mqtt/sensor/octopi/uptime.yaml)
</details>

<details><summary><strong>Prusa i3 Filament Type</strong></summary>

**Entity ID: `sensor.prusa_i3_filament_type`**

- Icon: [`mdi:printer-3d-nozzle`](https://pictogrammers.com/library/mdi/icon/printer-3d-nozzle/)
- State Topic: octoPrint/metadata/slicer_settings.filament_type

File: [`mqtt/sensor/prusa_i3/filament_type.yaml`](entities/mqtt/sensor/prusa_i3/filament_type.yaml)
</details>

<details><summary><strong>RtroPi Active Git Ref</strong></summary>

**Entity ID: `sensor.rtropi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/active_git_ref.yaml`](entities/mqtt/sensor/rtropi/active_git_ref.yaml)
</details>

<details><summary><strong>RtroPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.rtropi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/average_load_15_min.yaml`](entities/mqtt/sensor/rtropi/average_load_15_min.yaml)
</details>

<details><summary><strong>RtroPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.rtropi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/average_load_1_min.yaml`](entities/mqtt/sensor/rtropi/average_load_1_min.yaml)
</details>

<details><summary><strong>RtroPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.rtropi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/average_load_5_min.yaml`](entities/mqtt/sensor/rtropi/average_load_5_min.yaml)
</details>

<details><summary><strong>RtroPi Boot Time</strong></summary>

**Entity ID: `sensor.rtropi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/boot_time.yaml`](entities/mqtt/sensor/rtropi/boot_time.yaml)
</details>

<details><summary><strong>RtroPi CPU Temperature</strong></summary>

**Entity ID: `sensor.rtropi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/rtropi/cpu_temperature.yaml`](entities/mqtt/sensor/rtropi/cpu_temperature.yaml)
</details>

<details><summary><strong>RtroPi CPU Usage</strong></summary>

**Entity ID: `sensor.rtropi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/rtropi/cpu_usage.yaml`](entities/mqtt/sensor/rtropi/cpu_usage.yaml)
</details>

<details><summary><strong>RtroPi Disk Usage</strong></summary>

**Entity ID: `sensor.rtropi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/rtropi/disk_usage.yaml`](entities/mqtt/sensor/rtropi/disk_usage.yaml)
</details>

<details><summary><strong>RtroPi Local Git Ref</strong></summary>

**Entity ID: `sensor.rtropi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/local_git_ref.yaml`](entities/mqtt/sensor/rtropi/local_git_ref.yaml)
</details>

<details><summary><strong>RtroPi Local IP Address</strong></summary>

**Entity ID: `sensor.rtropi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/local_ip_address.yaml`](entities/mqtt/sensor/rtropi/local_ip_address.yaml)
</details>

<details><summary><strong>RtroPi Memory Usage</strong></summary>

**Entity ID: `sensor.rtropi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/rtropi/memory_usage.yaml`](entities/mqtt/sensor/rtropi/memory_usage.yaml)
</details>

<details><summary><strong>Rtropi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.rtropi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/rtropi/stats

File: [`mqtt/sensor/rtropi/pi_stats_start_time.yaml`](entities/mqtt/sensor/rtropi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>RtroPi Uptime</strong></summary>

**Entity ID: `sensor.rtropi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/rtropi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/rtropi/uptime.yaml`](entities/mqtt/sensor/rtropi/uptime.yaml)
</details>

<details><summary><strong>VSMPPi Active Git Ref</strong></summary>

**Entity ID: `sensor.vsmppi_active_git_ref`**

- Icon: [`mdi:source-branch-sync`](https://pictogrammers.com/library/mdi/icon/source-branch-sync/)
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/active_git_ref.yaml`](entities/mqtt/sensor/vsmppi/active_git_ref.yaml)
</details>

<details><summary><strong>VSMPPi Average Load (15 min)</strong></summary>

**Entity ID: `sensor.vsmppi_average_load_15_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/average_load_15_min.yaml`](entities/mqtt/sensor/vsmppi/average_load_15_min.yaml)
</details>

<details><summary><strong>VSMPPi Average Load (1 min)</strong></summary>

**Entity ID: `sensor.vsmppi_average_load_1_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/average_load_1_min.yaml`](entities/mqtt/sensor/vsmppi/average_load_1_min.yaml)
</details>

<details><summary><strong>VSMPPi Average Load (5 min)</strong></summary>

**Entity ID: `sensor.vsmppi_average_load_5_min`**

- Icon: [`mdi:weight`](https://pictogrammers.com/library/mdi/icon/weight/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/average_load_5_min.yaml`](entities/mqtt/sensor/vsmppi/average_load_5_min.yaml)
</details>

<details><summary><strong>VSMPPi Boot Time</strong></summary>

**Entity ID: `sensor.vsmppi_boot_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/boot_time.yaml`](entities/mqtt/sensor/vsmppi/boot_time.yaml)
</details>

<details><summary><strong>VSMPPi CPU Temperature</strong></summary>

**Entity ID: `sensor.vsmppi_cpu_temperature`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats
- Unit Of Measurement: °C

File: [`mqtt/sensor/vsmppi/cpu_temperature.yaml`](entities/mqtt/sensor/vsmppi/cpu_temperature.yaml)
</details>

<details><summary><strong>VSMPPi CPU Usage</strong></summary>

**Entity ID: `sensor.vsmppi_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/vsmppi/cpu_usage.yaml`](entities/mqtt/sensor/vsmppi/cpu_usage.yaml)
</details>

<details><summary><strong>VSMPPi Disk Usage</strong></summary>

**Entity ID: `sensor.vsmppi_disk_usage`**

- Icon: [`mdi:harddisk`](https://pictogrammers.com/library/mdi/icon/harddisk/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/vsmppi/disk_usage.yaml`](entities/mqtt/sensor/vsmppi/disk_usage.yaml)
</details>

<details><summary><strong>VSMPPi Local Git Ref</strong></summary>

**Entity ID: `sensor.vsmppi_local_git_ref`**

- Icon: [`mdi:source-repository`](https://pictogrammers.com/library/mdi/icon/source-repository/)
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/local_git_ref.yaml`](entities/mqtt/sensor/vsmppi/local_git_ref.yaml)
</details>

<details><summary><strong>VSMPPi Local IP Address</strong></summary>

**Entity ID: `sensor.vsmppi_local_ip_address`**

- Icon: [`mdi:ip-network-outline`](https://pictogrammers.com/library/mdi/icon/ip-network-outline/)
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/local_ip_address.yaml`](entities/mqtt/sensor/vsmppi/local_ip_address.yaml)
</details>

<details><summary><strong>VSMPPi Memory Usage</strong></summary>

**Entity ID: `sensor.vsmppi_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats
- Unit Of Measurement: %

File: [`mqtt/sensor/vsmppi/memory_usage.yaml`](entities/mqtt/sensor/vsmppi/memory_usage.yaml)
</details>

<details><summary><strong>VSMPPi Pi Stats Start Time</strong></summary>

**Entity ID: `sensor.vsmppi_pi_stats_start_time`**

- Icon: [`mdi:console`](https://pictogrammers.com/library/mdi/icon/console/)
- State Topic: /homeassistant/vsmppi/stats

File: [`mqtt/sensor/vsmppi/pi_stats_start_time.yaml`](entities/mqtt/sensor/vsmppi/pi_stats_start_time.yaml)
</details>

<details><summary><strong>VSMPPi Uptime</strong></summary>

**Entity ID: `sensor.vsmppi_uptime`**

- Icon: [`mdi:timer-cog-outline`](https://pictogrammers.com/library/mdi/icon/timer-cog-outline/)
- State Class: `measurement`
- State Topic: /homeassistant/vsmppi/stats
- Unit Of Measurement: `s`

File: [`mqtt/sensor/vsmppi/uptime.yaml`](entities/mqtt/sensor/vsmppi/uptime.yaml)
</details>

<details><summary><strong>Zigbee2MQTT Network Map</strong></summary>

**Entity ID: `sensor.zigbee2mqtt_network_map`**

- State Topic: zigbee2mqtt/bridge/response/networkmap

File: [`mqtt/sensor/zigbee2mqtt/network_map.yaml`](entities/mqtt/sensor/zigbee2mqtt/network_map.yaml)
</details>

<details><summary><strong>CRTPi CPU Fan</strong></summary>

**Entity ID: `mqtt.crtpi_cpu_fan`**

- Icon: [`mdi:fan`](https://pictogrammers.com/library/mdi/icon/fan/)
- Command Topic: /homeassistant/crtpi/gpio/cpu-fan

File: [`mqtt/switch/crtpi/cpu_fan.yaml`](entities/mqtt/switch/crtpi/cpu_fan.yaml)
</details>

<details><summary><strong>CRTPi CRT TV Power</strong></summary>

**Entity ID: `mqtt.crtpi_crt_tv_power`**

- Icon: [`mdi:television-classic`](https://pictogrammers.com/library/mdi/icon/television-classic/)
- Command Topic: /homeassistant/crtpi/gpio/crt-tv

File: [`mqtt/switch/crtpi/crt_tv_power.yaml`](entities/mqtt/switch/crtpi/crt_tv_power.yaml)
</details>

<details><summary><strong>MtrxPi | Sorter: Randomize Algorithm</strong></summary>

**Entity ID: `mqtt.mtrxpi_sorter_randomize_algorithm`**

- Icon: [`mdi:shuffle-variant`](https://pictogrammers.com/library/mdi/icon/shuffle-variant/)
- Command Topic: /mtrxpi/sorter/parameter/randomize-algorithm
- State Topic: /mtrxpi/sorter/parameter/randomize-algorithm

File: [`mqtt/switch/mtrxpi/sorter/randomize_algorithm.yaml`](entities/mqtt/switch/mtrxpi/sorter/randomize_algorithm.yaml)
</details>

<details><summary><strong>OctoPi CPU Fan</strong></summary>

**Entity ID: `mqtt.octopi_cpu_fan`**

- Icon: [`mdi:fan`](https://pictogrammers.com/library/mdi/icon/fan/)
- Command Topic: /octopi/gpio/cpu-fan
- State Topic: /octopi/gpio/cpu-fan

File: [`mqtt/switch/octopi/cpu_fan.yaml`](entities/mqtt/switch/octopi/cpu_fan.yaml)
</details>

<details><summary><strong>Prusa i3 Enclosure Fan</strong></summary>

**Entity ID: `mqtt.prusa_i3_enclosure_fan`**

- Icon: [`mdi:fan`](https://pictogrammers.com/library/mdi/icon/fan/)
- Command Topic: /prusa-i3-mk3/enclosure/fan
- State Topic: /prusa-i3-mk3/enclosure/fan

File: [`mqtt/switch/prusa_i3/enclosure_fan.yaml`](entities/mqtt/switch/prusa_i3/enclosure_fan.yaml)
</details>

</details>

## Mqtt

<details><summary><h3>Entities (2)</h3></summary>

<details><summary><strong>MtrxPi | Audio Visualiser: High Magnitude Hex Color</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_high_magnitude_hex_color`**

- Icon: [`mdi:palette`](https://pictogrammers.com/library/mdi/icon/palette/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/high-magnitude-hex-color
- State Topic: /mtrxpi/audio-visualiser/parameter/high-magnitude-hex-color

File: [`mqtt/text/mtrxpi/audio_visualiser/high_magnitude_hex_color.yaml`](entities/mqtt/text/mtrxpi/audio_visualiser/high_magnitude_hex_color.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Low Magnitude Hex Color</strong></summary>

**Entity ID: `mqtt.mtrxpi_audio_visualiser_low_magnitude_hex_color`**

- Icon: [`mdi:palette`](https://pictogrammers.com/library/mdi/icon/palette/)
- Command Topic: /mtrxpi/audio-visualiser/parameter/low-magnitude-hex-color
- State Topic: /mtrxpi/audio-visualiser/parameter/low-magnitude-hex-color

File: [`mqtt/text/mtrxpi/audio_visualiser/low_magnitude_hex_color.yaml`](entities/mqtt/text/mtrxpi/audio_visualiser/low_magnitude_hex_color.yaml)
</details>

</details>

## Rest

<details><summary><h3>Entities (5)</h3></summary>

<details><summary><code>rest.external_ip</code></summary>

- Resource: https://api.ipify.org/?format=json

File: [`rest/external_ip.yaml`](entities/rest/external_ip.yaml)
</details>

<details><summary><code>rest.tomorrow_io_realtime_weather</code></summary>

- Resource: https://api.tomorrow.io/v4/weather/realtime?apikey=abc123&location=51.501366,-0.141888&units=metric
- Method: GET

File: [`rest/tomorrow_io_realtime_weather.yaml`](entities/rest/tomorrow_io_realtime_weather.yaml)
</details>

<details><summary><code>rest.wger_will_weightentry</code></summary>

- Resource: http://10.0.0.104:3000/api/v2/weightentry/?limit=1&ordering=-date

File: [`rest/wger/wger_will_weightentry.yaml`](entities/rest/wger/wger_will_weightentry.yaml)
</details>

<details><summary><code>rest.wger_will_workoutlog</code></summary>

File: [`rest/wger/wger_will_workoutlog.yaml`](entities/rest/wger/wger_will_workoutlog.yaml)
</details>

<details><summary><code>rest.wger_will_workoutsession</code></summary>

- Resource: http://10.0.0.104:3000/api/v2/workoutsession/?limit=1&ordering=-id

File: [`rest/wger/wger_will_workoutsession.yaml`](entities/rest/wger/wger_will_workoutsession.yaml)
</details>

</details>

## Rest Command

<details><summary><h3>Entities (3)</h3></summary>

<details><summary><code>rest_command.get_weightentry</code></summary>

File: [`rest_command/wger/get_weightentry.yaml`](entities/rest_command/wger/get_weightentry.yaml)
</details>

<details><summary><code>rest_command.post_weightentry</code></summary>

File: [`rest_command/wger/post_weightentry.yaml`](entities/rest_command/wger/post_weightentry.yaml)
</details>

<details><summary><code>rest_command.put_weightentry</code></summary>

File: [`rest_command/wger/put_weightentry.yaml`](entities/rest_command/wger/put_weightentry.yaml)
</details>

</details>

## Script

<details><summary><h3>Entities (32)</h3></summary>

<details><summary><strong>AD: Monzo Auto Save</strong></summary>

**Entity ID: `script.ad_monzo_auto_save`**

> *No description provided*

- Mode: `single`

File: [`script/appdaemon_trigger/ad_monzo_auto_save.yaml`](entities/script/appdaemon_trigger/ad_monzo_auto_save.yaml)
</details>

<details><summary><strong>Cosmo: Clean Room</strong></summary>

**Entity ID: `script.cosmo_clean_room`**

> (Try to) get Cosmo to clean a room: if the route is clear, then vacuum the room; otherwise, do nothing. Any other conditions should be evaluated in the calling automation/script.
> Returns 1 if the room clean started, 0 otherwise.

- Fields:

```json
{
  "room_name": {
    "description": "The name of the room to clean",
    "required": true,
    "selector": {
      "area": null
    }
  },
  "repeats": {
    "description": "How many times to repeat the clean (defaults to 3)",
    "required": false,
    "default": 3,
    "selector": {
      "number": {
        "min": 1,
        "max": 3,
        "mode": "slider"
      }
    }
  },
  "suction_level": {
    "description": "The suction level to use (defaults to 2)",
    "required": false,
    "default": 2,
    "selector": {
      "number": {
        "min": 0,
        "max": 3,
        "mode": "slider"
      }
    }
  }
}
```

- Mode: `restart`
- Variables:

```json
{
  "repeats": "{{ repeats | default(3) | int(3) }}",
  "suction_level": "{{ suction_level | default(2) | int(2) }}",
  "suction_level_str": "{{ ['quiet', 'standard', 'strong', 'turbo'][suction_level] }}",
  "true_response": {
    "value": true
  },
  "false_response": {
    "value": false
  }
}
```
File: [`script/cosmo/cosmo_clean_room.yaml`](entities/script/cosmo/cosmo_clean_room.yaml)
</details>

<details><summary><strong>Cosmo: Get Room ID or Name</strong></summary>

**Entity ID: `script.cosmo_get_room_id_or_name`**

> Get a room's ID from its name, or vice versa

- Fields:

```json
{
  "lookup_value": {
    "description": "The value to look up (area or numeric ID)",
    "required": true,
    "selector": {
      "text": null
    }
  }
}
```

- Mode: `parallel`

File: [`script/cosmo/cosmo_get_room_id_or_name.yaml`](entities/script/cosmo/cosmo_get_room_id_or_name.yaml)
</details>

<details><summary><strong>Debug Persistent Notification</strong></summary>

**Entity ID: `script.debug_persistent_notification`**

> Create a persistent notification if debugging is turned on

- Fields:

```json
{
  "message": {
    "description": "The notification's message body",
    "example": "More detail about this thing",
    "selector": {
      "text": {
        "multiline": true
      }
    }
  },
  "notification_title": {
    "description": "The notification's title",
    "example": "Something has happened!",
    "selector": {
      "text": null
    }
  },
  "notification_id": {
    "description": "Optional ID for the persistent notification",
    "example": "important_thing_happened",
    "selector": {
      "text": null
    }
  }
}
```

- Mode: `parallel`

File: [`script/debug_persistent_notification.yaml`](entities/script/debug_persistent_notification.yaml)
</details>

<details><summary><strong>Dining Area | Set Lighting Based on Occupancy</strong></summary>

**Entity ID: `script.dining_area_set_lighting_based_on_occupancy`**

> Set dining area lighting based on current occupancy state

- Mode: `single`
- Variables:

```json
{
  "color_temp_kelvin": 2500,
  "modifier": "{{ states('sensor.lighting_modifier') | int(70) }}"
}
```
File: [`script/dining_area_set_lighting_based_on_occupancy.yaml`](entities/script/dining_area_set_lighting_based_on_occupancy.yaml)
</details>

<details><summary><strong>Air Purifier: Update Fan Speed</strong></summary>

**Entity ID: `script.air_purifier_update_fan_speed`**

> Update the air purifier fan speed based on the current air quality and other conditions

- Mode: `single`
- Variables:

```json
{
  "pm2_5": "{{ states('sensor.air_purifier_pm2_5') | float(0) }}",
  "quiet_mode": "{{ states('input_boolean.air_purifier_quiet_mode') | bool(false) }}",
  "current_speed": "{{ state_attr('fan.air_purifier', 'percentage') | int(0) }}"
}
```
File: [`script/fan/air_purifier/air_purifier_update_fan_speed.yaml`](entities/script/fan/air_purifier/air_purifier_update_fan_speed.yaml)
</details>

<details><summary><strong>Log Exception</strong></summary>

**Entity ID: `script.log_exception`**

> Log an exception, does not end the calling execution!

- Fields:

```json
{
  "calling_entity": {
    "description": "The entity that called this service",
    "required": true,
    "example": "automation.do_something",
    "selector": {
      "entity": null
    }
  },
  "message": {
    "description": "The message to be logged",
    "required": true,
    "example": "Something went wrong!",
    "selector": {
      "text": {
        "multiline": true
      }
    }
  }
}
```

- Mode: `parallel`
- Variables:

```json
{
  "entity_domain": "{{ calling_entity.split('.')[0] }}",
  "entity_id": "{{ calling_entity.split('.')[1] }}",
  "timestamp": "{{ now().strftime('%Y-%m-%d %H:%M:%S') }}",
  "formatted_message": "{% if \"\\n\" not in message.strip() and \"`\" not in message %}\n  {#- Plain text single line -#}\n  {{ \"`\" + message.strip() + \"`\" }}\n{% elif \"```\" in message %}\n  {#- Some type of code block -#}\n  {% if message.count(\"```\") >= 2 %}\n    {#- Valid, don't reformat -#}\n    {{ \"\\n\" + message.strip() }}\n  {% else -%}\n    {#- Invalid code block, wrap in triple-backticks -#}\n    {{ \"\\n```\\n\" + message.replace(\"`\", \"\\\\`\").strip() + \"\\n```\\n\" }}\n  {% endif %}\n{% else %}\n{{ message.strip() }}\n{% endif %}\n"
}
```
File: [`script/functions/log_exception.yaml`](entities/script/functions/log_exception.yaml)
</details>

<details><summary><strong>Run Dynamic Script</strong></summary>

**Entity ID: `script.run_dynamic_script`**

> Run a script, but the script is passed in as a literal argument

- Fields:

```json
{
  "actions": {
    "description": "A list of services/actions to run",
    "required": true,
    "example": "[\n  {\n    \"service\": \"script.turn_on\",\n    \"target\": {\n      \"entity_id\": \"script.debug_persistent_notification\"\n    },\n    \"data\": {}\n  },\n  {\n    \"service\": \"persistent_notification.create\",\n    \"target\": {},\n    \"data\": {\n      \"notification_title\": \"Sitting mode activated\",\n      \"message\": \"The office desk is now in sitting mode\",\n    }\n  }\n]\n",
    "selector": {
      "action": null
    }
  },
  "script_id": {
    "description": "The name of the script to run",
    "required": false,
    "selector": {
      "entity": {
        "domain": "script"
      }
    }
  },
  "suppress_debug_notifications": {
    "description": "If true, the debug notification(s) will not be shown",
    "required": false,
    "selector": {
      "boolean": null
    }
  }
}
```

- Mode: `parallel`
- Variables:

```json
{
  "suppress_debug_notifications": "{{ suppress_debug_notifications | default(false) }}"
}
```
File: [`script/functions/run_dynamic_script.yaml`](entities/script/functions/run_dynamic_script.yaml)
</details>

<details><summary><strong>State Manager | Attribute Timeout</strong></summary>

**Entity ID: `script.state_manager_attribute_timeout`**

> Timeout for "should be" on/off attributes of a state manager

- Fields:

```json
{
  "state_manager": {
    "description": "The state manager entity to reset attributes for",
    "required": true,
    "example": "var.will_s_office_state_manager",
    "selector": {
      "entity": {
        "domain": "var"
      }
    }
  }
}
```

- Mode: `parallel`
- Variables:

```json
{
  "cached_states": "{{\n  (state_attr(state_manager, \"entity_states_b64\") or \"e30=\")\n  | base64_decode\n  | from_json\n  | default({})\n}}",
  "target_area_id": "{{ area_id(state_manager) }}"
}
```
File: [`script/functions/state_manager/state_manager_attribute_timeout.yaml`](entities/script/functions/state_manager/state_manager_attribute_timeout.yaml)
</details>

<details><summary><strong>State Manager | Reset States</strong></summary>

**Entity ID: `script.state_manager_reset_states`**

> Reset the states of a state manager to the original states

- Fields:

```json
{
  "state_manager": {
    "description": "The state manager entity to reset attributes for",
    "required": true,
    "example": "var.will_s_office_state_manager",
    "selector": {
      "entity": {
        "domain": "var"
      }
    }
  }
}
```

- Mode: `parallel`
- Variables:

```json
{
  "target_area_id": "{{ area_id(state_manager) }}"
}
```
File: [`script/functions/state_manager/state_manager_reset_states.yaml`](entities/script/functions/state_manager/state_manager_reset_states.yaml)
</details>

<details><summary><strong>Target Git Branch: Set Options</strong></summary>

**Entity ID: `script.target_git_branch_set_options`**

> Set the options of input_select.target_git_branch to the current git branches

- Fields:

```json
{
  "update_remote_branches": {
    "description": "Update the remote branches sensor",
    "required": false,
    "selector": {
      "boolean": null
    }
  }
}
```

- Mode: `restart`

File: [`script/input_select/target_git_branch/target_git_branch_set_options.yaml`](entities/script/input_select/target_git_branch/target_git_branch_set_options.yaml)
</details>

<details><summary><strong>IR Blaster Topaz SR10 Issue Command</strong></summary>

**Entity ID: `script.ir_blaster_topaz_sr10_issue_command`**

> *No description provided*

- Fields:

```json
{
  "code": {
    "description": "The IR code to send",
    "example": "BjQjURFhAjLgAAHgBQsCfwYy4AoD4AEXBDICYQIyoAEBfwbgBQNAAUATQAHABwEyAkAvQAMBMgLAE0AHCU+bNCOiCDIC///gAgcCCDIC",
    "selector": {
      "text": null
    }
  },
  "delay_ms": {
    "description": "The delay in milliseconds to wait at the end of the script (ensures no overlap with other commands)",
    "example": "500",
    "default": 500,
    "selector": {
      "number": {
        "min": 0,
        "max": 1000,
        "unit_of_measurement": "milliseconds",
        "mode": "slider"
      }
    }
  },
  "extra_service_calls": {
    "description": "A list of extra service calls to make after the IR command has been sent",
    "required": false,
    "selector": {
      "action": null
    }
  }
}
```

- Mode: `queued`
- Variables:

```json
{
  "delay_ms": "{{ delay_ms | default(500) | int(500) }}",
  "true_response": {
    "value": true
  }
}
```
File: [`script/ir_blaster/topaz_sr10/ir_blaster_topaz_sr10_issue_command.yaml`](entities/script/ir_blaster/topaz_sr10/ir_blaster_topaz_sr10_issue_command.yaml)
</details>

<details><summary><strong>Kitchen | Set Lighting Based on Occupancy</strong></summary>

**Entity ID: `script.kitchen_set_lighting_based_on_occupancy`**

> Set kitchen lighting based on current occupancy state

- Mode: `single`
- Variables:

```json
{
  "kitchen_multiplier": "{{ 1 if now().hour >= 23 or now().hour < 7 else 2.5 }}",
  "modifier": "{{ states('sensor.lighting_modifier') | int(70) }}"
}
```
File: [`script/kitchen_set_lighting_based_on_occupancy.yaml`](entities/script/kitchen_set_lighting_based_on_occupancy.yaml)
</details>

<details><summary><strong>Topaz SR10: Turn Off</strong></summary>

**Entity ID: `script.topaz_sr10_turn_off`**

> Turn the Topaz SR10 off. Exists as a script because you can't have multi-step commands

- Mode: `single`

File: [`script/media_player/topaz_sr10/topaz_sr10_turn_off.yaml`](entities/script/media_player/topaz_sr10/topaz_sr10_turn_off.yaml)
</details>

<details><summary><strong>Topaz SR10: Volume Set</strong></summary>

**Entity ID: `script.topaz_sr10_volume_set`**

> Set the volume of the Topaz SR10 to a specific value

- Fields:

```json
{
  "volume_level": {
    "description": "The volume level to set the Topaz SR10 to; 0.0 - 1.0",
    "required": true,
    "example": "0.5",
    "selector": {
      "number": {
        "min": 0,
        "max": 1,
        "step": 0.01,
        "unit_of_measurement": "%"
      }
    }
  }
}
```

- Mode: `restart`

File: [`script/media_player/topaz_sr10/topaz_sr10_volume_set.yaml`](entities/script/media_player/topaz_sr10/topaz_sr10_volume_set.yaml)
</details>

<details><summary><strong>MtrxPi | Audio Visualiser: Set Colors</strong></summary>

**Entity ID: `script.mtrxpi_audio_visualiser_set_colors`**

> Helper to set the MtrxPi Audio Visualiser colors

- Fields:

```json
{
  "high_magnitude_color": {
    "description": "The color to use for the high magnitude",
    "example": "#FF0000",
    "required": false,
    "selector": {
      "color_rgb": null
    }
  },
  "low_magnitude_color": {
    "description": "The color to use for the low magnitude",
    "example": "#00FF00",
    "required": false,
    "selector": {
      "color_rgb": null
    }
  }
}
```

- Mode: `single`

File: [`script/mtrxpi/audio_visualiser/mtrxpi_audio_visualiser_set_colors.yaml`](entities/script/mtrxpi/audio_visualiser/mtrxpi_audio_visualiser_set_colors.yaml)
</details>

<details><summary><strong>MtrxPi: Queue Content</strong></summary>

**Entity ID: `script.mtrxpi_queue_content`**

> Add content to the queue with a priority

- Fields:

```json
{
  "id": {
    "description": "The ID of the content to add to the queue",
    "example": "raining-grid",
    "required": true,
    "selector": {
      "select": {
        "options": [
          "audio-visualiser",
          "clock",
          "gif-door-animated",
          "image-door-closed",
          "now-playing",
          "raining-grid",
          "snake",
          "sorter"
        ]
      }
    }
  },
  "priority": {
    "description": "The priority of the content in the queue. `\"clear\"` will remove the content from the queue if it exists. The higher the number, the lower the priority.",
    "example": "1",
    "required": false,
    "default": "clear",
    "selector": {
      "number": {
        "min": -1000,
        "max": 99999,
        "step": "any",
        "mode": "box"
      }
    }
  }
}
```

- Mode: `queued`
- Variables:

```json
{
  "id": "{{ id | default('') }}",
  "parameters": "{{ parameters | default({}) }}",
  "priority": "{{\n  priority\n  | default(\n    states(\"input_number.mtrxpi_\" ~ id.replace(\"-\", \"_\") ~ \"_queue_position\")\n    | default(None)\n  )\n}}"
}
```
File: [`script/mtrxpi/mtrxpi_queue_content.yaml`](entities/script/mtrxpi/mtrxpi_queue_content.yaml)
</details>

<details><summary><strong>Notify Vic</strong></summary>

**Entity ID: `script.notify_vic`**

> Send a notification to Vic's devices

- Fields:

```json
{
  "title": {
    "description": "The title of the notification",
    "example": "Something Important!",
    "default": " ",
    "selector": {
      "text": null
    }
  },
  "message": {
    "description": "The message body of the notification",
    "example": "A thing has happened, thought you ought to know",
    "required": true,
    "selector": {
      "text": {
        "multiline": true
      }
    }
  },
  "clear_notification": {
    "description": "Clear the persistent notification",
    "example": "true",
    "selector": {
      "boolean": null
    }
  },
  "notification_id": {
    "description": "Optional ID for the persistent notification",
    "example": "important_thing_happened",
    "selector": {
      "text": null
    }
  },
  "actions": {
    "description": "Optional actions for the phone notification",
    "example": "[{\"action\": \"URI\", \"title\": \"View More\", \"uri\": \"https://example.com\"}]",
    "selector": {
      "object": null
    }
  },
  "mobile_notification_icon": {
    "description": "Optional icon for the phone notification",
    "example": "mdi:alert",
    "selector": {
      "icon": {
        "placeholder": "mdi:bell"
      }
    }
  },
  "url": {
    "description": "URL to open when the notification is selected\nhttps://companion.home-assistant.io/docs/notifications/notifications-basic/#opening-a-url",
    "example": "/home-will/makerspace",
    "required": false,
    "selector": {
      "text": null
    }
  },
  "group": {
    "description": "Combine notifications together visually",
    "example": "example-notification-group",
    "required": false,
    "selector": {
      "text": null
    }
  }
}
```

- Mode: `queued`
- Variables:

```json
{
  "actions": "{{ actions | default([]) }}",
  "clear_notification": "{{\n  message | default('') == 'clear_notification' or\n  clear_notification | default(False) | bool(False)\n}}",
  "notification_id": "{% if clear_notification %}\n  {{ notification_id | default(None) }}\n{% else %}\n  {{ notification_id | default('notify_vic_' ~ now().strftime('%Y%m%d%H%M%S%f')) }}\n{% endif %}",
  "message": "{% if clear_notification %}\n  clear_notification\n{% else %}\n  {{ message | default(\"\") }}\n{% endif %}",
  "mobile_notification_icon": "{{ mobile_notification_icon | default('mdi:home-assistant') }}",
  "notif_title": "{{ title | default('Home Assistant') }}",
  "url": "{{ url | default('') }}",
  "group": "{{ group | default('') }}"
}
```
File: [`script/notify_vic.yaml`](entities/script/notify_vic.yaml)
</details>

<details><summary><strong>Notify Will</strong></summary>

**Entity ID: `script.notify_will`**

> Send a notification to Will's phone and the HA UI

- Fields:

```json
{
  "title": {
    "description": "The title of the notification",
    "example": "Something Important!",
    "default": " ",
    "selector": {
      "text": null
    }
  },
  "message": {
    "description": "The message body of the notification",
    "example": "A thing has happened, thought you ought to know",
    "required": true,
    "selector": {
      "text": {
        "multiline": true
      }
    }
  },
  "clear_notification": {
    "description": "Clear the persistent notification",
    "example": "true",
    "selector": {
      "boolean": null
    }
  },
  "notification_id": {
    "description": "Optional ID for the persistent notification",
    "example": "important_thing_happened",
    "selector": {
      "text": null
    }
  },
  "actions": {
    "description": "Optional actions for the phone notification",
    "example": "[{\"action\": \"URI\", \"title\": \"View More\", \"uri\": \"https://example.com\"}]",
    "selector": {
      "object": null
    }
  },
  "mobile_notification_icon": {
    "description": "Optional icon for the phone notification",
    "example": "mdi:alert",
    "selector": {
      "icon": {
        "placeholder": "mdi:bell"
      }
    }
  },
  "url": {
    "description": "URL to open when the notification is selected\nhttps://companion.home-assistant.io/docs/notifications/notifications-basic/#opening-a-url",
    "example": "/home-will/makerspace",
    "required": false,
    "selector": {
      "text": null
    }
  },
  "group": {
    "description": "Combine notifications together visually",
    "example": "example-notification-group",
    "required": false,
    "selector": {
      "text": null
    }
  },
  "sticky": {
    "description": "Whether to dismiss the notification upon selecting it or not",
    "required": false,
    "selector": {
      "boolean": null
    }
  },
  "persistent": {
    "description": "Block dismissing the notification via the \"Clear All\" button or when the device is locked",
    "required": false,
    "selector": {
      "boolean": null
    }
  },
  "image": {
    "description": "Optional image for the notification",
    "example": "/api/camera_proxy/camera.octoprint_camera",
    "required": false,
    "selector": {
      "text": null
    }
  }
}
```

- Mode: `queued`
- Variables:

```json
{
  "actions": "{{ actions | default([]) }}",
  "clear_notification": "{{\n  message | default('') == 'clear_notification' or\n  clear_notification | default(False) | bool(False)\n}}",
  "notification_id": "{% if clear_notification %}\n  {{ notification_id | default(None) }}\n{% else %}\n  {{ notification_id | default('notify_will_' ~ now().strftime('%Y%m%d%H%M%S%f')) }}\n{% endif %}",
  "message": "{% if clear_notification %}\n  clear_notification\n{% else %}\n  {{ message | default(\"\") }}\n{% endif %}",
  "mobile_notification_icon": "{{ mobile_notification_icon | default('mdi:home-assistant') }}",
  "notif_title": "{{ title | default('Home Assistant') }}",
  "url": "{{ url | default('') }}",
  "group": "{{ group | default('') }}",
  "sticky": "{{ sticky | default(false) }}",
  "persistent": "{{ persistent | default(false) }}",
  "image": "{{ image | default('') }}"
}
```
File: [`script/notify_will.yaml`](entities/script/notify_will.yaml)
</details>

<details><summary><strong>Office Desk: Set Position</strong></summary>

**Entity ID: `script.office_desk_set_position`**

> *No description provided*

- Fields:

```json
{
  "position": {
    "name": "Position",
    "description": "Position to set the desk to",
    "example": "50",
    "selector": {
      "number": {
        "min": 10,
        "max": 100,
        "step": 1
      }
    }
  }
}
```

- Mode: `restart`
- Variables:

```json
{
  "tolerance": 2
}
```
File: [`script/office_desk_set_position.yaml`](entities/script/office_desk_set_position.yaml)
</details>

<details><summary><strong>Office Desk: Sitting Mode</strong></summary>

**Entity ID: `script.office_desk_sitting_mode`**

> *No description provided*

- Mode: `single`

File: [`script/office_desk_sitting_mode.yaml`](entities/script/office_desk_sitting_mode.yaml)
</details>

<details><summary><strong>Office Desk: Standing Mode</strong></summary>

**Entity ID: `script.office_desk_standing_mode`**

> *No description provided*

- Mode: `single`

File: [`script/office_desk_standing_mode.yaml`](entities/script/office_desk_standing_mode.yaml)
</details>

<details><summary><strong>Office Desk: Stop Moving</strong></summary>

**Entity ID: `script.office_desk_stop_moving`**

> *No description provided*

- Mode: `restart`

File: [`script/office_desk_stop_moving.yaml`](entities/script/office_desk_stop_moving.yaml)
</details>

<details><summary><strong>Reset Next Bedroom Sunrise</strong></summary>

**Entity ID: `script.reset_next_bedroom_sunrise`**

> Set the next bedroom sunrise to tomorrow at the appropriate time (7:30 AM weekdays, 8:30 AM weekends)

- Mode: `single`

File: [`script/reset_next_bedroom_sunrise.yaml`](entities/script/reset_next_bedroom_sunrise.yaml)
</details>

<details><summary><strong>Send Bedroom Sunrise Notification</strong></summary>

**Entity ID: `script.send_bedroom_sunrise_notification`**

> Send sunrise notification with countdown timer to both phones

- Fields:

```json
{
  "clear_notification": {
    "description": "Clear the notification",
    "example": "true",
    "selector": {
      "boolean": null
    }
  }
}
```

- Mode: `single`
- Variables:

```json
{
  "clear_notification": "{{ clear_notification | default(False) | bool(False) }}"
}
```
File: [`script/send_bedroom_sunrise_notification.yaml`](entities/script/send_bedroom_sunrise_notification.yaml)
</details>

<details><summary><strong>GH Issue Create</strong></summary>

**Entity ID: `script.gh_issue_create`**

> Create a new issue on GitHub

- Fields:

```json
{
  "issue_title": {
    "name": "Issue Title",
    "description": "The title of the issue",
    "required": true,
    "selector": {
      "text": null
    }
  },
  "issue_labels": {
    "name": "Labels",
    "description": "Add one or more labels to the issue",
    "required": true,
    "selector": {
      "select": {
        "multiple": true,
        "options": [
          "bug",
          "chore",
          "feature-request",
          "refactor",
          "major",
          "minor",
          "patch",
          "tools"
        ]
      }
    }
  },
  "body": {
    "name": "Issue Body",
    "description": "The main body of the issue",
    "required": true,
    "selector": {
      "text": {
        "multiline": true
      }
    }
  },
  "assignee": {
    "name": "Assignee",
    "description": "Who to assign the issue to",
    "default": "worgarside",
    "selector": {
      "select": {
        "options": [
          "worgarside"
        ]
      }
    }
  },
  "repository": {
    "name": "Repository",
    "description": "The repo to open the issue in",
    "default": "home-assistant",
    "required": true,
    "selector": {
      "select": {
        "multiple": false,
        "options": [
          "github-config-files",
          "home-assistant",
          "home-assistant-appdaemon",
          "home-assistant-config-validator",
          "led-matrix-controller",
          "wg-scripts",
          "wg-utilities"
        ]
      }
    }
  }
}
```

- Mode: `queued`

File: [`script/shell_command/gh_cli/gh_issue_create.yaml`](entities/script/shell_command/gh_cli/gh_issue_create.yaml)
</details>

<details><summary><strong>Git Pull</strong></summary>

**Entity ID: `script.git_pull`**

> Pull the current Git branch

- Mode: `single`

File: [`script/shell_command/git/git_pull.yaml`](entities/script/shell_command/git/git_pull.yaml)
</details>

<details><summary><strong>ssh</strong></summary>

**Entity ID: `script.ssh`**

> Run a command on Pi

- Fields:

```json
{
  "command": {
    "description": "The command to run",
    "example": "cd wg-scripts && make update && make restart-all",
    "required": true,
    "selector": {
      "text": {
        "multiline": true
      }
    }
  },
  "host": {
    "description": "The host to run the command on",
    "example": "mtrxpi",
    "required": true,
    "selector": {
      "select": {
        "options": [
          "crtpi",
          "flmtpi",
          "mtrxpi",
          "octopi",
          "rtropi",
          "vsmppi"
        ]
      }
    }
  },
  "user": {
    "description": "The user to run the command as",
    "example": "pi",
    "default": "pi",
    "required": true,
    "selector": {
      "text": null
    }
  }
}
```

- Mode: `parallel`
- Variables:

```json
{
  "ip_addr_entity_id": "sensor.{{ host }}_local_ip_address",
  "prefix": "-o StrictHostKeyChecking=no -i /config/.ssh/{{ host }}"
}
```
File: [`script/ssh.yaml`](entities/script/ssh.yaml)
</details>

<details><summary><strong>Reset Reloadable Files Changed</strong></summary>

**Entity ID: `script.reset_reloadable_files_changed`**

> Fire a custom event to reset `sensor.system_reloadable_files_changed`

- Mode: `single`

File: [`script/system/reset_reloadable_files_changed.yaml`](entities/script/system/reset_reloadable_files_changed.yaml)
</details>

<details><summary><strong>Reset Restart Required Files Changed</strong></summary>

**Entity ID: `script.reset_restart_required_files_changed`**

> Fire a custom event to reset `sensor.system_restart_required_files_changed`

- Mode: `single`

File: [`script/system/reset_restart_required_files_changed.yaml`](entities/script/system/reset_restart_required_files_changed.yaml)
</details>

<details><summary><strong>Script Response Debugger</strong></summary>

**Entity ID: `script.script_response_debugger`**

> Wraps a script to log the response variable(s)

- Fields:

```json
{
  "script_name": {
    "description": "Name of the script to run",
    "required": true,
    "selector": {
      "entity": {
        "domain": "script"
      }
    }
  },
  "script_args": {
    "description": "Arguments to pass to the script (object)",
    "required": false,
    "selector": {
      "action": null
    }
  }
}
```

- Mode: `parallel`

File: [`script/system/script_response_debugger.yaml`](entities/script/system/script_response_debugger.yaml)
</details>

<details><summary><strong>Turn Off Physical Room</strong></summary>

**Entity ID: `script.turn_off_physical_room`**

> *No description provided*

- Fields:

```json
{
  "room": {
    "name": "Room",
    "description": "The room to turn off",
    "example": "office",
    "required": true,
    "selector": {
      "area": null
    }
  },
  "extra_service_calls": {
    "name": "Extra Service Calls",
    "description": "Extra services to call (default service is `homeassistant.turn_off`)",
    "default": [],
    "required": false,
    "example": "[\n  {\n    \"service_call\": \"script.turn_on\",\n    \"entity_id\": \"script.office_desk_sitting_mode\"\n  }\n]\n",
    "selector": {
      "action": null
    }
  }
}
```

- Mode: `queued`

File: [`script/turn_off_physical_room.yaml`](entities/script/turn_off_physical_room.yaml)
</details>

</details>

## Sensor

<details><summary><h3>Entities (6)</h3></summary>

<details><summary><strong>Hallway Radiator Temperature Derivative</strong></summary>

**Entity ID: `sensor.hallway_radiator_temperature_derivative`**

- Platform: `derivative`

File: [`sensor/hallway_radiator_temperature_derivative.yaml`](entities/sensor/hallway_radiator_temperature_derivative.yaml)
</details>

<details><summary><strong>Office Desk Occupied Cumulative Time</strong></summary>

**Entity ID: `sensor.binary_sensor.office_desk_occupied`**

- Platform: `history_stats`

File: [`sensor/office_desk_occupied_cumulative_time.yaml`](entities/sensor/office_desk_occupied_cumulative_time.yaml)
</details>

<details><summary><code>Office Desk Standing/Occupied Cumulative Time</code></summary>

**Entity ID: `sensor.binary_sensor.office_desk_standing_and_occupied`**

- Platform: `history_stats`

File: [`sensor/office_desk_standing_occupied_cumulative_time.yaml`](entities/sensor/office_desk_standing_occupied_cumulative_time.yaml)
</details>

<details><summary><code>sensor.plex_recently_added</code></summary>

- Platform: `plex_recently_added`

File: [`sensor/plex_recently_added.yaml`](entities/sensor/plex_recently_added.yaml)
</details>

<details><summary><code>sensor.time_date</code></summary>

- Platform: `time_date`

File: [`sensor/time_date.yaml`](entities/sensor/time_date.yaml)
</details>

<details><summary><strong>Wger | Will: Weight (Δ7d)</strong></summary>

**Entity ID: `sensor.sensor.wger_will_body_weight`**

- Platform: `statistics`

File: [`sensor/wger_will_weight_7d.yaml`](entities/sensor/wger_will_weight_7d.yaml)
</details>

</details>

## Shell Command

<details><summary><h3>Entities (20)</h3></summary>

<details><summary><code>shell_command.approve_pull_request</code></summary>

File: [`shell_command/approve_pull_request.yaml`](entities/shell_command/approve_pull_request.yaml)
</details>

<details><summary><code>shell_command.bash_subshell</code></summary>

File: [`shell_command/bash_subshell.yaml`](entities/shell_command/bash_subshell.yaml)
</details>

<details><summary><code>shell_command.checkout_git_branch</code></summary>

File: [`shell_command/checkout_git_branch.yaml`](entities/shell_command/checkout_git_branch.yaml)
</details>

<details><summary><code>shell_command.comment_on_pr</code></summary>

File: [`shell_command/comment_on_pr.yaml`](entities/shell_command/comment_on_pr.yaml)
</details>

<details><summary><code>shell_command.base64_decode_file</code></summary>

File: [`shell_command/file_operations/base64_decode_file.yaml`](entities/shell_command/file_operations/base64_decode_file.yaml)
</details>

<details><summary><code>shell_command.base64_encode_file</code></summary>

File: [`shell_command/file_operations/base64_encode_file.yaml`](entities/shell_command/file_operations/base64_encode_file.yaml)
</details>

<details><summary><code>shell_command.delete_file</code></summary>

File: [`shell_command/file_operations/delete_file.yaml`](entities/shell_command/file_operations/delete_file.yaml)
</details>

<details><summary><code>shell_command.read_file</code></summary>

File: [`shell_command/file_operations/read_file.yaml`](entities/shell_command/file_operations/read_file.yaml)
</details>

<details><summary><code>shell_command.write_file</code></summary>

File: [`shell_command/file_operations/write_file.yaml`](entities/shell_command/file_operations/write_file.yaml)
</details>

<details><summary><code>shell_command.get_gh_cli</code></summary>

File: [`shell_command/get_gh_cli.yaml`](entities/shell_command/get_gh_cli.yaml)
</details>

<details><summary><code>shell_command.gh</code></summary>

File: [`shell_command/gh.yaml`](entities/shell_command/gh.yaml)
</details>

<details><summary><code>shell_command.ls</code></summary>

File: [`shell_command/ls.yaml`](entities/shell_command/ls.yaml)
</details>

<details><summary><code>shell_command.mark_pr_as_ready_for_review</code></summary>

File: [`shell_command/mark_pr_as_ready_for_review.yaml`](entities/shell_command/mark_pr_as_ready_for_review.yaml)
</details>

<details><summary><code>shell_command.python_subshell</code></summary>

File: [`shell_command/python_subshell.yaml`](entities/shell_command/python_subshell.yaml)
</details>

<details><summary><code>shell_command.run_custom_file_1</code></summary>

File: [`shell_command/run_custom_file_1.yaml`](entities/shell_command/run_custom_file_1.yaml)
</details>

<details><summary><code>shell_command.run_custom_file_2</code></summary>

File: [`shell_command/run_custom_file_2.yaml`](entities/shell_command/run_custom_file_2.yaml)
</details>

<details><summary><code>shell_command.run_custom_file_3</code></summary>

File: [`shell_command/run_custom_file_3.yaml`](entities/shell_command/run_custom_file_3.yaml)
</details>

<details><summary><code>shell_command.set_pr_auto_merge</code></summary>

File: [`shell_command/set_pr_auto_merge.yaml`](entities/shell_command/set_pr_auto_merge.yaml)
</details>

<details><summary><code>shell_command.ssh</code></summary>

File: [`shell_command/ssh.yaml`](entities/shell_command/ssh.yaml)
</details>

<details><summary><code>shell_command.toggle_pr_label</code></summary>

File: [`shell_command/toggle_pr_label.yaml`](entities/shell_command/toggle_pr_label.yaml)
</details>

</details>

## Switch

<details><summary><h3>Entities (4)</h3></summary>

<details><summary><strong>Central Heating</strong></summary>

**Entity ID: `switch.central_heating`**

File: [`switch/central_heating.yaml`](entities/switch/central_heating.yaml)
</details>

<details><summary><strong>Hot Water</strong></summary>

**Entity ID: `switch.hot_water`**

File: [`switch/hot_water.yaml`](entities/switch/hot_water.yaml)
</details>

<details><summary><strong>MtrxPi Power</strong></summary>

**Entity ID: `switch.mtrxpi_power`**

File: [`switch/mtrxpi_power.yaml`](entities/switch/mtrxpi_power.yaml)
</details>

<details><summary><strong>Prusa i3 MK3 Power</strong></summary>

**Entity ID: `switch.prusa_i3_mk3_power`**

File: [`switch/prusa_i3_mk3_power.yaml`](entities/switch/prusa_i3_mk3_power.yaml)
</details>

</details>

## Template

<details><summary><h3>Entities (77)</h3></summary>

<details><summary><strong>Bank Holiday</strong></summary>

**Entity ID: `binary_sensor.bank_holiday`**

- Icon: [`mdi:calendar-star`](https://pictogrammers.com/library/mdi/icon/calendar-star/)

File: [`template/binary_sensor/bank_holiday.yaml`](entities/template/binary_sensor/bank_holiday.yaml)
</details>

<details><summary><strong>Before Midday</strong></summary>

**Entity ID: `binary_sensor.before_midday`**

- Icon: [`mdi:clock-time-twelve-outline`](https://pictogrammers.com/library/mdi/icon/clock-time-twelve-outline/)

File: [`template/binary_sensor/before_midday.yaml`](entities/template/binary_sensor/before_midday.yaml)
</details>

<details><summary><strong>Office Desk Occupied</strong></summary>

**Entity ID: `binary_sensor.office_desk_occupied`**

- Icon: [`mdi:chair-rolling`](https://pictogrammers.com/library/mdi/icon/chair-rolling/)

File: [`template/binary_sensor/office_desk_occupied.yaml`](entities/template/binary_sensor/office_desk_occupied.yaml)
</details>

<details><summary><strong>Office Desk Standing and Occupied</strong></summary>

**Entity ID: `binary_sensor.office_desk_standing_and_occupied`**

- Icon:

```jinja
{% if this.state == "on" %}
  mdi:human-handsup
{% else %}
  mdi:human-handsdown
{% endif %}

```
File: [`template/binary_sensor/office_desk_standing_and_occupied.yaml`](entities/template/binary_sensor/office_desk_standing_and_occupied.yaml)
</details>

<details><summary><strong>Office Desk Standing Mode</strong></summary>

**Entity ID: `binary_sensor.office_desk_standing_mode`**

- Icon:

```jinja
{% if this.state == "on" %}
  phu:desk-stand-alt
{% else %}
  phu:desk-sit-alt
{% endif %}

```
File: [`template/binary_sensor/office_desk_standing_mode.yaml`](entities/template/binary_sensor/office_desk_standing_mode.yaml)
</details>

<details><summary><strong>Quiet Hours</strong></summary>

**Entity ID: `binary_sensor.quiet_hours`**

File: [`template/binary_sensor/quiet_hours.yaml`](entities/template/binary_sensor/quiet_hours.yaml)
</details>

<details><summary><strong>CRTPi Online</strong></summary>

**Entity ID: `binary_sensor.crtpi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/crtpi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/crtpi_online.yaml)
</details>

<details><summary><strong>GrowPi Online</strong></summary>

**Entity ID: `binary_sensor.growpi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/growpi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/growpi_online.yaml)
</details>

<details><summary><strong>MtrxPi Online</strong></summary>

**Entity ID: `binary_sensor.mtrxpi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/mtrxpi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/mtrxpi_online.yaml)
</details>

<details><summary><strong>OctoPi Online</strong></summary>

**Entity ID: `binary_sensor.octopi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/octopi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/octopi_online.yaml)
</details>

<details><summary><strong>RtroPi Online</strong></summary>

**Entity ID: `binary_sensor.rtropi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/rtropi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/rtropi_online.yaml)
</details>

<details><summary><strong>VSMPPi Online</strong></summary>

**Entity ID: `binary_sensor.vsmppi_online`**

- Icon: [`mdi:raspberry-pi`](https://pictogrammers.com/library/mdi/icon/raspberry-pi/)

File: [`template/binary_sensor/raspberry_pi_online/vsmppi_online.yaml`](entities/template/binary_sensor/raspberry_pi_online/vsmppi_online.yaml)
</details>

<details><summary><strong>Vic at Work</strong></summary>

**Entity ID: `binary_sensor.vic_at_work`**

- Icon: [`mdi:badge-account`](https://pictogrammers.com/library/mdi/icon/badge-account/)

File: [`template/binary_sensor/vic_at_work.yaml`](entities/template/binary_sensor/vic_at_work.yaml)
</details>

<details><summary><strong>Weekday</strong></summary>

**Entity ID: `binary_sensor.weekday`**

- Icon: [`mdi:calendar-week`](https://pictogrammers.com/library/mdi/icon/calendar-week/)

File: [`template/binary_sensor/weekday.yaml`](entities/template/binary_sensor/weekday.yaml)
</details>

<details><summary><strong>Weekend</strong></summary>

**Entity ID: `binary_sensor.weekend`**

- Icon: [`mdi:calendar-weekend`](https://pictogrammers.com/library/mdi/icon/calendar-weekend/)

File: [`template/binary_sensor/weekend.yaml`](entities/template/binary_sensor/weekend.yaml)
</details>

<details><summary><strong>Will's MacBook Pro Docked</strong></summary>

**Entity ID: `binary_sensor.will_s_macbook_pro_docked`**

- Icon: [`mdi:monitor-share`](https://pictogrammers.com/library/mdi/icon/monitor-share/)

File: [`template/binary_sensor/will_s_macbook_pro_docked.yaml`](entities/template/binary_sensor/will_s_macbook_pro_docked.yaml)
</details>

<details><summary><strong>Work MacBook Pro Docked</strong></summary>

**Entity ID: `binary_sensor.work_macbook_pro_docked`**

- Icon: [`mdi:monitor-share`](https://pictogrammers.com/library/mdi/icon/monitor-share/)

File: [`template/binary_sensor/work_macbook_pro_docked.yaml`](entities/template/binary_sensor/work_macbook_pro_docked.yaml)
</details>

<details><summary><strong>Prusa i3 Thumbnail</strong></summary>

**Entity ID: `template.prusa_i3_thumbnail`**

- Icon: [`mdi:monitor-screenshot`](https://pictogrammers.com/library/mdi/icon/monitor-screenshot/)

File: [`template/image/prusa_i3_thumbnail.yaml`](entities/template/image/prusa_i3_thumbnail.yaml)
</details>

<details><summary><strong>AppDaemon CPU Usage</strong></summary>

**Entity ID: `sensor.appdaemon_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/appdaemon_cpu_usage.yaml`](entities/template/sensor/addon_stats/appdaemon_cpu_usage.yaml)
</details>

<details><summary><strong>AppDaemon Memory Usage</strong></summary>

**Entity ID: `sensor.appdaemon_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/appdaemon_memory_usage.yaml`](entities/template/sensor/addon_stats/appdaemon_memory_usage.yaml)
</details>

<details><summary><strong>CastSponsorSkip CPU Usage</strong></summary>

**Entity ID: `sensor.castsponsorskip_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/castsponsorskip_cpu_usage.yaml`](entities/template/sensor/addon_stats/castsponsorskip_cpu_usage.yaml)
</details>

<details><summary><strong>CastSponsorSkip Memory Usage</strong></summary>

**Entity ID: `sensor.castsponsorskip_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/castsponsorskip_memory_usage.yaml`](entities/template/sensor/addon_stats/castsponsorskip_memory_usage.yaml)
</details>

<details><summary><strong>ESPHome Add-on CPU Usage</strong></summary>

**Entity ID: `sensor.esphome_add_on_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/esphome_add_on_cpu_usage.yaml`](entities/template/sensor/addon_stats/esphome_add_on_cpu_usage.yaml)
</details>

<details><summary><strong>ESPHome Add-on Memory Usage</strong></summary>

**Entity ID: `sensor.esphome_add_on_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/esphome_add_on_memory_usage.yaml`](entities/template/sensor/addon_stats/esphome_add_on_memory_usage.yaml)
</details>

<details><summary><strong>Item Warehouse API CPU Usage</strong></summary>

**Entity ID: `sensor.item_warehouse_api_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/item_warehouse_api_cpu_usage.yaml`](entities/template/sensor/addon_stats/item_warehouse_api_cpu_usage.yaml)
</details>

<details><summary><strong>Item Warehouse API Memory Usage</strong></summary>

**Entity ID: `sensor.item_warehouse_api_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/item_warehouse_api_memory_usage.yaml`](entities/template/sensor/addon_stats/item_warehouse_api_memory_usage.yaml)
</details>

<details><summary><strong>Item Warehouse Website CPU Usage</strong></summary>

**Entity ID: `sensor.item_warehouse_website_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/item_warehouse_website_cpu_usage.yaml`](entities/template/sensor/addon_stats/item_warehouse_website_cpu_usage.yaml)
</details>

<details><summary><strong>Item Warehouse Website Memory Usage</strong></summary>

**Entity ID: `sensor.item_warehouse_website_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/item_warehouse_website_memory_usage.yaml`](entities/template/sensor/addon_stats/item_warehouse_website_memory_usage.yaml)
</details>

<details><summary><strong>Terminal & SSH Add-on CPU Usage</strong></summary>

**Entity ID: `sensor.terminal_ssh_add_on_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/terminal_ssh_add_on_cpu_usage.yaml`](entities/template/sensor/addon_stats/terminal_ssh_add_on_cpu_usage.yaml)
</details>

<details><summary><strong>Terminal & SSH Add-on Memory Usage</strong></summary>

**Entity ID: `sensor.terminal_ssh_add_on_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/terminal_ssh_add_on_memory_usage.yaml`](entities/template/sensor/addon_stats/terminal_ssh_add_on_memory_usage.yaml)
</details>

<details><summary><strong>Visual Studio Code Add-on CPU Usage</strong></summary>

**Entity ID: `sensor.visual_studio_code_add_on_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/visual_studio_code_add_on_cpu_usage.yaml`](entities/template/sensor/addon_stats/visual_studio_code_add_on_cpu_usage.yaml)
</details>

<details><summary><strong>Visual Studio Code Add-on Memory Usage</strong></summary>

**Entity ID: `sensor.visual_studio_code_add_on_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/visual_studio_code_add_on_memory_usage.yaml`](entities/template/sensor/addon_stats/visual_studio_code_add_on_memory_usage.yaml)
</details>

<details><summary><strong>YAS-209 Bridge CPU Usage</strong></summary>

**Entity ID: `sensor.yas_209_bridge_cpu_usage`**

- Icon: [`mdi:cpu-32-bit`](https://pictogrammers.com/library/mdi/icon/cpu-32-bit/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/yas_209_bridge_cpu_usage.yaml`](entities/template/sensor/addon_stats/yas_209_bridge_cpu_usage.yaml)
</details>

<details><summary><strong>YAS-209 Bridge Memory Usage</strong></summary>

**Entity ID: `sensor.yas_209_bridge_memory_usage`**

- Icon: [`mdi:memory`](https://pictogrammers.com/library/mdi/icon/memory/)
- Unit Of Measurement: %

File: [`template/sensor/addon_stats/yas_209_bridge_memory_usage.yaml`](entities/template/sensor/addon_stats/yas_209_bridge_memory_usage.yaml)
</details>

<details><summary><strong>Address Line 1</strong></summary>

**Entity ID: `sensor.address_line_1`**

- Icon: [`mdi:map-marker`](https://pictogrammers.com/library/mdi/icon/map-marker/)

File: [`template/sensor/address_line_1.yaml`](entities/template/sensor/address_line_1.yaml)
</details>

<details><summary><strong>Air Purifier Fan Speed</strong></summary>

**Entity ID: `sensor.air_purifier_fan_speed`**

- Icon:

```jinja
{% if not states("fan.air_purifier") | bool(false) %}
  mdi:fan-off
{% elif state_attr('fan.air_purifier', 'mode') == 'auto' %}
  mdi:fan-auto
{% elif state_attr('fan.air_purifier', 'mode') == 'manual' %}
  {% if state_attr('fan.air_purifier', 'percentage') == 25 %}
    mdi:fan-speed-1
  {% elif state_attr('fan.air_purifier', 'percentage') == 50 %}
    mdi:fan-speed-2
  {% elif state_attr('fan.air_purifier', 'percentage') == 75 %}
    mdi:fan-speed-3
  {% else %}
    mdi:fan
  {% endif %}
{% else %}
  mdi:fan
{% endif %}
```
File: [`template/sensor/air_purifier_fan_speed.yaml`](entities/template/sensor/air_purifier_fan_speed.yaml)
</details>

<details><summary><strong>Current Hour</strong></summary>

**Entity ID: `sensor.current_hour`**

- Icon:

```jinja
{%
  set hours = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
  ] * 2
%}
mdi:clock-time-{{ hours[this.state | int(12) - 1] }}-outline
```
File: [`template/sensor/current_hour.yaml`](entities/template/sensor/current_hour.yaml)
</details>

<details><summary><strong>Vic and Will Distance</strong></summary>

**Entity ID: `sensor.vic_and_will_distance`**

- Icon: [`mdi:map-marker-distance`](https://pictogrammers.com/library/mdi/icon/map-marker-distance/)
- Unit Of Measurement: `miles`

File: [`template/sensor/distance/vic_and_will_distance.yaml`](entities/template/sensor/distance/vic_and_will_distance.yaml)
</details>

<details><summary><strong>Vic Distance from Home</strong></summary>

**Entity ID: `sensor.vic_distance_from_home`**

- Icon: [`mdi:map-marker-distance`](https://pictogrammers.com/library/mdi/icon/map-marker-distance/)
- Unit Of Measurement: `miles`

File: [`template/sensor/distance/vic_distance_from_home.yaml`](entities/template/sensor/distance/vic_distance_from_home.yaml)
</details>

<details><summary><strong>Will Distance from Home</strong></summary>

**Entity ID: `sensor.will_distance_from_home`**

- Icon: [`mdi:map-marker-distance`](https://pictogrammers.com/library/mdi/icon/map-marker-distance/)
- Unit Of Measurement: `miles`

File: [`template/sensor/distance/will_distance_from_home.yaml`](entities/template/sensor/distance/will_distance_from_home.yaml)
</details>

<details><summary><strong>Low Batteries</strong></summary>

**Entity ID: `sensor.low_batteries`**

- Icon:

```jinja
{% set ns = namespace(total=0, count=0, average=0) %}
{% for value in this.attributes.entities | default([]) | map(attribute="state") %}
  {% set ns.total = ns.total + value %}
  {% set ns.count = ns.count + 1 %}
  {% set ns.average = ns.total / ns.count %}
{% endfor %}
{% if ns.average > 0 %}
  mdi:battery-{{ ns.average | round(-1) | int(10) or 10 }}
{% else %}
  mdi:battery
{% endif %}

```
File: [`template/sensor/entity_counts/low_batteries.yaml`](entities/template/sensor/entity_counts/low_batteries.yaml)
</details>

<details><summary><strong>Unavailable Entities</strong></summary>

**Entity ID: `sensor.unavailable_entities`**

- Icon: [`mdi:lan-disconnect`](https://pictogrammers.com/library/mdi/icon/lan-disconnect/)

File: [`template/sensor/entity_counts/unavailable_entities.yaml`](entities/template/sensor/entity_counts/unavailable_entities.yaml)
</details>

<details><summary><strong>HiFi System: Media Metadata</strong></summary>

**Entity ID: `sensor.hifi_system_media_metadata`**

File: [`template/sensor/hifi_system_media_metadata.yaml`](entities/template/sensor/hifi_system_media_metadata.yaml)
</details>

<details><summary><strong>Lighting Modifier</strong></summary>

**Entity ID: `sensor.lighting_modifier`**

- Icon: [`mdi:brightness-percent`](https://pictogrammers.com/library/mdi/icon/brightness-percent/)
- Unit Of Measurement: %

File: [`template/sensor/lighting_modifier.yaml`](entities/template/sensor/lighting_modifier.yaml)
</details>

<details><summary><strong>Sun Elevation</strong></summary>

**Entity ID: `sensor.sun_elevation`**

- Unit Of Measurement: °

File: [`template/sensor/nature/sun_elevation.yaml`](entities/template/sensor/nature/sun_elevation.yaml)
</details>

<details><summary><strong>Time of Day</strong></summary>

**Entity ID: `sensor.time_of_day`**

- Icon:

```jinja
{{
  {
    "Morning": "mdi:weather-sunset-up",
    "Afternoon": "mdi:weather-sunny",
    "Evening": "mdi:weather-sunset-down",
    "Sunrise": "mdi:weather-sunset-up",
    "Sunset": "mdi:weather-sunset-down",
    "Twilight": "mdi:weather-sunset",
    "Dawn": "mdi:weather-sunset-up",
    "Dusk": "mdi:weather-sunset-down",
    "Night": "mdi:weather-night",
    "Unknown": "mdi:help-rhombus-outline"
  }.get(this.state, "mdi:help-rhombus-outline")
}}
```
File: [`template/sensor/nature/time_of_day.yaml`](entities/template/sensor/nature/time_of_day.yaml)
</details>

<details><summary><strong>Tomorrow.io: Cloud Base</strong></summary>

**Entity ID: `sensor.tomorrow_io_cloud_base`**

- Icon: [`mdi:cloud-arrow-down-outline`](https://pictogrammers.com/library/mdi/icon/cloud-arrow-down-outline/)
- Unit Of Measurement: `km`

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_cloud_base.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_cloud_base.yaml)
</details>

<details><summary><strong>Tomorrow.io: Cloud Ceiling</strong></summary>

**Entity ID: `sensor.tomorrow_io_cloud_ceiling`**

- Icon: [`mdi:cloud-arrow-up-outline`](https://pictogrammers.com/library/mdi/icon/cloud-arrow-up-outline/)
- Unit Of Measurement: `km`

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_cloud_ceiling.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_cloud_ceiling.yaml)
</details>

<details><summary><strong>Tomorrow.io: Cloud Cover</strong></summary>

**Entity ID: `sensor.tomorrow_io_cloud_cover`**

- Icon: [`mdi:cloud-percent-outline`](https://pictogrammers.com/library/mdi/icon/cloud-percent-outline/)
- Unit Of Measurement: %

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_cloud_cover.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_cloud_cover.yaml)
</details>

<details><summary><strong>Tomorrow.io: Dew Point</strong></summary>

**Entity ID: `sensor.tomorrow_io_dew_point`**

- Icon: [`mdi:water-thermometer-outline`](https://pictogrammers.com/library/mdi/icon/water-thermometer-outline/)
- Unit Of Measurement: °C

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_dew_point.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_dew_point.yaml)
</details>

<details><summary><strong>Tomorrow.io: Freezing Rain Intensity</strong></summary>

**Entity ID: `sensor.tomorrow_io_freezing_rain_intensity`**

- Icon: [`mdi:weather-snowy-rainy`](https://pictogrammers.com/library/mdi/icon/weather-snowy-rainy/)
- Unit Of Measurement: mm/hr

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_freezing_rain_intensity.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_freezing_rain_intensity.yaml)
</details>

<details><summary><strong>Tomorrow.io: Humidity</strong></summary>

**Entity ID: `sensor.tomorrow_io_humidity`**

- Icon: [`mdi:cloud-percent-outline`](https://pictogrammers.com/library/mdi/icon/cloud-percent-outline/)
- Unit Of Measurement: %

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_humidity.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_humidity.yaml)
</details>

<details><summary><strong>Tomorrow.io: Precipitation Probability</strong></summary>

**Entity ID: `sensor.tomorrow_io_precipitation_probability`**

- Icon: [`mdi:cloud-percent-outline`](https://pictogrammers.com/library/mdi/icon/cloud-percent-outline/)
- Unit Of Measurement: %

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_precipitation_probability.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_precipitation_probability.yaml)
</details>

<details><summary><strong>Tomorrow.io: Pressure Surface Level</strong></summary>

**Entity ID: `sensor.tomorrow_io_pressure_surface_level`**

- Icon: [`mdi:gauge`](https://pictogrammers.com/library/mdi/icon/gauge/)
- Unit Of Measurement: hPa

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_pressure_surface_level.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_pressure_surface_level.yaml)
</details>

<details><summary><strong>Tomorrow.io: Rain Intensity</strong></summary>

**Entity ID: `sensor.tomorrow_io_rain_intensity`**

- Icon:

```jinja
{% if this.state | float(1) > 0 %}
  mdi:weather-rainy
{% else %}
  mdi:cloud-outline
{% endif %}
```

- Unit Of Measurement: mm/hr

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_rain_intensity.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_rain_intensity.yaml)
</details>

<details><summary><strong>Tomorrow.io: Sleet Intensity</strong></summary>

**Entity ID: `sensor.tomorrow_io_sleet_intensity`**

- Icon: [`mdi:weather-snowy-rainy`](https://pictogrammers.com/library/mdi/icon/weather-snowy-rainy/)
- Unit Of Measurement: mm/hr

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_sleet_intensity.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_sleet_intensity.yaml)
</details>

<details><summary><strong>Tomorrow.io: Snow Intensity</strong></summary>

**Entity ID: `sensor.tomorrow_io_snow_intensity`**

- Icon: [`mdi:weather-snowy`](https://pictogrammers.com/library/mdi/icon/weather-snowy/)
- Unit Of Measurement: mm/hr

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_snow_intensity.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_snow_intensity.yaml)
</details>

<details><summary><strong>Tomorrow.io: Temperature</strong></summary>

**Entity ID: `sensor.tomorrow_io_temperature`**

- Icon: [`mdi:thermometer`](https://pictogrammers.com/library/mdi/icon/thermometer/)
- Unit Of Measurement: °C

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_temperature.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_temperature.yaml)
</details>

<details><summary><strong>Tomorrow.io: Temperature Apparent</strong></summary>

**Entity ID: `sensor.tomorrow_io_temperature_apparent`**

- Icon: [`mdi:thermometer`](https://pictogrammers.com/library/mdi/icon/thermometer/)
- Unit Of Measurement: °C

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_temperature_apparent.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_temperature_apparent.yaml)
</details>

<details><summary><strong>Tomorrow.io: UV Health Concern</strong></summary>

**Entity ID: `sensor.tomorrow_io_uv_health_concern`**

- Icon: [`mdi:sun-wireless-outline`](https://pictogrammers.com/library/mdi/icon/sun-wireless-outline/)

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_uv_health_concern.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_uv_health_concern.yaml)
</details>

<details><summary><strong>Tomorrow.io: UV Index</strong></summary>

**Entity ID: `sensor.tomorrow_io_uv_index`**

- Icon: [`mdi:sun-wireless-outline`](https://pictogrammers.com/library/mdi/icon/sun-wireless-outline/)

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_uv_index.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_uv_index.yaml)
</details>

<details><summary><strong>Tomorrow.io: Visibility</strong></summary>

**Entity ID: `sensor.tomorrow_io_visibility`**

- Icon: [`mdi:weather-hazy`](https://pictogrammers.com/library/mdi/icon/weather-hazy/)
- Unit Of Measurement: `km`

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_visibility.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_visibility.yaml)
</details>

<details><summary><strong>Tomorrow.io: Weather Code</strong></summary>

**Entity ID: `sensor.tomorrow_io_weather_code`**

- Icon:

```jinja
{{
  {
    "Unknown": "mdi:help-rhombus-outline",
    "Clear, Sunny": "mdi:weather-sunny",
    "Mostly Clear": "mdi:weather-sunny",
    "Partly Cloudy": "mdi:weather-partly-cloudy",
    "Mostly Cloudy": "mdi:weather-cloudy",
    "Cloudy": "mdi:weather-cloudy",
    "Fog": "mdi:weather-fog",
    "Light Fog": "mdi:weather-fog",
    "Drizzle": "mdi:weather-rainy",
    "Rain": "mdi:weather-pouring",
    "Light Rain": "mdi:weather-rainy",
    "Heavy Rain": "mdi:weather-pouring",
    "Snow": "mdi:weather-snowy",
    "Flurries": "mdi:weather-snowy",
    "Light Snow": "mdi:weather-snowy",
    "Heavy Snow": "mdi:weather-snowy",
    "Freezing Drizzle": "mdi:weather-snowy",
    "Freezing Rain": "mdi:weather-snowy",
    "Light Freezing Rain": "mdi:weather-snowy",
    "Heavy Freezing Rain": "mdi:weather-snowy",
    "Ice Pellets": "mdi:weather-snowy",
    "Heavy Ice Pellets": "mdi:weather-snowy",
    "Light Ice Pellets": "mdi:weather-snowy",
    "Thunderstorm": "mdi:weather-lightning"
  }.get(this.state, "mdi:help-rhombus-outline")
}}
```
File: [`template/sensor/nature/tomorrow_io/tomorrow_io_weather_code.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_weather_code.yaml)
</details>

<details><summary><strong>Tomorrow.io: Wind Direction</strong></summary>

**Entity ID: `sensor.tomorrow_io_wind_direction`**

- Icon: [`mdi:compass-outline`](https://pictogrammers.com/library/mdi/icon/compass-outline/)
- Unit Of Measurement: °

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_wind_direction.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_wind_direction.yaml)
</details>

<details><summary><strong>Tomorrow.io: Wind Gust</strong></summary>

**Entity ID: `sensor.tomorrow_io_wind_gust`**

- Icon: [`mdi:weather-windy`](https://pictogrammers.com/library/mdi/icon/weather-windy/)
- Unit Of Measurement: m/s

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_wind_gust.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_wind_gust.yaml)
</details>

<details><summary><strong>Tomorrow.io: Wind Speed</strong></summary>

**Entity ID: `sensor.tomorrow_io_wind_speed`**

- Icon: [`mdi:weather-windy`](https://pictogrammers.com/library/mdi/icon/weather-windy/)
- Unit Of Measurement: m/s

File: [`template/sensor/nature/tomorrow_io/tomorrow_io_wind_speed.yaml`](entities/template/sensor/nature/tomorrow_io/tomorrow_io_wind_speed.yaml)
</details>

<details><summary><strong>Office Desk Standing Mode Percentage</strong></summary>

**Entity ID: `sensor.office_desk_standing_mode_percentage`**

- Icon: [`mdi:percent`](https://pictogrammers.com/library/mdi/icon/percent/)
- Unit Of Measurement: %

File: [`template/sensor/office_desk/office_desk_standing_mode_percentage.yaml`](entities/template/sensor/office_desk/office_desk_standing_mode_percentage.yaml)
</details>

<details><summary><strong>Office Desk Standing Time Remaining</strong></summary>

**Entity ID: `sensor.office_desk_standing_time_remaining`**

- Icon:

```jinja
{% if this.state | float(default=0.0) > 0 %}
  mdi:timer-sand
{% else %}
  mdi:timer-sand-complete
{% endif %}

```

- Unit Of Measurement: `min`

File: [`template/sensor/office_desk/office_desk_standing_time_remaining.yaml`](entities/template/sensor/office_desk/office_desk_standing_time_remaining.yaml)
</details>

<details><summary><strong>Person Cosmo</strong></summary>

**Entity ID: `sensor.person_cosmo`**

File: [`template/sensor/person/person_cosmo.yaml`](entities/template/sensor/person/person_cosmo.yaml)
</details>

<details><summary><strong>Spotify Will Garside Media Album Artwork Internal URL</strong></summary>

**Entity ID: `sensor.spotify_will_garside_media_album_artwork_internal_url`**

File: [`template/sensor/spotify/spotify_will_garside_media_album_artwork_internal_url.yaml`](entities/template/sensor/spotify/spotify_will_garside_media_album_artwork_internal_url.yaml)
</details>

<details><summary><strong>Spotify Will Garside Media Album Name</strong></summary>

**Entity ID: `sensor.spotify_will_garside_media_album_name`**

File: [`template/sensor/spotify/spotify_will_garside_media_album_name.yaml`](entities/template/sensor/spotify/spotify_will_garside_media_album_name.yaml)
</details>

<details><summary><strong>Spotify Will Garside Media Artist</strong></summary>

**Entity ID: `sensor.spotify_will_garside_media_artist`**

File: [`template/sensor/spotify/spotify_will_garside_media_artist.yaml`](entities/template/sensor/spotify/spotify_will_garside_media_artist.yaml)
</details>

<details><summary><strong>Spotify Will Garside Media Title</strong></summary>

**Entity ID: `sensor.spotify_will_garside_media_title`**

File: [`template/sensor/spotify/spotify_will_garside_media_title.yaml`](entities/template/sensor/spotify/spotify_will_garside_media_title.yaml)
</details>

<details><summary><strong>Vic's Electric Blanket Level</strong></summary>

**Entity ID: `sensor.vic_s_electric_blanket_level`**

- Icon:

```jinja
{% if not is_state("switch.vic_s_electric_blanket", "on") %}
  mdi:numeric-0-circle
{% else %}
  {% set power = states("sensor.vic_s_electric_blanket_power") | float(0) %}
  {% if power < 1 %}
    mdi:numeric-0-circle
  {% elif power >= 20 and power < 30 %}
    mdi:numeric-1-circle
  {% elif power >= 30 and power < 60 %}
    mdi:numeric-2-circle
  {% elif power >= 60 %}
    mdi:numeric-3-circle
  {% else %}
    mdi:help-circle
  {% endif %}
{% endif %}
```
File: [`template/sensor/vic_s_electric_blanket_level.yaml`](entities/template/sensor/vic_s_electric_blanket_level.yaml)
</details>

<details><summary><strong>Vic's Office Fan Speed</strong></summary>

**Entity ID: `sensor.vic_s_office_fan_speed`**

- Icon:

```jinja
{% if not states("fan.vic_s_office_fan") | bool(false) %}
  mdi:fan-off
{% elif is_state("fan.vic_s_office_fan", "off") %}
  mdi:fan-off
{% elif state_attr("fan.vic_s_office_fan", "percentage") | int(0) == 0 %}
  mdi:fan-off
{% elif state_attr("fan.vic_s_office_fan", "percentage") | int(0) <= 25 %}
  mdi:fan-speed-1
{% elif state_attr("fan.vic_s_office_fan", "percentage") | int(0) <= 50 %}
  mdi:fan-speed-2
{% elif state_attr("fan.vic_s_office_fan", "percentage") | int(0) <= 75 %}
  mdi:fan-speed-3
{% else %}
  mdi:fan
{% endif %}
```

- Unit Of Measurement: %

File: [`template/sensor/vic_s_office_fan_speed.yaml`](entities/template/sensor/vic_s_office_fan_speed.yaml)
</details>

<details><summary><strong>Will's Electric Blanket Level</strong></summary>

**Entity ID: `sensor.will_s_electric_blanket_level`**

- Icon:

```jinja
{% if not is_state("switch.will_s_electric_blanket", "on") %}
  mdi:numeric-0-circle
{% else %}
  {% set power = states("sensor.will_s_electric_blanket_power") | float(0) %}
  {% if power < 1 %}
    mdi:numeric-0-circle
  {% elif power >= 20 and power < 30 %}
    mdi:numeric-1-circle
  {% elif power >= 30 and power < 60 %}
    mdi:numeric-2-circle
   {% elif power >= 60 %}
    mdi:numeric-3-circle
  {% else %}
    mdi:help-circle
  {% endif %}
{% endif %}
```
File: [`template/sensor/will_s_electric_blanket_level.yaml`](entities/template/sensor/will_s_electric_blanket_level.yaml)
</details>

<details><summary><strong>Will's Office Fan Speed</strong></summary>

**Entity ID: `sensor.will_s_office_fan_speed`**

- Icon:

```jinja
{% if not states("fan.will_s_office_fan") | bool(false) %}
  mdi:fan-off
{% elif is_state("fan.will_s_office_fan", "off") %}
  mdi:fan-off
{% elif state_attr("fan.will_s_office_fan", "percentage") | int(0) == 0 %}
  mdi:fan-off
{% elif state_attr("fan.will_s_office_fan", "percentage") | int(0) <= 25 %}
  mdi:fan-speed-1
{% elif state_attr("fan.will_s_office_fan", "percentage") | int(0) <= 50 %}
  mdi:fan-speed-2
{% elif state_attr("fan.will_s_office_fan", "percentage") | int(0) <= 75 %}
  mdi:fan-speed-3
{% else %}
  mdi:fan
{% endif %}
```

- Unit Of Measurement: %

File: [`template/sensor/will_s_office_fan_speed.yaml`](entities/template/sensor/will_s_office_fan_speed.yaml)
</details>

</details>

## Template

<details><summary><h3>Entities (11)</h3></summary>

<details><summary><strong>Apollo PLT 1B | Begonia: Last Online</strong></summary>

**Entity ID: `template.apollo_plt_1b_begonia_last_online`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`template_triggered/sensor/apollo/apollo_plt_1b_begonia_last_online.yaml`](entities/template_triggered/sensor/apollo/apollo_plt_1b_begonia_last_online.yaml)
</details>

<details><summary><strong>Apollo PLT 1B | Coleus: Last Online</strong></summary>

**Entity ID: `template.apollo_plt_1b_coleus_last_online`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`template_triggered/sensor/apollo/apollo_plt_1b_coleus_last_online.yaml`](entities/template_triggered/sensor/apollo/apollo_plt_1b_coleus_last_online.yaml)
</details>

<details><summary><strong>Apollo PLT 1B | Monstera: Last Online</strong></summary>

**Entity ID: `template.apollo_plt_1b_monstera_last_online`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`template_triggered/sensor/apollo/apollo_plt_1b_monstera_last_online.yaml`](entities/template_triggered/sensor/apollo/apollo_plt_1b_monstera_last_online.yaml)
</details>

<details><summary><strong>Apollo PLT 1B | Spider Plant: Last Online</strong></summary>

**Entity ID: `template.apollo_plt_1b_spider_plant_last_online`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`template_triggered/sensor/apollo/apollo_plt_1b_spider_plant_last_online.yaml`](entities/template_triggered/sensor/apollo/apollo_plt_1b_spider_plant_last_online.yaml)
</details>

<details><summary><strong>Cosmo Room Lookup</strong></summary>

**Entity ID: `template.cosmo_room_lookup`**

- Icon: [`mdi:floor-plan`](https://pictogrammers.com/library/mdi/icon/floor-plan/)

File: [`template_triggered/sensor/cosmo_room_lookup.yaml`](entities/template_triggered/sensor/cosmo_room_lookup.yaml)
</details>

<details><summary><strong>Cube | Active Face</strong></summary>

**Entity ID: `template.cube_active_face`**

- Icon: `mdi:dice-{{ trigger.event.data.args.activated_face }}`

File: [`template_triggered/sensor/cube_active_face.yaml`](entities/template_triggered/sensor/cube_active_face.yaml)
</details>

<details><summary><strong>Cube | Latest Event</strong></summary>

**Entity ID: `template.cube_latest_event`**

- Icon: [`mdi:history`](https://pictogrammers.com/library/mdi/icon/history/)

File: [`template_triggered/sensor/cube_latest_event.yaml`](entities/template_triggered/sensor/cube_latest_event.yaml)
</details>

<details><summary><strong>System: Reloadable Files Changed</strong></summary>

**Entity ID: `template.system_reloadable_files_changed`**

- Icon:

```jinja
{% if this.state | int(default=0) > 0 %}
  mdi:reload-alert
{% else %}
  mdi:reload
{% endif %}

```
File: [`template_triggered/sensor/system_reloadable_files_changed.yaml`](entities/template_triggered/sensor/system_reloadable_files_changed.yaml)
</details>

<details><summary><strong>System: Restart Required Files Changed</strong></summary>

**Entity ID: `template.system_restart_required_files_changed`**

- Icon:

```jinja
{% if this.state | int(default=0) > 0 %}
  mdi:restart-alert
{% else %}
  mdi:restart
{% endif %}

```
File: [`template_triggered/sensor/system_restart_required_files_changed.yaml`](entities/template_triggered/sensor/system_restart_required_files_changed.yaml)
</details>

<details><summary><strong>Topaz SR10 Active Child</strong></summary>

**Entity ID: `template.topaz_sr10_active_child`**

File: [`template_triggered/sensor/topaz_sr10_active_child.yaml`](entities/template_triggered/sensor/topaz_sr10_active_child.yaml)
</details>

<details><summary><strong>Will's YAS-209 Bridge Input</strong></summary>

**Entity ID: `template.will_s_yas_209_bridge_input`**

- Icon: [`mdi:soundbar`](https://pictogrammers.com/library/mdi/icon/soundbar/)

File: [`template_triggered/sensor/will_s_yas_209_bridge_input.yaml`](entities/template_triggered/sensor/will_s_yas_209_bridge_input.yaml)
</details>

</details>

## Utility Meter

<details><summary><h3>Entities (8)</h3></summary>

<details><summary><strong>OVO | Electricity: Daily Cost</strong></summary>

**Entity ID: `utility_meter.ovo_electricity_daily_cost`**

File: [`utility_meter/ovo_electricity_daily_cost.yaml`](entities/utility_meter/ovo_electricity_daily_cost.yaml)
</details>

<details><summary><strong>OVO | Electricity: Daily Usage</strong></summary>

**Entity ID: `utility_meter.ovo_electricity_daily_usage`**

File: [`utility_meter/ovo_electricity_daily_usage.yaml`](entities/utility_meter/ovo_electricity_daily_usage.yaml)
</details>

<details><summary><strong>OVO | Electricity: Monthly Cost</strong></summary>

**Entity ID: `utility_meter.ovo_electricity_monthly_cost`**

File: [`utility_meter/ovo_electricity_monthly_cost.yaml`](entities/utility_meter/ovo_electricity_monthly_cost.yaml)
</details>

<details><summary><strong>OVO | Electricity: Monthly Usage</strong></summary>

**Entity ID: `utility_meter.ovo_electricity_monthly_usage`**

File: [`utility_meter/ovo_electricity_monthly_usage.yaml`](entities/utility_meter/ovo_electricity_monthly_usage.yaml)
</details>

<details><summary><strong>OVO | Gas: Daily Cost</strong></summary>

**Entity ID: `utility_meter.ovo_gas_daily_cost`**

File: [`utility_meter/ovo_gas_daily_cost.yaml`](entities/utility_meter/ovo_gas_daily_cost.yaml)
</details>

<details><summary><strong>OVO | Gas: Daily Usage</strong></summary>

**Entity ID: `utility_meter.ovo_gas_daily_usage`**

File: [`utility_meter/ovo_gas_daily_usage.yaml`](entities/utility_meter/ovo_gas_daily_usage.yaml)
</details>

<details><summary><strong>OVO | Gas: Monthly Cost</strong></summary>

**Entity ID: `utility_meter.ovo_gas_monthly_cost`**

File: [`utility_meter/ovo_gas_monthly_cost.yaml`](entities/utility_meter/ovo_gas_monthly_cost.yaml)
</details>

<details><summary><strong>OVO | Gas: Monthly Usage</strong></summary>

**Entity ID: `utility_meter.ovo_gas_monthly_usage`**

File: [`utility_meter/ovo_gas_monthly_usage.yaml`](entities/utility_meter/ovo_gas_monthly_usage.yaml)
</details>

</details>

## Var

<details><summary><h3>Entities (18)</h3></summary>

<details><summary><strong>Auto-Reload Queue</strong></summary>

**Entity ID: `var.auto_reload_queue`**

- Icon: [`mdi:reload`](https://pictogrammers.com/library/mdi/icon/reload/)
- Unit Of Measurement: `domains`

File: [`var/auto_reload_queue.yaml`](entities/var/auto_reload_queue.yaml)
</details>

<details><summary><strong>Auto-Save Amount</strong></summary>

**Entity ID: `var.auto_save_amount`**

- Icon: [`mdi:piggy-bank`](https://pictogrammers.com/library/mdi/icon/piggy-bank/)
- Unit Of Measurement: GBP

File: [`var/auto_save_amount.yaml`](entities/var/auto_save_amount.yaml)
</details>

<details><summary><strong>Auto-Save Cumulative Total</strong></summary>

**Entity ID: `var.auto_save_cumulative_total`**

- Icon: [`mdi:chart-timeline-variant-shimmer`](https://pictogrammers.com/library/mdi/icon/chart-timeline-variant-shimmer/)
- Unit Of Measurement: GBP

File: [`var/auto_save_cumulative_total.yaml`](entities/var/auto_save_cumulative_total.yaml)
</details>

<details><summary><strong>Central Heating Last Action</strong></summary>

**Entity ID: `var.central_heating_last_action`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`var/central_heating_last_action.yaml`](entities/var/central_heating_last_action.yaml)
</details>

<details><summary><strong>Current AppDaemon Branch</strong></summary>

**Entity ID: `var.current_appdaemon_branch`**

- Icon: [`mdi:source-branch-plus`](https://pictogrammers.com/library/mdi/icon/source-branch-plus/)

File: [`var/current_appdaemon_branch.yaml`](entities/var/current_appdaemon_branch.yaml)
</details>

<details><summary><strong>Current AppDaemon Ref</strong></summary>

**Entity ID: `var.current_appdaemon_ref`**

- Icon: [`mdi:application-parentheses`](https://pictogrammers.com/library/mdi/icon/application-parentheses/)

File: [`var/current_appdaemon_ref.yaml`](entities/var/current_appdaemon_ref.yaml)
</details>

<details><summary><strong>Hot Water Last Action</strong></summary>

**Entity ID: `var.hot_water_last_action`**

- Icon: [`mdi:clock-outline`](https://pictogrammers.com/library/mdi/icon/clock-outline/)

File: [`var/hot_water_last_action.yaml`](entities/var/hot_water_last_action.yaml)
</details>

<details><summary><strong>Lounge | Occupancy Automation States Pre-Exercise Mode</strong></summary>

**Entity ID: `var.lounge_occupancy_automation_state_pre_exercise_mode`**

File: [`var/lounge_occupancy_automation_state_pre_exercise_mode.yaml`](entities/var/lounge_occupancy_automation_state_pre_exercise_mode.yaml)
</details>

<details><summary><strong>Spotify Tempo (Will)</strong></summary>

**Entity ID: `var.spotify_tempo_will`**

- Icon: [`mdi:metronome`](https://pictogrammers.com/library/mdi/icon/metronome/)
- Unit Of Measurement: BPM

File: [`var/spotify/spotify_tempo_will.yaml`](entities/var/spotify/spotify_tempo_will.yaml)
</details>

<details><summary><strong>Pixel Now Playing (Tasker)</strong></summary>

**Entity ID: `var.tasker_pixel_now_playing`**

- Icon: [`mdi:cellphone-play`](https://pictogrammers.com/library/mdi/icon/cellphone-play/)

File: [`var/tasker/tasker_pixel_now_playing.yaml`](entities/var/tasker/tasker_pixel_now_playing.yaml)
</details>

<details><summary><strong>Amex Balance</strong></summary>

**Entity ID: `var.truelayer_balance_amex`**

- Icon: si:americanexpress
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_amex.yaml`](entities/var/truelayer/truelayer_balance_amex.yaml)
</details>

<details><summary><strong>HSBC Current Account Balance</strong></summary>

**Entity ID: `var.truelayer_balance_hsbc_current_account`**

- Icon: [`mdi:bank`](https://pictogrammers.com/library/mdi/icon/bank/)
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_hsbc_current_account.yaml`](entities/var/truelayer/truelayer_balance_hsbc_current_account.yaml)
</details>

<details><summary><strong>Santander Current Account Balance</strong></summary>

**Entity ID: `var.truelayer_balance_santander_current_account`**

- Icon: [`mdi:bank`](https://pictogrammers.com/library/mdi/icon/bank/)
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_santander_current_account.yaml`](entities/var/truelayer/truelayer_balance_santander_current_account.yaml)
</details>

<details><summary><strong>Santander Savings Account Balance</strong></summary>

**Entity ID: `var.truelayer_balance_santander_savings_account`**

- Icon: [`mdi:piggy-bank`](https://pictogrammers.com/library/mdi/icon/piggy-bank/)
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_santander_savings_account.yaml`](entities/var/truelayer/truelayer_balance_santander_savings_account.yaml)
</details>

<details><summary><strong>Starling Current Account Balance</strong></summary>

**Entity ID: `var.truelayer_balance_starling_current_account`**

- Icon: [`mdi:bank`](https://pictogrammers.com/library/mdi/icon/bank/)
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_starling_current_account.yaml`](entities/var/truelayer/truelayer_balance_starling_current_account.yaml)
</details>

<details><summary><strong>Starling Joint Account Balance</strong></summary>

**Entity ID: `var.truelayer_balance_starling_joint_account`**

- Icon: [`mdi:bank`](https://pictogrammers.com/library/mdi/icon/bank/)
- Unit Of Measurement: GBP

File: [`var/truelayer/truelayer_balance_starling_joint_account.yaml`](entities/var/truelayer/truelayer_balance_starling_joint_account.yaml)
</details>

<details><summary><strong>Vic's Office State Manager</strong></summary>

**Entity ID: `var.vic_s_office_state_manager`**

- Icon: [`mdi:database-settings-outline`](https://pictogrammers.com/library/mdi/icon/database-settings-outline/)

File: [`var/vic_s_office_state_manager.yaml`](entities/var/vic_s_office_state_manager.yaml)
</details>

<details><summary><strong>Will's Office State Manager</strong></summary>

**Entity ID: `var.will_s_office_state_manager`**

- Icon: [`mdi:database-settings-outline`](https://pictogrammers.com/library/mdi/icon/database-settings-outline/)

File: [`var/will_s_office_state_manager.yaml`](entities/var/will_s_office_state_manager.yaml)
</details>

</details>
