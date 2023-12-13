"""
Advent of Code 2023
Day 6.1
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


def parse_races(input: list[str]):
    nums = []
    for line in input:
        nums.append(re.findall(r"\d+", line))

    # Should only be two rows: one for time, one for distance
    assert len(nums) == 2

    total_moe = 0
    for i in range(0, len(nums[0])):
        moe = calculate_race_opts((int(nums[0][i]), int(nums[1][i])))
        total_moe = total_moe * moe if total_moe else moe

    print(total_moe)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        parse_races(doc.readlines())


if __name__ == "__main__":
    main()
