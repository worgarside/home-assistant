#!/bin/bash

while getopts ":t:v:" opt; do
  case ${opt} in
    t) TOKEN="${OPTARG}"
    ;;
    v) TAG="${OPTARG}"
    ;;
    *) echo "shell_command.get_latest_appdaemon_release INVALID USAGE :(" >> /config/home-assistant.log
       exit 1 ;;
  esac
done

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    cd /addon_configs/a0d7b954_appdaemon || exit 1

    echo git add .
    git add .

    echo git stash -m "shell_command.get_latest_appdaemon_release|$(date +%s)"
    git stash -m "shell_command.get_latest_appdaemon_release|$(date +%s)"

    git fetch --all --tags --prune
    git checkout "${TAG}"

    git status

}>> /config/shell-command.log 2>&1
