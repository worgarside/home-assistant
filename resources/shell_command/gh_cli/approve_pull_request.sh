#!/bin/bash

while getopts ":u:" opt; do
  case $opt in
    u) URL="$OPTARG"
    ;;
    *) echo "shell_command.approve_pull_request INVALID USAGE" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

/config/resources/gh_cli/bin/gh pr review "$URL" --approve --body "Approved via Home Assistant"
