#!/bin/bash

while getopts ":u:" opt; do
  case $opt in
    u) URL="$OPTARG"
    ;;
    *) echo "shell_command.set_pr_auto_merge INVALID USAGE" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

/config/resources/gh_cli/bin/gh pr merge "$URL" --squash --auto
