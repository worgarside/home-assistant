#!/bin/bash

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    echo git add .
    git add .

    echo git stash -m "shell_command.checkout_develop_head|$(date +%s)"
    git stash -m "shell_command.checkout_develop_head|$(date +%s)"

    git checkout develop
    git pull
}>> /config/shell-command.log 2>&1
