#!/bin/bash

while getopts ":b:t:" opt; do
  case ${opt} in
    b) BRANCH="${OPTARG}"
    ;;
    t) TOKEN="${OPTARG}"
    ;;
    *) echo "shell_command.checkout_git_branch INVALID USAGE :(" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    cd /config || exit 1

    echo git add .
    git add .

    echo git stash -m "shell_command.checkout_git_branch|$(date +%s)"
    git stash -m "shell_command.checkout_git_branch|$(date +%s)"

    git fetch --all --prune

    git checkout "${BRANCH}"
    git pull

    git status

    curl -sSL -X POST \
      -H "Authorization: Bearer ${TOKEN}" \
      -H "Content-Type: application/json" \
      -d '{"entity_id": "sensor.current_git_branch"}' \
      http://homeassistant.local:8123/api/services/homeassistant/update_entity

}>> /config/shell-command.log 2>&1
