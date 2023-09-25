# cubesat-cli

CLI tool for performing CRUD operations on bill of materials (BOM) data & assembly instructions data, using the dof-cubesat schema.

# Requirements

- linkml v1.5.6+
- git

# Installation

Recursively clone and `cd` into the `cubesat-cli` repo

```bash
git clone --recurse-submodules https://github.com/ODU-CGA-CubeSat/cubesat-cli.git
cd cubesat-cli
```

Install `cubesat-cli` in `~/.cubesat-cli`

```bash
./gradlew install
```

Update `~/.bashrc` to add `~/.cubesat-cli/bin` to `PATH`

```bash
printf '\n# cubesat-cli\nexport PATH="$PATH:$HOME/.cubesat-cli/bin"' >> ~/.bashrc
```

Update interactive shell with changes made to `~/.bashrc`

```bash
source ~/.bashrc
```
