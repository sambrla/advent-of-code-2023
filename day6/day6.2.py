"""
Advent of Code 2023
Day 6.2
"""

import re
import sys


def calculate_race_opts(race: tuple[int, int]) -> int:
    race_len, record = race

    dists = []
    for ms in range(0, (race_len >> 1) + 1):
        dists.append((race_len - ms) * ms)

    ways = sum(i > record for i in dists)
    return (ways << 1) if (race_len+1) % 2 == 0 else (ways << 1) - 1


def total_margin_of_error(input):
    nums = []
    for line in input:
        match = re.search(r"[^A-Za-z:\s][\d+ ]+", line)
        if (match):
            nums.append(int(match.group().replace(" ", "")))

    # Should only be two rows: one for time, one for distance
    assert len(nums) == 2

    return calculate_race_opts((nums[0], nums[1]))


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        print(total_margin_of_error(doc.readlines()))


if __name__ == "__main__":
    main()
