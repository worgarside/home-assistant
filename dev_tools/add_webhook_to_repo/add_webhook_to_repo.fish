#!/usr/bin/env fish

# Check if at least two arguments are provided
if test (count $argv) -lt 2
    echo "Usage: fish add_webhook_repo_to_fish.fish <callback_url> <repo_name> ..."
    exit 1
end

# Parse and validate the callback_url argument
set callback_url $argv[1]

# Validate callback_url
if not string match -qr '^https://.+$' $callback_url
    echo "Error: callback_url must be a HTTPS URL."
    echo "Usage: fish add_webhook_repo_to_fish.fish <callback_url> <repo_name> ..."
    exit 1
end

# Define a function to process each argument
function add_webook_to_repo
    set repo_name $argv[1]

    # Validate repo_name
    if not string match -qr '^[a-zA-Z0-9\-_]+$' $repo_name
        echo "Error: Repository names must match the regex ^[a-zA-Z0-9\-_]+\$"
        echo "Usage: fish add_webhook_repo_to_fish.fish <callback_url> <repo_name> ..."
        exit 1
    end

    echo Processing https://github.com/worgarside/$repo_name/settings/hooks

    curl -L \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $gh_token" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/repos/worgarside/$repo_name/hooks \
        -d $webhook_payload >/dev/null
end

set gh_token (gh auth token)

set webhook_payload "{
  \"name\": \"web\",
  \"active\": true,
  \"events\": [
    \"check_run\",
    \"check_suite\",
    \"pull_request\",
    \"pull_request_review\"
  ],
  \"config\": {
    \"url\": \"$callback_url\",
    \"insecure_ssl\": \"0\",
    \"content_type\": \"json\"
  }
}"

# Iterate through the remaining arguments and call the function for each argument
for arg in (seq 2 (count $argv))
    add_webook_to_repo $argv[$arg]
end
