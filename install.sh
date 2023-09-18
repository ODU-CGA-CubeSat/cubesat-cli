#!/usr/bin/bash

# Build dof-cubesat schema
if [ ! -r ./dof-cubesat/build/schema/dof-cubesat.yaml ]; then
    cd dof-cubesat
    ./gradlew build
    cd ..
fi

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
    ln -sv $HOME/.cubesat-cli/cubesat_cli.py $HOME/.cubesat-cli/bin/cubesat-cli
fi

# Add $HOME/.cubesat-cli to PATH in ~/.bashrc
condition="echo $PATH | grep 'cubesat-cli'"
if ! eval $condition; then
    printf '\n# cubesat-cli\nexport PATH="$PATH:$HOME/.cubesat-cli/bin"' >> ~/.bashrc
fi
source ~/.bashrc
