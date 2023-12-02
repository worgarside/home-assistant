#!/bin/bash

while getopts ":t:" opt; do
  case ${opt} in
    t) TOKEN="${OPTARG}"
    ;;
    *) echo "shell_command.get_latest_release INVALID USAGE :(" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    cd /config || exit 1

    echo git add .
    git add .

    echo git stash -m "shell_command.get_latest_release|$(date +%s)"
    git stash -m "shell_command.get_latest_release|$(date +%s)"

    git checkout main
    git pull

    git status

    curl -sSL -X POST \
      -H "Authorization: Bearer ${TOKEN}" \
      -d '{"state": "on"}' \
      http://homeassistant.local:8123/api/states/input_boolean.system_latest_release_downloaded

}>> /config/shell-command.log 2>&1
