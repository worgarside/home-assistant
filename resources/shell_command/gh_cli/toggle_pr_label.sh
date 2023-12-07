#!/bin/bash

while getopts ":u:l:a:" opt; do
    case $opt in
        u) URL="$OPTARG"
            ;;
        l) LABEL="$OPTARG"
            ;;
        a) ADD_REMOVE="$OPTARG"
            ;;
        *) echo "shell_command.toggle_pr_label INVALID USAGE" >> /config/home-assistant.log
            exit 1 ;;
    esac
done

/config/resources/gh_cli/bin/gh pr edit "$URL" --"$ADD_REMOVE"-label "$LABEL"
