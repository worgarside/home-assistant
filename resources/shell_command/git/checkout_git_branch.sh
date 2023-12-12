#!/bin/bash

BRANCH="main"

while getopts ":b:e:t:" opt; do
    case ${opt} in
        b)
            if [[ -n "${OPTARG}" ]]; then
                BRANCH="${OPTARG}"
            fi
            ;;
        t)
            [[ "${OPTARG}" != "null" ]] && TOKEN="${OPTARG}" || TOKEN="" ;;
        e)
            [[ "${OPTARG}" != "null" ]] && ENTITY_ID="${OPTARG}" || ENTITY_ID="" ;;
        *) echo "shell_command.checkout_git_branch INVALID USAGE: -${opt} ${OPTARG}" >> /config/home-assistant.log
            exit 1 ;;
    esac
done

{
    exec > >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[INFO]\t/")
    exec 2> >(trap "" INT TERM; sed "s/^/$(date +'%Y-%m-%dT%H:%M:%S')\t[ERROR]\t/" >&2)

    echo "shell_command.checkout_git_branch STARTED with branch: ${BRANCH} and entity ID(s): ${ENTITY_ID}"

    cd /config || exit 1

    echo git add .
    git add .

    echo git stash -m "shell_command.checkout_git_branch|${BRANCH}|$(date +%s)"
    git stash -m "shell_command.checkout_git_branch|${BRANCH}|$(date +%s)"

    echo git fetch --all --prune
    git fetch --all --prune

    echo git checkout "${BRANCH}"
    git checkout "${BRANCH}"

    echo git pull
    git pull

    git status

    if [[ -n ${TOKEN} ]] && [[ -n ${ENTITY_ID} ]]; then
        IFS=',' read -ra ENTITY_IDS <<< "${ENTITY_ID}"

        for id in "${ENTITY_IDS[@]}"; do
            echo "Updating Home Assistant entity: ${id}"

            curl -sSL -X POST \
                -H "Authorization: Bearer ${TOKEN}" \
                -H "Content-Type: application/json" \
                -d '{"entity_id": "'"${id}"'"}' \
                http://homeassistant.local:8123/api/services/homeassistant/update_entity
        done

    else
        echo "Token or entity ID missing, skipping Home Assistant update."
    fi


}>> /config/shell-command.log 2>&1
