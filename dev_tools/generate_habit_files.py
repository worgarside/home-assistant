"""Generate habit tracking files for additional numbered habits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_PATH = Path(__file__).parents[1]
STATE_FILE = Path(__file__).parent / "habit_counts.json"

if REPO_PATH.name != "home-assistant" or not REPO_PATH.is_dir():
    raise RuntimeError(
        "Unable to locate the `home-assistant` repository."
        f" Current path is: {REPO_PATH!s}",
    )


def load_state() -> dict[str, dict[str, int]]:
    """Load previously saved habit counts from state file.

    Returns:
        Nested dict of {user: {habit_type: count}}, empty if file doesn't exist.
    """
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())  # type: ignore[no-any-return]
    return {}


def save_state(state: dict[str, dict[str, int]]) -> None:
    """Persist habit counts to state file.

    Args:
        state: Nested dict of {user: {habit_type: count}}.
    """
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
    print(f"  ✓ Saved state to {STATE_FILE}")


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

        # Input number for streak min days per week
        streak_min_days_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_binary_{num}_streak_min_days_per_week.yaml"
        )
        streak_min_days_path.parent.mkdir(parents=True, exist_ok=True)
        streak_min_days_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Streak Min Days Per Week"

icon: mdi:calendar-week

min: 1

max: 7

step: 1

mode: box

initial: 7
""",
        )

        # Input number for repeat reminder interval
        repeat_interval_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_binary_{num}_repeat_reminder_interval.yaml"
        )
        repeat_interval_path.parent.mkdir(parents=True, exist_ok=True)
        repeat_interval_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Repeat Reminder Interval"

icon: mdi:timer-outline

min: 1

max: 1440

step: 1

mode: box

initial: 60
""",
        )

        # Input number for repeat reminder count
        repeat_count_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_binary_{num}_repeat_reminder_count.yaml"
        )
        repeat_count_path.parent.mkdir(parents=True, exist_ok=True)
        repeat_count_path.write_text(
            f"""---
name: "{user.title()} | Habit Binary {num}: Repeat Reminder Count"

icon: mdi:repeat

min: 0

max: 1000

step: 1

mode: box

initial: 0
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

condition: >-
  {{{{
    is_state('input_boolean.XXXUSERXXX_habit_binary_XXXNUMXXX', 'off') and
    states("input_text.XXXUSERXXX_habit_binary_XXXNUMXXX_name") not in ["", "unknown"]
  }}}}

variables:
  habit_name: >-
    {{{{
      states('input_text.XXXUSERXXX_habit_binary_XXXNUMXXX_name')
      | default('Habit Binary XXXNUMXXX')
    }}}}
  repeat_interval: >-
    {{{{
      states('input_number.XXXUSERXXX_habit_binary_XXXNUMXXX_repeat_reminder_interval') | int(60)
    }}}}
  repeat_reminder_count: >-
    {{{{
      states('input_number.XXXUSERXXX_habit_binary_XXXNUMXXX_repeat_reminder_count') | int(0)
    }}}}

action:
  - action: script.notify_XXXUSERXXX
    data:
      title: "Habit Reminder"
      message: "Don't forget to mark {{{{ habit_name }}}} as complete!"
      notification_id: XXXUSERXXX_habit_binary_XXXNUMXXX_reminder
      url: /home-XXXUSERXXX/mood-habits
      actions:
        - action: "MARK_HABIT_AS_COMPLETE__XXXUSERUPPERXXX__BINARY_XXXNUMXXX"
          title: "Mark as Complete"

  - if: "{{{{ repeat_reminder_count | int(0) > 0 }}}}"
    then:
      - repeat:
          until: >-
            XXXJINJA2SETSTARTXXX
              set cutoff_time = (
                now().replace(hour=0, minute=0, second=0, microsecond=0)
                + timedelta(days=1)
                - timedelta(minutes=(repeat_interval + 5))
              )
            XXXJINJA2SETENDXXX
            XXXJINJA2SETSTARTXXX set habit_completed = is_state('input_boolean.XXXUSERXXX_habit_binary_XXXNUMXXX', 'on') XXXJINJA2SETENDXXX
            {{{{
              now() >= cutoff_time or
              repeat.index > repeat_reminder_count | int(0) or
              habit_completed
            }}}}
          sequence:
            - delay:
                minutes: "{{{{ repeat_interval | int(60) }}}}"

            - action: script.notify_XXXUSERXXX
              data:
                title: "Habit Reminder"
                message: "Don't forget to mark {{{{ habit_name }}}} as complete!"
                notification_id: XXXUSERXXX_habit_binary_XXXNUMXXX_reminder
                url: /home-XXXUSERXXX/mood-habits
                actions:
                  - action: "MARK_HABIT_AS_COMPLETE__XXXUSERUPPERXXX__BINARY_XXXNUMXXX"
                    title: "Mark as Complete"
"""  # noqa: E501
        reminder_content = (
            reminder_template
            .replace("{{{{", "{{")
            .replace("}}}}", "}}")
            .replace("XXXJINJA2SETSTARTXXX", "{%")
            .replace("XXXJINJA2SETENDXXX", "%}")
            .replace("XXXUSERUPPERXXX", user.upper())
            .replace("XXXUSERXXX", user)
            .replace("XXXNUMXXX", str(num))
            .replace("XXXUSERTITLEXXX", user.title())
        )
        reminder_automation_path.write_text(reminder_content)

        # SQL sensor for streak
        sql_sensor_path = (
            REPO_PATH
            / "entities"
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
  WITH min_days_per_week AS (
    SELECT COALESCE(
      (SELECT (state::numeric)::integer
       FROM states
       INNER JOIN states_meta ON states.metadata_id = states_meta.metadata_id
       WHERE states_meta.entity_id = 'input_number.{user}_habit_binary_{num}_streak_min_days_per_week'
       ORDER BY states.last_updated_ts DESC
       LIMIT 1),
      7
    ) as min_days
  ),
  daily_last_states AS (
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
  week_groups AS (
    SELECT
      DATE_TRUNC('week', check_date - INTERVAL '1 day') + INTERVAL '1 day' as week_start,
      COUNT(*) as days_count
    FROM valid_dates
    GROUP BY DATE_TRUNC('week', check_date - INTERVAL '1 day') + INTERVAL '1 day'
  ),
  yesterday_week_start AS (
    SELECT DATE_TRUNC('week', (CURRENT_DATE - 1) - INTERVAL '1 day') + INTERVAL '1 day' as week_start
  ),
  valid_weeks AS (
    SELECT
      wg.week_start,
      wg.days_count,
      EXTRACT(EPOCH FROM ((CURRENT_DATE - 1) - wg.week_start)) / 86400 as days_ago_week_start
    FROM week_groups wg
    CROSS JOIN min_days_per_week mdpw
    CROSS JOIN yesterday_week_start yws
    WHERE wg.days_count >= mdpw.min_days
       OR (wg.week_start = yws.week_start AND wg.days_count > 0)
  ),
  ordered_weeks AS (
    SELECT
      vw.week_start,
      vw.days_count,
      vw.days_ago_week_start,
      ROW_NUMBER() OVER (ORDER BY vw.week_start DESC) as rn,
      (EXTRACT(EPOCH FROM (
        vw.week_start - LAG(vw.week_start, 1) OVER (ORDER BY vw.week_start DESC)
      )) / 86400)::integer as days_since_prev_week
    FROM valid_weeks vw
    CROSS JOIN yesterday_week_start yws
    WHERE vw.week_start <= yws.week_start
  ),
  consecutive_week_groups AS (
    SELECT
      week_start,
      days_count,
      days_ago_week_start,
      rn,
      SUM(CASE WHEN days_since_prev_week IS NULL OR days_since_prev_week = 7 THEN 0 ELSE 1 END)
        OVER (ORDER BY week_start DESC) as grp
    FROM ordered_weeks
  ),
  current_streak_weeks AS (
    SELECT week_start, days_count
    FROM consecutive_week_groups
    WHERE grp = (SELECT grp FROM consecutive_week_groups ORDER BY week_start DESC LIMIT 1)
  )
  SELECT COALESCE(SUM(days_count)::integer, 0) as streak
  FROM current_streak_weeks

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

        # Input number for repeat reminder interval
        repeat_interval_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_countable_{num}_repeat_reminder_interval.yaml"
        )
        repeat_interval_path.parent.mkdir(parents=True, exist_ok=True)
        repeat_interval_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Repeat Reminder Interval"

icon: mdi:timer-outline

min: 1

max: 1440

step: 1

mode: box

initial: 60
""",
        )

        # Input number for repeat reminder count
        repeat_count_path = (
            REPO_PATH
            / "entities"
            / "input_number"
            / "habit"
            / f"{user}_habit_countable_{num}_repeat_reminder_count.yaml"
        )
        repeat_count_path.parent.mkdir(parents=True, exist_ok=True)
        repeat_count_path.write_text(
            f"""---
name: "{user.title()} | Habit Countable {num}: Repeat Reminder Count"

icon: mdi:repeat

min: 0

max: 1000

step: 1

mode: box

initial: 0
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

condition: >-
  {{
    states('input_number.XXXUSERXXX_habit_countable_XXXNUMXXX') | int(0) == 0 and
    states("input_text.XXXUSERXXX_habit_countable_XXXNUMXXX_name") not in ["", "unknown"]
  }}

variables:
  habit_name: >-
    {{{{ states('input_text.XXXUSERXXX_habit_countable_XXXNUMXXX_name')
    | default('Habit Countable XXXNUMXXX') }}}}
  repeat_interval: >-
    "{{{{ states('input_number.XXXUSERXXX_habit_countable_XXXNUMXXX_repeat_reminder_interval') | int(60) }}}}"
  repeat_reminder_count: >-
    "{{{{ states('input_number.XXXUSERXXX_habit_countable_XXXNUMXXX_repeat_reminder_count') | int(0) }}}}"

action:
  - action: script.notify_XXXUSERXXX
    data:
      title: "Habit Reminder"
      message: "Don't forget to track {{{{ habit_name }}}}!"
      notification_id: XXXUSERXXX_habit_countable_XXXNUMXXX_reminder
      url: /home-XXXUSERXXX/mood-habits
      actions:
        - action: "INCREMENT_HABIT__XXXUSERUPPERXXX__COUNTABLE_XXXNUMXXX"
          title: "Increment"

  - if: "{{{{ repeat_reminder_count | int(0) > 0 }}}}"
    then:
      - repeat:
          until: >-
            XXXJINJA2SETSTARTXXX
              set cutoff_time = (
                now().replace(hour=0, minute=0, second=0, microsecond=0)
                + timedelta(days=1)
                - timedelta(minutes=(repeat_interval + 5))
              )
            XXXJINJA2SETENDXXX
            XXXJINJA2SETSTARTXXX set habit_completed = states('input_number.XXXUSERXXX_habit_countable_XXXNUMXXX') | int(0) > 0 XXXJINJA2SETENDXXX
            {{{{
              now() >= cutoff_time or
              repeat.index > repeat_reminder_count | int(0) or
              habit_completed
            }}}}
          sequence:
            - delay:
                minutes: "{{{{ repeat_interval | int(60) }}}}"

            - action: script.notify_XXXUSERXXX
              data:
                title: "Habit Reminder"
                message: "Don't forget to track {{{{ habit_name }}}}!"
                notification_id: XXXUSERXXX_habit_countable_XXXNUMXXX_reminder
                url: /home-XXXUSERXXX/mood-habits
                actions:
                  - action: "INCREMENT_HABIT__XXXUSERUPPERXXX__COUNTABLE_XXXNUMXXX"
                    title: "Increment"
"""  # noqa: E501
        reminder_content = (
            reminder_template
            .replace("{{{{", "{{")
            .replace("}}}}", "}}")
            .replace("XXXJINJA2SETSTARTXXX", "{%")
            .replace("XXXJINJA2SETENDXXX", "%}")
            .replace("XXXUSERUPPERXXX", user.upper())
            .replace("XXXUSERXXX", user)
            .replace("XXXNUMXXX", str(num))
            .replace("XXXUSERTITLEXXX", user.title())
        )
        reminder_automation_path.write_text(reminder_content)

        print(f"    ✓ Generated files for countable habit {num}")


def generate_binary_habit_notification_action_files(user: str, total_count: int) -> None:
    """Generate a single automation that handles mark-complete actions for all binary habits.

    Args:
        user: User name (e.g., 'will').
        total_count: Total number of binary habits (determines number of triggers).
    """
    print(f"Generating binary habit notification action automation for {user}...")

    automation_path = (
        REPO_PATH
        / "entities"
        / "automation"
        / "mobile_app"
        / "notification_action"
        / "habit"
        / f"{user}_habit_binary"
        / "mark_complete.yaml"
    )
    automation_path.parent.mkdir(parents=True, exist_ok=True)

    trigger_lines = [
        f"  - platform: event\n"
        f"    event_type: mobile_app_notification_action\n"
        f"    event_data:\n"
        f"      action: MARK_HABIT_AS_COMPLETE__{user.upper()}__BINARY_{num}\n"
        f'    id: "{num}"'
        for num in range(1, total_count + 1)
    ]
    triggers = "\n\n".join(trigger_lines)

    content = f"""---
alias: /mobile-app/notification-action/habit/{user}-habit-binary/mark-complete

id: mobile_app_notification_action_habit_{user}_habit_binary_mark_complete

description: Mark {user.title()}'s binary habits as complete from notification action

mode: parallel

trigger:
{triggers}

action:
  - action: input_boolean.turn_on
    target:
      entity_id: "input_boolean.{user}_habit_binary_{{{{ trigger.id }}}}"
"""
    automation_path.write_text(content)
    print(f"  ✓ Generated binary habit notification action automation for {user}")


def generate_countable_habit_notification_action_files(
    user: str,
    total_count: int,
) -> None:
    """Generate a single automation that handles increment actions for all countable habits.

    Args:
        user: User name (e.g., 'will').
        total_count: Total number of countable habits (determines number of triggers).
    """
    print(f"Generating countable habit notification action automation for {user}...")

    automation_path = (
        REPO_PATH
        / "entities"
        / "automation"
        / "mobile_app"
        / "notification_action"
        / "habit"
        / f"{user}_habit_countable"
        / "increment.yaml"
    )
    automation_path.parent.mkdir(parents=True, exist_ok=True)

    trigger_lines = [
        f"  - platform: event\n"
        f"    event_type: mobile_app_notification_action\n"
        f"    event_data:\n"
        f"      action: INCREMENT_HABIT__{user.upper()}__COUNTABLE_{num}\n"
        f'    id: "{num}"'
        for num in range(1, total_count + 1)
    ]
    triggers = "\n\n".join(trigger_lines)

    content = f"""---
alias: /mobile-app/notification-action/habit/{user}-habit-countable/increment

id: mobile_app_notification_action_habit_{user}_habit_countable_increment

description: Increment {user.title()}'s countable habits from notification action

mode: parallel

trigger:
{triggers}

action:
  - action: input_number.increment
    target:
      entity_id: "input_number.{user}_habit_countable_{{{{ trigger.id }}}}"
"""
    automation_path.write_text(content)
    print(f"  ✓ Generated countable habit notification action automation for {user}")


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


def _run_for_user(
    user: str,
    binary_count: int | None,
    countable_count: int | None,
    *,
    mood: bool,
) -> None:
    """Run all generators for a single user.

    Args:
        user: User name (e.g., 'will').
        binary_count: Number of binary habits to generate, or None to skip.
        countable_count: Number of countable habits to generate, or None to skip.
        mood: Whether to generate mood files.
    """
    if binary_count is not None:
        generate_binary_habit_files(user, binary_count)
        generate_binary_habit_notification_action_files(user, binary_count)

    if countable_count is not None:
        generate_countable_habit_files(user, countable_count)
        generate_countable_habit_notification_action_files(user, countable_count)

    if binary_count is not None or countable_count is not None:
        generate_habit_template_sensors(user)

    if mood:
        generate_mood_files(user)


def main() -> None:
    """Run the habit file generator."""
    parser = argparse.ArgumentParser(
        description="Generate habit tracking files for numbered habits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_habit_files.py --user=will --binary 10
  python generate_habit_files.py --user=will --countable 2
  python generate_habit_files.py --user=will --binary 10 --countable 2
  python generate_habit_files.py --user=will --binary   # uses last saved count
  python generate_habit_files.py --regenerate-all       # regenerate everything from saved state
        """,
    )
    parser.add_argument(
        "--user",
        help="User name (e.g., 'will') — not required with --regenerate-all",
    )
    parser.add_argument(
        "--binary",
        type=int,
        nargs="?",
        const=-1,
        metavar="COUNT",
        help="Generate binary habits; omit COUNT to reuse last saved count",
    )
    parser.add_argument(
        "--countable",
        type=int,
        nargs="?",
        const=-1,
        metavar="COUNT",
        help="Generate countable habits; omit COUNT to reuse last saved count",
    )
    parser.add_argument(
        "--mood",
        action="store_true",
        help="Generate mood tracking files",
    )
    parser.add_argument(
        "--regenerate-all",
        action="store_true",
        help="Regenerate all files for all users/types using saved state (ignores other flags)",
    )

    args = parser.parse_args()
    state = load_state()

    if args.regenerate_all:
        if not state:
            parser.error(
                f"No saved state found at {STATE_FILE}. "
                "Run with explicit args first to build the state.",
            )
        print(f"Regenerating all files from saved state ({STATE_FILE})...")
        for user, user_state in state.items():
            print(f"\n--- {user} ---")
            _run_for_user(
                user=user,
                binary_count=user_state.get("binary"),
                countable_count=user_state.get("countable"),
                mood=bool(user_state.get("mood", False)),
            )
        print("\n✓ Regeneration complete")
        return

    if not args.user:
        parser.error("--user is required unless --regenerate-all is specified")

    if args.binary is None and args.countable is None and not args.mood:
        parser.error(
            "At least one of --binary, --countable, --mood, or --regenerate-all must be specified",
        )

    user = args.user.lower()
    user_state = state.setdefault(user, {})

    binary_count: int | None = None
    countable_count: int | None = None

    if args.binary is not None:
        if args.binary == -1:
            if "binary" in user_state:
                binary_count = user_state["binary"]
                print(f"Using saved binary count for {user}: {binary_count}")
            else:
                parser.error(
                    f"No count provided and no saved state for {user}/binary. "
                    "Provide a count explicitly, e.g. --binary 10",
                )
        else:
            if args.binary < 1:
                parser.error("--binary count must be a positive integer")
            binary_count = args.binary

    if args.countable is not None:
        if args.countable == -1:
            if "countable" in user_state:
                countable_count = user_state["countable"]
                print(f"Using saved countable count for {user}: {countable_count}")
            else:
                parser.error(
                    f"No count provided and no saved state for {user}/countable. "
                    "Provide a count explicitly, e.g. --countable 2",
                )
        else:
            if args.countable < 1:
                parser.error("--countable count must be a positive integer")
            countable_count = args.countable

    _run_for_user(
        user=user,
        binary_count=binary_count,
        countable_count=countable_count,
        mood=args.mood,
    )

    if binary_count is not None:
        user_state["binary"] = binary_count
    if countable_count is not None:
        user_state["countable"] = countable_count
    if args.mood:
        user_state["mood"] = True

    save_state(state)
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
  - action: input_select.select_option
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
  - action: input_text.set_value
    target:
      entity_id: input_text.{user}_mood_note
    data:
      value: ""
""",
    )

    # SQL sensor for mood streak
    mood_streak_sensor_path = (
        REPO_PATH / "entities" / "sql" / "mood" / f"{user}_mood_streak.yaml"
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
