#!/bin/bash

/config/resources/gh_cli/bin/gh auth login --with-token < "/config/.github_token" 2>&1 > /config/home-assistant.log

while getopts ":u:d:" opt; do
  case $opt in
    u) URL="$OPTARG"
    ;;
    d) IS_DRAFT="$OPTARG"
    ;;
    *) echo "shell_command.mark_pr_as_ready_for_review INVALID USAGE" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

if [[ "$IS_DRAFT" = "True" || "$IS_DRAFT" = "true" ]]; then
  /config/resources/gh_cli/bin/gh pr ready "$URL"
  exit 0
else
  /config/resources/gh_cli/bin/gh pr ready "$URL" --undo
  exit 0
fi
