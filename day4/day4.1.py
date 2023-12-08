"""
Advent of Code 2023
Day 4.1
"""

import re
import sys

def calculate_winnings(cards: list[int]) -> int:
    num_re = re.compile(r"Card\s+\d+:\s+([^\|]+)\s+\|\s+([^\|]+)\n")

    total_points = 0
    for line in cards:
        points = 0

        nums = num_re.findall(line)
        if not nums:
            continue

        want, have = nums[0]
        want = want.split()
        have = have.split()

        # Check if 'have' numbers are in 'want' list
        for n in have:
            if n in want:
                points = points * 2 if points > 0 else 1

        total_points += points
    return total_points


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        print(calculate_winnings(doc.readlines()))


if __name__ == "__main__":
    main()
