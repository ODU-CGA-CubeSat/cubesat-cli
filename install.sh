#!/usr/bin/bash

# Create $HOME/.cubesat-cli folder, if none exists
if [ ! -r $HOME/.cubesat-cli ]; then
    mkdir $HOME/.cubesat-cli
fi

# Create $HOME/.cubesat-cli/bin folder, if none exists
if [ ! -r $HOME/.cubesat-cli/bin ]; then
    mkdir $HOME/.cubesat-cli/bin
fi

# Copy source files to $HOME/.cubesat-cli folder
cp -r ./* $HOME/.cubesat-cli

# Create symlink for cubesat-cli, if none exists
if [ ! -r $HOME/.cubesat-cli/bin/cubesat-cli ]; then
    ln -sv $HOME/.cubesat-cli/cubesat-cli.py $HOME/.cubesat-cli/bin/cubesat-cli
fi

# Add $HOME/.cubesat-cli to PATH in ~/.bashrc
printf '\n# cubesat-cli\nexport PATH="$PATH:$HOME/.cubesat-cli/bin"' >> ~/.bashrc
source ~/.bashrc
