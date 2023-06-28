#!/bin/bash

GH_CLI_VERSION="2.31.0"
TARBALL_FILE=gh_"$GH_CLI_VERSION"_linux_arm64.tar.gz

# Download CLI
wget \
    https://github.com/cli/cli/releases/download/v"$GH_CLI_VERSION"/"$TARBALL_FILE" \
    -O "$TARBALL_FILE"

# Remove old CLI
rm -rf resources/gh_cli || :

# Extract CLI
mkdir -p resources/gh_cli
tar -xf "$TARBALL_FILE" -C resources/gh_cli --strip-components=1

# Grant execute permissions
chmod +x resources/gh_cli/bin/gh

# Remove tarball
rm "$TARBALL_FILE"

echo "gh cli version: $(resources/gh_cli/bin/gh --version)"
