#!/bin/bash

REPO_NAME=$1

if [ -z "$REPO_NAME" ]
then
    echo "ERROR 1"
    exit 1
fi

TOKEN_FILE=/config/.github_token

if [ ! -f "$TOKEN_FILE" ]
then
    echo "ERROR 2"
    exit 1
fi

/config/resources/gh_cli/bin/gh auth login --with-token < "$TOKEN_FILE" &&
/config/resources/gh_cli/bin/gh pr list \
    --repo "worgarside/$REPO_NAME" \
    --json author,autoMergeRequest,createdAt,isDraft,labels,number,statusCheckRollup,title,url \
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
