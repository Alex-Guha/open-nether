#!/usr/bin/env python3
# Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
"""Writes the giant fungus structure templates (src/main/resources/data/opennether/structure/giant_fungus/*.nbt).

    python3 scripts/giant-fungi.py

Each fungus is a straight stem whose flared base reaches 6 blocks below the template's ground line (the structure starts
6 blocks under the surface), under an umbrella cap: nearly flat in the middle (wide enough to land an airship on),
dropping towards a skirt at the rim, with shroomlights in its underside and, for crimson, weeping vines hanging from it.
The shapes are fixed by the seeds below, so running this again writes the same files. Run from the repository root.
"""
import gzip
import io
import math
import pathlib
import random
import struct

DATA_VERSION = 3955  # Minecraft 1.21.1
OUT = pathlib.Path("src/main/resources/data/opennether/structure/giant_fungus")
EMBED = 6  # blocks of the stem below ground

# name: (kind, seed, stem height above ground, stem radius, cap radius, cap drop at the rim, skirt length)
FUNGI = {
    "crimson_1": ("crimson", 11, 30, 1.6, 10, 5, 3),
    "crimson_2": ("crimson", 12, 38, 2.1, 12, 6, 4),
    "crimson_3": ("crimson", 13, 24, 1.4, 8, 4, 3),
    "warped_1": ("warped", 21, 32, 1.6, 10, 7, 4),
    "warped_2": ("warped", 22, 40, 2.1, 12, 8, 5),
    "warped_3": ("warped", 23, 26, 1.4, 8, 6, 3),
}


def tag_string(s):
    b = s.encode("utf-8")
    return struct.pack(">H", len(b)) + b


def write_tag(buf, value):
    """the payload of a value: dict = compound, list of ints = list of int, list of dicts = list of compound, str, int"""
    if isinstance(value, dict):
        for key, v in value.items():
            buf.write(bytes([tag_type(v)]) + tag_string(key))
            write_tag(buf, v)
        buf.write(b"\x00")
    elif isinstance(value, list):
        inner = tag_type(value[0]) if value else 0
        buf.write(bytes([inner]) + struct.pack(">i", len(value)))
        for v in value:
            write_tag(buf, v)
    elif isinstance(value, str):
        buf.write(tag_string(value))
    elif isinstance(value, int):
        buf.write(struct.pack(">i", value))
    else:
        raise TypeError(value)


def tag_type(value):
    return {dict: 10, list: 9, str: 8, int: 3}[type(value)]


def fungus(kind, seed, height, stem_r, cap_r, drop, skirt):
    rng = random.Random(seed)
    stem = {"Name": f"minecraft:{kind}_stem", "Properties": {"axis": "y"}}
    hyphae = {"Name": f"minecraft:{kind}_hyphae", "Properties": {"axis": "y"}}
    wart = {"Name": "minecraft:nether_wart_block" if kind == "crimson" else "minecraft:warped_wart_block"}
    light = {"Name": "minecraft:shroomlight"}
    vine = {"Name": "minecraft:weeping_vines_plant"}
    vine_tip = {"Name": "minecraft:weeping_vines", "Properties": {"age": "25"}}
    blocks = {}
    c = cap_r + 1  # the axis, in template coordinates
    ground = EMBED
    top = ground + height  # the cap's highest layer
    # stem: flared roots below and just above ground, then the trunk up into the cap
    for y in range(0, top):
        above = y - ground
        r = stem_r + (1.6 if above < 0 else max(0.0, 1.6 - above * 0.5))
        for dx in range(-3, 4):
            for dz in range(-3, 4):
                if dx * dx + dz * dz <= r * r + 0.3:
                    outer = dx * dx + dz * dz > (r - 1) * (r - 1)
                    blocks[(c + dx, y, c + dz)] = hyphae if outer and above < 3 else stem
    # cap: top surface falls from flat in the middle to `drop` lower at the rim; 3 thick in the middle, 2 at the rim
    underside = []
    for dx in range(-cap_r, cap_r + 1):
        for dz in range(-cap_r, cap_r + 1):
            d = math.sqrt(dx * dx + dz * dz)
            if d > cap_r + 0.4:
                continue
            f = d / cap_r
            surface = top - round(drop * f ** 2.5)
            if rng.random() < 0.05 and f < 0.8:
                surface += 1  # a bump now and then, so the top is not a plate
            thick = 3 if f < 0.6 else 2
            bottom = surface - thick + 1
            if f > 0.85:
                bottom -= skirt  # the skirt hanging from the rim
            for y in range(bottom, surface + 1):
                blocks[(c + dx, y, c + dz)] = wart
            underside.append((c + dx, bottom, c + dz, d))
    for x, y, z, d in underside:
        if d > stem_r + 1 and rng.random() < 0.14:
            blocks[(x, y, z)] = light
        elif kind == "crimson" and d > stem_r + 2 and rng.random() < 0.09:
            length = rng.randint(2, 9)
            for i in range(1, length + 1):
                if y - i < ground + 2:
                    break
                blocks[(x, y - i, z)] = vine if i < length else vine_tip
    return blocks


def template(blocks):
    palette, index = [], {}
    entries = []
    for (x, y, z), state in sorted(blocks.items()):
        key = (state["Name"], tuple(sorted(state.get("Properties", {}).items())))
        if key not in index:
            index[key] = len(palette)
            palette.append(state)
        entries.append({"pos": [x, y, z], "state": index[key]})
    size = [max(p[i] for p in blocks) + 1 for i in range(3)]
    return {"DataVersion": DATA_VERSION, "size": size, "palette": palette, "blocks": entries, "entities": []}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, params in FUNGI.items():
        data = template(fungus(*params))
        buf = io.BytesIO()
        buf.write(b"\x0a" + tag_string(""))
        write_tag(buf, data)
        (OUT / f"{name}.nbt").write_bytes(gzip.compress(buf.getvalue(), mtime=0))
        print(f"{name}: size {data['size']}, {len(data['blocks'])} blocks")


if __name__ == "__main__":
    main()
