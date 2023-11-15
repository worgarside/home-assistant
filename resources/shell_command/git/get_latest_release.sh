#!/bin/bash

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    cd /config || exit 1

    echo git add .
    git add .

    echo git stash -m "shell_command.get_latest_release|$(date +%s)"
    git stash -m "shell_command.get_latest_release|$(date +%s)"

    cd /config/appdaemon || exit 1

    git stash -m "shell_command.get_latest_release__appdaemon|$(date +%s)"

    cd /config || exit 1

    git checkout main
    git pull
    git submodule update --init --recursive

    git status
}>> /config/shell-command.log 2>&1
