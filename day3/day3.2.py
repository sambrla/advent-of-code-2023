"""
Advent of Code 2023
Day 3.2
"""

import re
import sys

def parse_part_number(data: list[str]) -> int:
    num_re = re.compile(r"\d+")
    sym_re = re.compile(r"\*")

    gear_nums = {}
    ratios = []
    for y, line in enumerate(data):
        # Validate all nums on current line by searching
        # surrounding border of adjacent chars for symbol
        for num in num_re.finditer(line):
            for dy, dx in ((dy, dx) for dy in range(-1, 2)
                                    for dx in range(-1, len(num.group())+1)):
                # Check bounds
                if ((y+dy < 0 or y+dy >= len(data)) or
                    (num.start()+dx < 0 or num.start()+dx >= len(line))):
                    continue

                needle = sym_re.match(data[y+dy][num.start()+dx])
                if not needle:
                    continue

                # Create a key from the needle's coords and store in a dict
                # with the current num. If a subsequent match generates the
                # same key for a different num, calculate and store the ratio
                key = "{},{}".format(y+dy, num.start()+dx)
                if key not in gear_nums:
                    gear_nums[key] = int(num.group())
                else:
                    ratios.append(gear_nums[key] * int(num.group()))

    return sum(ratios)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        print(parse_part_number(doc.readlines()))


if __name__ == "__main__":
    main()
