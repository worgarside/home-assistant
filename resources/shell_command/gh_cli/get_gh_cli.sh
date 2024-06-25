#!/bin/bash

GH_CLI_VERSION="2.51.0"
TARBALL_FILE=gh_"$GH_CLI_VERSION"_linux_arm64.tar.gz

# Download CLI
wget \
    https://github.com/cli/cli/releases/download/v"$GH_CLI_VERSION"/"$TARBALL_FILE" \
    -O "$TARBALL_FILE"

# Remove old CLI
rm -rf /config/resources/gh_cli || :

# Extract CLI
mkdir -p /config/resources/gh_cli
tar -xf "$TARBALL_FILE" -C /config/resources/gh_cli --strip-components=1

# Grant execute permissions
chmod +x /config/resources/gh_cli/bin/gh

# Remove tarball
rm "$TARBALL_FILE"

echo "gh cli version: $(/config/resources/gh_cli/bin/gh --version)" >> /config/home-assistant.log

TOKEN_FILES=(
    "/config/worgarside-hass.github_token"
    "/config/worgarside.github_token"
)

for TOKEN_FILE in "${TOKEN_FILES[@]}"
do
    if [ ! -f "$TOKEN_FILE" ]
    then
        echo "Error: No GitHub token found at $TOKEN_FILE" >> /config/home-assistant.log
        continue
    fi

    /config/resources/gh_cli/bin/gh auth login --with-token < "$TOKEN_FILE"

    if ! /config/resources/gh_cli/bin/gh auth status >/dev/null 2>&1
    then
        echo "Error logging in with GH CLI using token from $TOKEN_FILE" >> /config/home-assistant.log
    else
        echo "Logged in with GH CLI using token from $TOKEN_FILE" >> /config/home-assistant.log
        /config/resources/gh_cli/bin/gh auth status >> /config/home-assistant.log 2>&1
    fi
done
