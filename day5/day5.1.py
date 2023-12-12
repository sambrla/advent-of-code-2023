"""
Advent of Code 2023
Day 5.1
"""

import re
import sys

from collections import namedtuple

# _map_names = [
#     "seed-to-soil",
#     "soil-to-fertilizer",
#     "fertilizer-to-water",
#     "water-to-light",
#     "light-to-temperature",
#     "temperature-to-humidity",
#     "humidity-to-location"
# ]

Map = namedtuple("Map", "src_start, src_end, dst_start, dst_end, offset")


def map_seeds(seed: int, almanac: list[Map], i: int) -> int:
    if not almanac or i >= len(almanac):
        return seed

    for map in almanac[i]:
        if seed in range(map.src_start, map.src_end + 1):
            seed += map.offset
            break

    return map_seeds(seed, almanac, i+1)


def build_almanac(input: list[str]) -> list[Map]:
    """
    Each returned map in the almanac is in the format:
    (src start, src end, dst start, dst end, offset)
    """
    regex = re.compile(r"(\d+) (\d+) (\d+)")

    almanac = []
    for i in range(0, len(input)):
        vals = regex.findall(input[i])
        maps = []
        for dst_start, src_start, range_len in vals:
            maps.append(Map(int(src_start),
                            int(src_start)+int(range_len)-1,
                            int(dst_start),
                            int(dst_start)+int(range_len)-1,
                            int(dst_start)-int(src_start)))
        maps.sort(key=lambda m: m.src_start)
        almanac.append(maps)

    return almanac


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        lines = doc.read().split("\n\n")

        seeds = re.findall(r"\d+", lines[0])
        almanac = build_almanac(lines[1:])
        min_loc = None

        for s in seeds:
            loc = map_seeds(int(s), almanac, 0)
            if min_loc is None or loc < min_loc:
                min_loc = loc

        print(min_loc)


if __name__ == "__main__":
    main()
