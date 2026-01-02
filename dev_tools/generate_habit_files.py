"""Generate habit tracking files for additional numbered habits."""

from __future__ import annotations

import argparse
from pathlib import Path

REPO_PATH = Path(__file__).parents[1]

if REPO_PATH.name != "home-assistant" or not REPO_PATH.is_dir():
    raise RuntimeError(
        "Unable to locate the `home-assistant` repository."
        f" Current path is: {REPO_PATH!s}",
    )


def generate_binary_habit_files(user: str, total_count: int) -> None:
    """Generate all required files for binary habits (done/not done).

    Args:
        user: User name (e.g., 'will').
        total_count: Total number of binary habits desired.
    """
    print(f"Generating {total_count} binary habit(s)...")

    for num in range(1, total_count + 1):
        print(f"  Generating files for binary habit {num}...")

        # Input boolean
        boolean_path = (
            REPO_PATH
            / "entities"
            / "input_boolean"
            / "habit"
            / f"{user}_habit_binary_{num}.yaml"
        )
        boolean_path.parent.mkdir(parents=True, exist_ok=True)
        boolean_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}"

icon: mdi:checkbox-marked-circle-outline
""",
        )

        # Input text name
        text_name_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_binary_{num}_name.yaml"
        )
        text_name_path.parent.mkdir(parents=True, exist_ok=True)
        text_name_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Name"

icon: mdi:format-text

max: 255
""",
        )

        # Input text icon (on state)
        text_icon_on_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_binary_{num}_icon_on.yaml"
        )
        text_icon_on_path.parent.mkdir(parents=True, exist_ok=True)
        text_icon_on_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Icon (On)"

icon: mdi:emoticon

max: 255
""",
        )

        # Input text icon (off state)
        text_icon_off_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_binary_{num}_icon_off.yaml"
        )
        text_icon_off_path.parent.mkdir(parents=True, exist_ok=True)
        text_icon_off_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Icon (Off)"

icon: mdi:emoticon

max: 255
""",
        )

        # Input datetime reminder time
        datetime_path = (
            REPO_PATH
            / "entities"
            / "input_datetime"
            / "habit"
            / f"{user}_habit_binary_{num}_reminder_time.yaml"
        )
        datetime_path.parent.mkdir(parents=True, exist_ok=True)
        datetime_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Reminder Time"

has_date: false

has_time: true

icon: mdi:clock-outline
""",
        )

        # Reminder automation
        reminder_automation_path = (
            REPO_PATH
            / "entities"
            / "automation"
            / "input_datetime"
            / "habit"
            / f"{user}_habit_binary_{num}"
            / "reminder.yaml"
        )
        reminder_automation_path.parent.mkdir(parents=True, exist_ok=True)
        reminder_template = """---
alias: /input-datetime/habit/XXXUSERXXX-habit-binary-XXXNUMXXX/reminder

id: input_datetime_habit_XXXUSERXXX_habit_binary_XXXNUMXXX_reminder

description: Remind to log XXXUSERTITLEXXX's binary habit XXXNUMXXX at configured reminder time

mode: single

trigger:
  - platform: time
    at: input_datetime.XXXUSERXXX_habit_binary_XXXNUMXXX_reminder_time

condition: "{{{{ not is_state('input_boolean.XXXUSERXXX_habit_binary_XXXNUMXXX', 'on') }}}}"

variables:
  habit_name: "{{{{ states('input_text.XXXUSERXXX_habit_binary_XXXNUMXXX_name') | default('Habit Binary XXXNUMXXX') }}}}"

action:
  - service: script.notify_XXXUSERXXX
    data:
      title: "Habit Reminder"
      message: "Don't forget to mark {{{{ habit_name }}}} as complete!"
      notification_id: XXXUSERXXX_habit_binary_XXXNUMXXX_reminder
      url: /home-XXXUSERXXX/mood-habits
"""  # noqa: E501
        reminder_content = (
            reminder_template
            .replace("{{{{", "{{")
            .replace("}}}}", "}}")
            .replace("XXXUSERXXX", user)
            .replace("XXXNUMXXX", str(num))
            .replace("XXXUSERTITLEXXX", user.title())
        )
        reminder_automation_path.write_text(reminder_content)

        # SQL sensor for streak
        sql_sensor_path = (
            REPO_PATH
            / "entities"
            / "sensor"
            / "sql"
            / "habit"
            / f"{user}_habit_binary_{num}_streak.yaml"
        )
        sql_sensor_path.parent.mkdir(parents=True, exist_ok=True)
        sql_sensor_template = """---
name: {user_title} | Habit Binary {num} Streak

unique_id: {user}_habit_binary_{num}_streak

icon: mdi:fire

query: >-
  WITH daily_last_states AS (
    SELECT
      DATE(to_timestamp(states.last_updated_ts)) as check_date,
      states.state,
      states.last_updated_ts,
      ROW_NUMBER() OVER (
          PARTITION BY DATE(to_timestamp(states.last_updated_ts))
          ORDER BY states.last_updated_ts DESC
      ) as rn
    FROM states
    INNER JOIN states_meta ON states.metadata_id = states_meta.metadata_id
    WHERE states_meta.entity_id = 'input_boolean.{user}_habit_binary_{num}'
      AND states.last_updated_ts >= EXTRACT(EPOCH FROM (CURRENT_DATE - INTERVAL '365 days'))
      AND DATE(to_timestamp(states.last_updated_ts)) < CURRENT_DATE
  ),
  valid_dates AS (
    SELECT DISTINCT check_date
    FROM daily_last_states
    WHERE rn = 1
      AND state = 'on'
  ),
  ordered_dates AS (
    SELECT
      check_date,
      (CURRENT_DATE - 1) - check_date as days_ago,
      ROW_NUMBER() OVER (ORDER BY check_date DESC) as rn
    FROM valid_dates
    ORDER BY check_date DESC
  ),
  consecutive_groups AS (
    SELECT
      check_date,
      days_ago,
      rn,
      days_ago - rn + 1 as grp
    FROM ordered_dates
  )
  SELECT COUNT(*)::integer as streak
  FROM consecutive_groups
  WHERE grp = (SELECT grp FROM consecutive_groups WHERE days_ago = 0 LIMIT 1)

column: streak
"""
        sql_sensor_path.write_text(
            sql_sensor_template.format(user=user, user_title=user.title(), num=num),
        )

        print(f"    ✓ Generated files for binary habit {num}")


def generate_countable_habit_files(user: str, total_count: int) -> None:
    """Generate all required files for countable habits (can be done multiple times per day).

    Args:
        user: User name (e.g., 'will').
        total_count: Total number of countable habits desired.
    """
    print(f"Generating {total_count} countable habit(s)...")

    for num in range(1, total_count + 1):
        print(f"  Generating files for countable habit {num}...")

        # Input number
        number_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_countable_{num}.yaml"
        )
        number_path.parent.mkdir(parents=True, exist_ok=True)
        number_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}"

icon: mdi:counter

min: 0

max: 100

step: 1

mode: box
""",
        )

        # Input text name
        text_name_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_countable_{num}_name.yaml"
        )
        text_name_path.parent.mkdir(parents=True, exist_ok=True)
        text_name_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Name"

icon: mdi:format-text

max: 255
""",
        )

        # Input text icon (zero state)
        text_icon_zero_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_countable_{num}_icon_zero.yaml"
        )
        text_icon_zero_path.parent.mkdir(parents=True, exist_ok=True)
        text_icon_zero_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Icon (Zero)"

icon: mdi:emoticon

max: 255
""",
        )

        # Input text icon (active state)
        text_icon_active_path = (
            REPO_PATH
            / "entities"
            / "input_text"
            / "habit"
            / f"{user}_habit_countable_{num}_icon_active.yaml"
        )
        text_icon_active_path.parent.mkdir(parents=True, exist_ok=True)
        text_icon_active_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Icon (Active)"

icon: mdi:emoticon

max: 255
""",
        )

        # Input datetime reminder time
        datetime_path = (
            REPO_PATH
            / "entities"
            / "input_datetime"
            / "habit"
            / f"{user}_habit_countable_{num}_reminder_time.yaml"
        )
        datetime_path.parent.mkdir(parents=True, exist_ok=True)
        datetime_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Reminder Time"

has_date: false

has_time: true

icon: mdi:clock-outline
""",
        )

        # Reminder automation
        reminder_automation_path = (
            REPO_PATH
            / "entities"
            / "automation"
            / "input_datetime"
            / "habit"
            / f"{user}_habit_countable_{num}"
            / "reminder.yaml"
        )
        reminder_automation_path.parent.mkdir(parents=True, exist_ok=True)
        reminder_template = """---
alias: /input-datetime/habit/XXXUSERXXX-habit-countable-XXXNUMXXX/reminder

id: input_datetime_habit_XXXUSERXXX_habit_countable_XXXNUMXXX_reminder

description: Remind to log XXXUSERTITLEXXX's countable habit XXXNUMXXX at configured reminder time

mode: single

trigger:
  - platform: time
    at: input_datetime.XXXUSERXXX_habit_countable_XXXNUMXXX_reminder_time

condition: "{{{{ states('input_number.XXXUSERXXX_habit_countable_XXXNUMXXX') | int(0) == 0 }}}}"

variables:
  habit_name: >-
    {{{{ states('input_text.XXXUSERXXX_habit_countable_XXXNUMXXX_name') | default('Habit Countable XXXNUMXXX') }}}}

action:
  - service: script.notify_XXXUSERXXX
    data:
      title: "Habit Reminder"
      message: "Don't forget to track {{{{ habit_name }}}}!"
      notification_id: XXXUSERXXX_habit_countable_XXXNUMXXX_reminder
      url: /home-XXXUSERXXX/mood-habits
"""
        reminder_content = (
            reminder_template
            .replace("{{{{", "{{")
            .replace("}}}}", "}}")
            .replace("XXXUSERXXX", user)
            .replace("XXXNUMXXX", str(num))
            .replace("XXXUSERTITLEXXX", user.title())
        )
        reminder_automation_path.write_text(reminder_content)

        print(f"    ✓ Generated files for countable habit {num}")


def generate_habit_template_sensors(user: str) -> None:
    """Generate high-level template sensors for habit tracking.

    Args:
        user: User name (e.g., 'will').
    """
    print(f"Generating high-level habit template sensors for {user}...")

    # Binary habits count sensor
    binary_count_path = (
        REPO_PATH
        / "entities"
        / "template"
        / "sensor"
        / "habit"
        / f"{user}_habits_binary_count.yaml"
    )
    binary_count_path.parent.mkdir(parents=True, exist_ok=True)
    binary_count_path.write_text(
        f"""---
name: {user.title()} | Habits Binary Count

unique_id: {user}_habits_binary_count

icon: mdi:toggle-switch

state: >-
  {{% set ns = namespace(count=0) %}}
  {{% for i in range(1, 999) %}}
    {{%-
      if not has_value("input_boolean.{user}_habit_binary_" ~ i) or
        states("input_text.{user}_habit_binary_" ~ i ~ "_name")
        in ["", "unknown"]
    -%}}
      {{%- break %}}
    {{%- endif -%}}
    {{% set ns.count = i %}}
  {{% endfor %}}
  {{{{ ns.count }}}}
""",
    )

    # Countable habits count sensor
    countable_count_path = (
        REPO_PATH
        / "entities"
        / "template"
        / "sensor"
        / "habit"
        / f"{user}_habits_countable_count.yaml"
    )
    countable_count_path.parent.mkdir(parents=True, exist_ok=True)
    countable_count_path.write_text(
        f"""---
name: {user.title()} | Habits Countable Count

unique_id: {user}_habits_countable_count

icon: mdi:numeric

state: >-
  {{% set ns = namespace(count=0) %}}
  {{% for i in range(1, 999) %}}
    {{%-
      if not has_value("input_number.{user}_habit_countable_" ~ i) or
        states("input_text.{user}_habit_countable_" ~ i ~ "_name") in ["", "unknown"]
    -%}}
      {{%- break %}}
    {{%- endif -%}}
    {{% set ns.count = i %}}
  {{% endfor %}}
  {{{{ ns.count }}}}
""",
    )

    # Total habits count sensor
    total_count_path = (
        REPO_PATH
        / "entities"
        / "template"
        / "sensor"
        / "habit"
        / f"{user}_habits_total_count.yaml"
    )
    total_count_path.parent.mkdir(parents=True, exist_ok=True)
    total_count_path.write_text(
        f"""---
name: {user.title()} | Habits Total Count

unique_id: {user}_habits_total_count

icon: mdi:counter

state: >-
  {{{{
    states('sensor.{user}_habits_binary_count') | int(0) +
    states('sensor.{user}_habits_countable_count') | int(0)
  }}}}
""",
    )

    print(f"  ✓ Generated high-level habit template sensors for {user}")


def main() -> None:
    """Run the habit file generator."""
    parser = argparse.ArgumentParser(
        description="Generate habit tracking files for numbered habits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_habit_files.py --user=will --binary 3
  python generate_habit_files.py --user=will --countable 2
  python generate_habit_files.py --user=will --binary --countable 5
        """,
    )
    parser.add_argument(
        "--user",
        required=True,
        help="User name (e.g., 'will')",
    )
    parser.add_argument(
        "--binary",
        action="store_true",
        help="Generate binary habits",
    )
    parser.add_argument(
        "--countable",
        action="store_true",
        help="Generate countable habits",
    )
    parser.add_argument(
        "--mood",
        action="store_true",
        help="Generate mood tracking files",
    )
    parser.add_argument(
        "count",
        type=int,
        nargs="?",
        help="Total number of habits desired (required if --binary or --countable is specified)",
    )

    args = parser.parse_args()

    if not args.binary and not args.countable and not args.mood:
        parser.error(
            "At least one of --binary, --countable, or --mood must be specified",
        )

    if (args.binary or args.countable) and args.count is None:
        parser.error("Count is required when --binary or --countable is specified")

    if args.count is not None and args.count < 1:
        parser.error("Count must be a positive integer")

    user = args.user.lower()

    if args.binary:
        generate_binary_habit_files(user, args.count)

    if args.countable:
        generate_countable_habit_files(user, args.count)

    if args.binary or args.countable:
        generate_habit_template_sensors(user)

    if args.mood:
        generate_mood_files(user)

    print("\n✓ Generation complete")


def generate_mood_files(user: str) -> None:
    """Generate all required files for mood tracking.

    Args:
        user: User name (e.g., 'will').
    """
    print(f"Generating mood files for {user}...")

    # Input select for mood
    mood_select_path = REPO_PATH / "entities" / "input_select" / f"{user}_mood_today.yaml"
    mood_select_path.parent.mkdir(parents=True, exist_ok=True)
    mood_select_path.write_text(
        f"""---
icon: mdi:emoticon-happy

name: {user.title()} | Mood Today

options:
  - Not Set
  - Very Low
  - Low
  - Okay
  - Good
  - Great
""",
    )

    # Input text for mood note
    mood_note_path = REPO_PATH / "entities" / "input_text" / f"{user}_mood_note.yaml"
    mood_note_path.parent.mkdir(parents=True, exist_ok=True)
    mood_note_path.write_text(
        f"""---
name: {user.title()} | Mood Note

icon: mdi:text

max: 255
""",
    )

    # Automation to reset mood selection daily
    mood_reset_automation_path = (
        REPO_PATH
        / "entities"
        / "automation"
        / "input_select"
        / user
        / "mood_today"
        / "reset_daily.yaml"
    )
    mood_reset_automation_path.parent.mkdir(parents=True, exist_ok=True)
    mood_reset_automation_path.write_text(
        f"""---
alias: /input-select/{user}/mood-today/reset-daily

id: input_select_{user}_mood_today_reset_daily

description: Reset mood selection at midnight

mode: single

trigger:
  - platform: time
    at: "00:00:00"

action:
  - service: input_select.select_option
    target:
      entity_id: input_select.{user}_mood_today
    data:
      option: Not Set
""",
    )

    # Automation to reset mood note daily
    mood_note_reset_automation_path = (
        REPO_PATH
        / "entities"
        / "automation"
        / "input_text"
        / user
        / "mood_note"
        / "reset_daily.yaml"
    )
    mood_note_reset_automation_path.parent.mkdir(parents=True, exist_ok=True)
    mood_note_reset_automation_path.write_text(
        f"""---
alias: /input-text/{user}/mood-note/reset-daily

id: input_text_{user}_mood_note_reset_daily

description: Clear mood note at midnight

mode: single

trigger:
  - platform: time
    at: "00:00:00"

action:
  - service: input_text.set_value
    target:
      entity_id: input_text.{user}_mood_note
    data:
      value: ""
""",
    )

    # SQL sensor for mood streak
    mood_streak_sensor_path = (
        REPO_PATH / "entities" / "sensor" / "sql" / "mood" / f"{user}_mood_streak.yaml"
    )
    mood_streak_sensor_path.parent.mkdir(parents=True, exist_ok=True)
    mood_streak_sensor_path.write_text(
        f"""---
name: {user.title()} | Mood Streak

unique_id: {user}_mood_streak

icon: mdi:fire

query: >-
  WITH daily_last_states AS (
    SELECT
      DATE(to_timestamp(states.last_updated_ts)) as check_date,
      states.state,
      states.last_updated_ts,
      ROW_NUMBER() OVER (
        PARTITION BY DATE(to_timestamp(states.last_updated_ts))
        ORDER BY states.last_updated_ts DESC
      ) as rn
    FROM states
    INNER JOIN states_meta ON states.metadata_id = states_meta.metadata_id
    WHERE states_meta.entity_id = 'input_select.{user}_mood_today'
      AND states.last_updated_ts >= EXTRACT(EPOCH FROM (CURRENT_DATE - INTERVAL '365 days'))
      AND DATE(to_timestamp(states.last_updated_ts)) < CURRENT_DATE
  ),
  valid_dates AS (
    SELECT DISTINCT check_date
    FROM daily_last_states
    WHERE rn = 1
      AND state IN ('Very Low', 'Low', 'Okay', 'Good', 'Great')
  ),
  ordered_dates AS (
    SELECT
      check_date,
      (CURRENT_DATE - 1) - check_date as days_ago,
      ROW_NUMBER() OVER (ORDER BY check_date DESC) as rn
    FROM valid_dates
    ORDER BY check_date DESC
  ),
  consecutive_groups AS (
    SELECT
      check_date,
      days_ago,
      rn,
      days_ago - rn + 1 as grp
    FROM ordered_dates
  )
  SELECT COUNT(*)::integer as streak
  FROM consecutive_groups
  WHERE grp = (SELECT grp FROM consecutive_groups WHERE days_ago = 0 LIMIT 1)

column: streak
""",  # noqa: S608
    )

    print(f"  ✓ Generated mood files for {user}")


if __name__ == "__main__":
    main()
