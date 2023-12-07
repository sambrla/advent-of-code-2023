"""
Advent of Code 2023
Day 3.1
"""

import re
import sys

def parse_part_number(data: list[str]) -> int:
    num_re = re.compile(r"\d+")
    sym_re = re.compile(r"[^\d\w\n.]")

    part_nums = []
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

                if sym_re.match(data[y+dy][num.start()+dx]):
                    part_nums.append(int(num.group()))
                    break

    return sum(part_nums)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        print(parse_part_number(doc.readlines()))


if __name__ == "__main__":
    main()
