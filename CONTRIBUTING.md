# Contributing

Thanks for wanting to help. Bug reports, compatibility reports and pull requests are all welcome.

## Reporting a bug or asking for a feature

Use the issue templates ([bug report](../../issues/new?template=bug_report.yaml), [feature request](../../issues/new?template=feature_request.yml)). A bug report helps most when it includes:
- the version of this mod, and of any other mods involved;
- steps that make it happen again;
- `logs/latest.log` (*and* `crash-reports/crash-*.txt` if relevant, not "or");
- for anything drawn wrong, a screenshot or video.

## Building

See "Building from source" in the [README](README.md).

## Finding your way around

| Path | What |
|---|---|
| `src/main/java/com/alexguha/opennether/` | The mod |
| `src/main/java/com/alexguha/opennether/compat/` | Compatibility with other mods; `OptionalModMixinPlugin` skips mixins into mods that are not installed |
| `src/main/resources/data/minecraft/` | Overrides of the vanilla Nether's world generation: its noise settings (terrain and surface), dimension type and cave carver |
| `src/main/resources/data/opennether/` | Our own world generation: the terrain's density functions and noise, the forests' groves, the giant fungi (structures and templates), and the NeoForge biome modifiers that add them to the Nether's biomes |
| `scripts/giant-fungi.py` | Writes the giant fungus templates (`data/opennether/structure/giant_fungus/`) |
| `src/main/templates/META-INF/neoforge.mods.toml` | The mod's metadata, filled in from `gradle.properties` by the build |
| `scripts/` | Build helpers and the static checks (`check.sh`) |
| `changelog/` | Changes per release, one file per minor version |

Some code comments may cite `docs/...`: those are the maintainer's notes, which are not public. Every comment should explain itself without them.

## Testing a change

Test in game, with the built jar in a normal game install. In the pull request, say what you tried, with which mods, and whether in single player or on a server. The maintainer may run further tests before merging.

After a build, `scripts/check.sh` runs the static checks:
- `headers`: every Java file has its origin header (below; `python3 scripts/stamp-headers.py` writes them).
- `mixins`: every class, method and field our mixins name exists in the jars we build against, and every mixin into another mod is skipped without that mod (`OptionalModMixinPlugin`, below). Known exceptions are in `scripts/mixincheck-expected.txt`.
- `hooks`: the mixins and reflection other mods have into our classes (`scripts/hooks-into-us.txt`) still find what they need. If a change of yours breaks one, say so in the pull request: that mod's players would crash.
- `version` and `tests`: the version fits the branch, and the unit tests passed.

## Code conventions

- **File headers.** Every Java file starts with a comment saying where it comes from and its licence. After adding files, run `python3 scripts/stamp-headers.py`. Code copied from another project keeps its own header; see `LICENSING.md`.
- **Mixins on other mods** use string `targets` and `remap = false` where the target is not Minecraft's. Add the mod's package to `OptionalModMixinPlugin.MOD_BY_PACKAGE`, or players without that mod crash (`scripts/check.sh` catches a missing one). Check that the injection applies with `-Dmixin.debug.export=true`.
- **Server-side mixins** go in a config's `mixins` section, never `client`.
- **Comments** say what the code does and why, in terms of the game and the other mods involved.

## Pull requests

- One change per pull request.
- Describe what players will notice. The maintainer writes the changelog entry.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), such as `fix(config): keep the setting after a reload`. Following it isn't required: the maintainer can reword a message when merging.
- Write `Fixes #123` for an issue it fixes.
- Sign off every commit (`git commit -s`, below).

## Licence of contributions

This project's code is under the PolyForm Shield License 1.0.0 (`LICENSING.md`). For a contribution to ship with the rest, its licence has to allow that. By submitting a contribution (a pull request, a patch, or code posted in an issue) you agree that:

1. **You have the right to submit it.** You certify the [Developer Certificate of Origin 1.1](https://developercertificate.org/): you wrote it, or it is based on work whose licence lets you submit it under these terms, and you understand it and this agreement are public and kept. Sign off every commit to say so: `git commit -s` adds a `Signed-off-by: Your Name <email>` line. (Use an email you are happy to make public, such as GitHub's noreply address.)
2. **You license it to the maintainer.** You grant Alex Guha, the maintainer, a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable licence to use, reproduce, modify, prepare derivative works of, publicly display, sublicense and distribute your contribution and such derivative works, as part of this project, under the PolyForm Shield License 1.0.0 or under whatever licence the project uses at the time; and a patent licence on the same terms as section 3 of the Apache License 2.0.
3. **You keep your copyright.** This is a licence, not a transfer: you may still use your own contribution in any other way you like.
4. **Code you took from elsewhere keeps its licence.** If part of your contribution comes from another project, say so in the pull request, name the project and its licence, and keep its notices. Code under a licence that can't ship under these terms (GPL, for instance) can't go in.

If you can't agree to these terms, open an issue describing the change instead, and the maintainer may write it.
