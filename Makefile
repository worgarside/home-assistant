vscode-shortcut-1:
	act -s GITHUB_TOKEN="$(gh auth token)" -W .github/workflows/validate_ha_config.yml
