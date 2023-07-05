#!/bin/bash

while getopts ":u:c:" opt; do
  case $opt in
    u) URL="$OPTARG"
    ;;
    c) COMMENT="$OPTARG"
    ;;
    *) echo "shell_command.comment_on_pr INVALID USAGE" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

/config/resources/gh_cli/bin/gh auth login --with-token < "/config/.github_token" 2>&1 > /config/home-assistant.log

/config/resources/gh_cli/bin/gh pr comment "$URL" --body "$COMMENT"
