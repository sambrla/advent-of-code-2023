"""
Advent of Code 2023
Day 12.1
"""

import sys


def arrangements(record, groups, i) -> int:
    if i == len(record):
        # print(record)
        damaged = [len(s) for s in record.split(".") if s]
        return 1 if groups == damaged else 0

    spring = record[i]
    count = 0

    # Unknown
    if spring == "?":
        count += (arrangements(record[:i] + "." + record[i+1:], groups, i) +
                  arrangements(record[:i] + "#" + record[i+1:], groups, i))
    else:
        # Known
        # record[i] in ".#":
        count += arrangements(record, groups, i+1)

    return count


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        record = []
        groups = []

        for line in [line.strip().split() for line in doc]:
            record.append(line[0])
            groups.append([int(n) for n in line[1].split(",")])

        sum = 0
        for i in range(len(record)):
            sum += arrangements(record[i], groups[i], 0)

        print(sum)


if __name__ == "__main__":
    main()
