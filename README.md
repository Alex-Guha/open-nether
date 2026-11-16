<div align="center">

# Open Nether

![Minecraft 1.21.1](https://img.shields.io/badge/Minecraft-1.21.1-62B47A?style=flat-square)
![NeoForge](https://img.shields.io/badge/Loader-NeoForge-D7742F?style=flat-square)
![License](https://img.shields.io/badge/License-PolyForm%20Shield%201.0.0-blue?style=flat-square)
[![Build](https://img.shields.io/github/actions/workflow/status/Alex-Guha/open-nether/build.yml?branch=main&style=flat-square&logo=github&label=Build)](https://github.com/Alex-Guha/open-nether/actions/workflows/build.yml)

</div>

Opens the Nether's roof and reshapes its terrain for players arriving from above, by airship through Immersive Portals: Aeronautics' dimension stack.

**Work in progress**: nothing is changed yet.

## Highlights

- 

### Good to know

- 

### Compatibility

Works with:
- YUNG's Better Nether Fortresses
- MNS (Moog's Nether Structures)
- Immersive Portals: Aeronautics' dimension stack

Not compatible:
- 

## How it works

<!-- A few paragraphs for players and newcomers: what the mod changes and how, in game terms. -->

## Building from source

You need JDK 21 (newer ones break the Gradle and Mixin tooling) and Python 3.

```bash
export JAVA_HOME=/path/to/jdk-21
./gradlew downloadModJars --no-daemon --console=plain   # downloads the mods we compile against
scripts/extract-nested-deps.sh      # unpacks the libraries nested inside their jars into deps/
./gradlew build --no-daemon --console=plain
scripts/check.sh                    # the static checks
```

The jar is `build/libs/opennether-<version>.jar`. The build also runs the unit tests (`-x test` skips them). If the build reports a class from another mod as missing, run `scripts/extract-nested-deps.sh` again.

## Contributing and reporting bugs

Report bugs through [GitHub issues](../../issues/new/choose). Pull requests are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Changes in each release are in [changelog/](changelog/).

## Credits and licence

This mod's code is under the [PolyForm Shield License 1.0.0](LICENSE). You may include it in modpacks, patch it and build add-ons for it, but not republish it or a fork of it as a competing mod. If this mod stops being maintained, that restriction no longer applies. [LICENSING.md](LICENSING.md) says which part is under which licence, and [NOTICE](NOTICE) credits every project it builds on.
