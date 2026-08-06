set shell := ["bash", "-euo", "pipefail", "-c"]

# List available recipes
default:
    @just --list

# Install locked dependencies and prek git hooks
setup:
    uv sync --locked --all-groups
    uv run --frozen prek install --force

# Run the same blocking checks as CI
ci:
    just check
    just ha-validate

# Run every prek hook against the repository
check:
    uv run --frozen prek run --all-files --show-diff-on-failure

# Run auto-formatting hooks
format:
    uv run --frozen prek run end-of-file-fixer --all-files
    uv run --frozen prek run pretty-format-json --all-files
    uv run --frozen prek run trailing-whitespace --all-files
    uv run --frozen prek run yamlfmt --all-files
    uv run --frozen prek run ruff-check --all-files
    uv run --frozen prek run ruff-format --all-files
    uv run --frozen prek run beautysh --all-files

# Validate entities and regenerate entity documentation
entities:
    uv run --frozen prek run validate-entities --all-files
    uv run --frozen prek run generate-readme --all-files

# Type-check maintained Python utilities
typecheck:
    uv run --frozen basedpyright

# Validate GitHub Actions workflows
actionlint:
    uv run --frozen prek run actionlint --all-files

# Regenerate the uv lockfile
lock:
    uv lock

# Update prek hook revisions after their cooldown period
hooks-update:
    uv run --frozen prek auto-update --cooldown-days 3

# Run Home Assistant validation locally through act
ha-validate event="pull_request":
    command -v act >/dev/null || { echo "Install act to run Home Assistant validation locally."; exit 1; }
    act "{{ event }}" -W .github/workflows/validate_home_assistant_config.yml

# Run the Home Assistant colour generator
colors:
    uv run --frozen python dev_tools/color_generator.py

# Add the Home Assistant webhook to one or more repositories
add-webhook callback_url *repositories:
    fish dev_tools/add_webhook_to_repo.fish "{{ callback_url }}" {{ repositories }}
