"""
Advent of Code 2023
Day 5.2
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


def map_seed_ranges(
    seed_range: list[tuple[int, int]],
    almanac: list[Map],
    i: int
) -> list[tuple[int, int]]:
    if not almanac or i >= len(almanac):
        return seed_range

    mapped_range = []
    for start, end in seed_range:
        # Run seed range through each map
        all_mapped = False
        for map in almanac[i]:
            # Full overlap
            if start >= map.src_start and end <= map.src_end:
                start += map.offset
                end += map.offset
                mapped_range.append((start, end))

                # Nothing left to do given the seed range
                # is a full overlap of this map
                all_mapped = True
                break

            # Start inside, end outside
            elif start >= map.src_start and start <= map.src_end and end > map.src_end:
                old_end = end
                start += map.offset
                end = map.src_end + map.offset
                mapped_range.append((start, end))

                # Update start and end with what's left over
                # for the next map (if any)
                start = map.src_end + 1
                end = old_end

            # Start outside, end inside
            elif start < map.src_start and end >= map.src_start and end <= map.src_end:
                old_start = start
                start = map.src_start + map.offset
                end += map.offset
                mapped_range.append((start, end))

                # Update start and end with what's left over
                # for the next map (if any)
                start = old_start
                end = map.src_start - 1

        # Add any range not matched 'as is' in readiness for the next map set
        if not all_mapped:
            mapped_range.append((start, end))

    return map_seed_ranges(mapped_range, almanac, i+1)


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

        seeds = re.findall(r"(\d+) (\d+)", lines[0])
        almanac = build_almanac(lines[1:])

        min_loc: tuple[int, int] = None
        for s, l in seeds:
            range_start = int(s)
            range_end = range_start + int(l)

            locs = map_seed_ranges([(range_start, range_end)], almanac, 0)
            candidate_loc = min(locs, key=lambda r: r[0])

            if min_loc is None or candidate_loc < min_loc:
                min_loc = candidate_loc

        print(min_loc[0])


if __name__ == "__main__":
    main()
