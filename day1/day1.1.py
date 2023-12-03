"""
Advent of Code 2023
Day 1.1
"""

import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        sum = 0
        for line in doc:
            cval = 0

            # First digit
            for c in line:
                if c.isdigit():
                    cval = int(c) * 10
                    break

            # Last digit
            for c in reversed(line):
                if c.isdigit():
                    cval += int(c)
                    break

            sum += cval
        print(sum)


if __name__ == "__main__":
    main()
