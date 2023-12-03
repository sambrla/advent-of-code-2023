"""
Advent of Code 2023
Day 1.2
"""

import sys

def replace_digit_words(line: str):
    DIGIT_WORDS = [("oneight", 18),
                   ("twone", 21),
                   ("threeight", 38),
                   ("fiveight", 58),
                   ("sevenine", 79),
                   ("eightwo", 82),
                   ("eighthree", 83),
                   ("nineight", 98),
                   ("one", 1),
                   ("two", 2),
                   ("three", 3),
                   ("four", 4),
                   ("five", 5),
                   ("six", 6),
                   ("seven", 7),
                   ("eight", 8),
                   ("nine", 9)]
    for d in DIGIT_WORDS:
        line = line.replace(d[0], str(d[1]))
    return line


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        sum = 0
        for line in doc:
            cval = 0
            line = replace_digit_words(line)

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
