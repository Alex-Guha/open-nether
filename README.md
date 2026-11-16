<div align="center">

# Open Nether

![Minecraft 1.21.1](https://img.shields.io/badge/Minecraft-1.21.1-62B47A?style=flat-square)
![NeoForge](https://img.shields.io/badge/Loader-NeoForge-D7742F?style=flat-square)
![License](https://img.shields.io/badge/License-PolyForm%20Shield%201.0.0-blue?style=flat-square)
[![Build](https://img.shields.io/github/actions/workflow/status/Alex-Guha/open-nether/build.yml?branch=main&style=flat-square&logo=github&label=Build)](https://github.com/Alex-Guha/open-nether/actions/workflows/build.yml)

</div>

Opens the Nether's roof and reshapes its terrain for players arriving from above, by airship through Immersive Portals: Aeronautics' dimension stack.

## Highlights

- No roof: the Nether is open above, with about 130 blocks of open air over its highest ground.
- Highlands and mesas up to about Y 120, with overhanging rims, cut by wide basins down to the lava sea. The caverns stay inside the highlands, open to the sky in places.
- Crimson and warped forests in groves and glades: dense stands of huge fungi and open clearings.
- Giant crimson and warped fungi, 24 to 40 blocks tall, with caps wide and flat enough to land an airship on.

### Good to know

- Chunks generated before the mod was added keep their roof: start a new world, or explore new parts of the Nether.
- Glowstone grows only under netherrack ceilings, so with the roof gone there is less of it (about 40% of vanilla's).
- The Nether's logical height is 256, so the dimension stack's ceiling plane sits at Y 256 and nether portals may be placed up to there.
- MNS's mega fortress hangs its posts from the ceiling by chains; with no ceiling the chains run up into the open air.

### Compatibility

Works with:
- YUNG's Better Nether Fortresses
- MNS (Moog's Nether Structures)
- Immersive Portals: Aeronautics' dimension stack

Not compatible:
- Incendium and Amplified Nether: they replace the Nether's terrain too, and the game will not load with both.
- Jaden's Nether Expansion with its default config, which replaces the Nether's terrain and biome source; set `netherWorldGenOverhaul` and `improvedNetherBiomeSource` to false in its config (the game warns about this).

## How it works

Open Nether is data: it changes the Nether's world generation through the same files a datapack would, shipped inside the mod's jar. It keeps vanilla's Nether below the old roof: the lava sea at Y 32, the caverns, the biomes and their features. Above that, instead of the rock cap and the bedrock roof, the terrain thins out under the open sky, at a height that changes across the land: high in the highlands, low in the basins that open onto the lava sea. The groves and giant fungi are features and structures added to the Nether's own biomes through biome tags (`opennether:has_feature/...`, `opennether:has_structure/...`), so a modpack can add other mods' biomes to them.

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
