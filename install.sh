#!/bin/bash

set -e 

echo "Installing reco..."

INSTALL_DIR="$HOME/.local/share/reco"
BIN_DIR="$HOME/.local/bin/"

# create directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# copy project files
echo "Coping files..."
rm -rf "$INSTALL_DIR"
cp -rf . "$INSTALL_DIR"

# make executanles 
chmod +x "$INSTALL_DIR/reco"

#create symlink
ln -sf "$INSTALL_DIR/reco" "$BIN_DIR/reco"

echo "Installation complete!"

echo ""
echo "Make sure $BIN_DIR is in your PATH."
echo "Run: reco --help"


