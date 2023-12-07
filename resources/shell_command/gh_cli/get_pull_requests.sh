#!/bin/bash

sh /config/resources/shell_command/gh_cli/check_gh_cli.sh

REPO_NAME=$1

if [ -z "$REPO_NAME" ]
then
    echo '
        {
            "0": {
                "title": "ERROR: No repository name provided to sensor",
                "labels": ["major"],
                "url": "https://github.com/settings/tokens",
                "statusCheckRollup": ["FAILURE"],
                "author": "worgarside",
                "createdAt": "2021-01-01T00:00:00Z",
                "isDraft": false,
                "number": 0,
                "autoMergeRequest": false
            }
        }
    '
    exit 0
fi

PULL_REQUESTS=$(
    /config/resources/gh_cli/bin/gh pr list \
        --repo "worgarside/$REPO_NAME" \
        --json author,autoMergeRequest,createdAt,isDraft,labels,number,reviewDecision,statusCheckRollup,title,url \
        --jq '
            map(.labels = [.labels[].name]) |
            map(.author = .author.login) |
            sort_by(.createdAt) |
            reverse |
            map(.statusCheckRollup |= group_by(.name))|
            map(
                .statusCheckRollup |= map(
                    max_by(.startedAt) |
                    if .status == "IN_PROGRESS" then "IN_PROGRESS" else (.conclusion // .state) end
                )
            ) |
            map(.statusCheckRollup |= unique) |
            map(.autoMergeRequest = (.autoMergeRequest != null)) |
            to_entries |
            map({(.key|tostring): .value}) |
            add |
            with_entries(select(.key | test("^[0-9]$")))
    '
)

if [ -z "$PULL_REQUESTS" ]
then
    echo "{}"
    exit 0
fi

echo "$PULL_REQUESTS"
