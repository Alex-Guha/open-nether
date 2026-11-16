# Licensing

For anyone who redistributes this mod, includes it in a pack, or contributes code to it: which works it is built from, which part is under which licence, and how each file says where it comes from. It is not legal advice.

## Chain of works

| # | Work | Licence | What this project took |
|---|---|---|---|
| 1 | [NeoForge MDK](https://github.com/NeoForged/MDK) (the NeoForged project) | MIT ([TEMPLATE_LICENSE.txt](TEMPLATE_LICENSE.txt)) | The build files: `build.gradle`, `settings.gradle`, `gradle.properties`, `neoforge.mods.toml` |
| 2 | [Gradle](https://gradle.org) wrapper | Apache-2.0 | `gradlew`, `gradlew.bat`, `gradle/wrapper/` |

<!-- Add a row for every work code is copied or ported from, with its licence and what was taken. -->

## Which part is under which licence

- Everything written for this mod, in `src/`, `scripts/` and elsewhere, is under the [PolyForm Shield License 1.0.0](LICENSE). Its licensor is Alex Guha; the `Required Notice:` line is in [NOTICE](NOTICE).
- The build files of the MDK keep its MIT licence, and the Gradle wrapper its Apache License 2.0, as far as they are not this project's changes.

Both `LICENSE` and `NOTICE` go into every jar's `META-INF`.

## How each file is marked

Every Java file starts with a comment naming its origin and licence. A file written for this mod:

```java
/*
 * Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
 */
```

`python3 scripts/stamp-headers.py` adds it to files without a header, and `--check` (part of `scripts/check.sh`) reports files without one. Code copied from another work keeps that work's header and notices, adds a line naming this project's changes, and gets a row in the table above.

## Things that are not code

- No third-party library is bundled in the jar: other mods are dependencies the player installs.
- Textures, models and sounds are this project's own unless a file next to them says otherwise.

## Contributions

Contributions are accepted under the terms in [CONTRIBUTING.md](CONTRIBUTING.md), "Licence of contributions".
