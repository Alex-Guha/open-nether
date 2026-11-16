#!/usr/bin/env bash
# Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
# Many mods ship libraries (or their own classes) as jar-in-jar. Gradle sees only the outer jar, so this extracts the
# nested jars, recursively, of every Modrinth mod build.gradle names (maven.modrinth:<slug>:...) into deps/
# (gitignored), where build.gradle puts them on the compile classpath. On a fresh machine, run
# `./gradlew downloadModJars` first so the outer jars are in Gradle's cache.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p deps
CACHE=${GRADLE_USER_HOME:-$HOME/.gradle}/caches/modules-2/files-2.1/maven.modrinth
JAR=${JAVA_HOME:+$JAVA_HOME/bin/}jar
command -v "$JAR" > /dev/null || { echo "no jar tool ($JAR): set JAVA_HOME to a JDK" >&2; exit 1; }

extract_nested() {  # $1 = jar to inspect
    local tmp inner
    tmp=$(mktemp -d)
    # the JDK's jar tool (needed for the build anyway): unzip is not on every machine
    (cd "$tmp" && "$JAR" xf "$1" META-INF/jarjar)
    for inner in "$tmp"/META-INF/jarjar/*.jar; do
        [ -f "$inner" ] || continue
        cp "$inner" "deps/$(basename "$inner")"
        echo "extracted $(basename "$inner")"
        extract_nested "$inner"
    done
    rm -rf "$tmp"
}

slugs=$(grep -vE '^\s*//' build.gradle | grep -oE 'maven\.modrinth:[A-Za-z0-9_.-]+:' | cut -d: -f2 | sort -u || true)
[ -n "$slugs" ] || { echo "build.gradle names no Modrinth mods: nothing to extract"; exit 0; }
for slug in $slugs; do
    [ -d "$CACHE/$slug" ] || { echo "$slug is not in Gradle's cache: run ./gradlew downloadModJars" >&2; exit 1; }
    while IFS= read -r outer; do
        extract_nested "$outer"
    done < <(find "$CACHE/$slug" -name '*.jar')
done

# Drop older duplicates of the same library (bundled by two mods)
for prefix in $(ls deps | sed -E 's/-[0-9][^/]*\.jar$//' | sort | uniq -d); do
    for old in $(ls deps/"$prefix"-[0-9]*.jar | sort -V | head -n -1); do
        rm -f "$old"; echo "removed duplicate $(basename "$old")"
    done
done
