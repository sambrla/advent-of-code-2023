"""
Advent of Code 2023
Day 12.2
"""

import functools
import itertools
import sys


@functools.cache
def arrangements(record, groups, seen) -> int:
    """
    Impl help to adopt cache:
    Paulson, J. 2023. https://www.youtube.com/watch?v=xTGkP2GNmbQ
    """
    if not record:
        if not groups and seen == 0:
            return 1
        elif len(groups) == 1 and seen == groups[0]:
            return 1
        else:
            return 0

    spring = record[0]
    count = 0

    if spring == "#":
        count += arrangements(record[1:], groups, seen+1)
    elif spring == "?":
        count += (arrangements("." + record[1:], groups, seen) +
                  arrangements("#" + record[1:], groups, seen))
    else: # Spring is .
        if groups and seen == groups[0]:
            count += arrangements(record[1:], groups[1:], 0)
        elif seen == 0:
            count += arrangements(record[1:], groups, seen)
        # else:
        #     print(record, groups, seen)

    return count


def unfold(report, groups):
    for i in range(len(report)):
        report[i] = "?".join(itertools.repeat(report[i], 5))

    for i in range(len(groups)):
        groups[i] = groups[i] * 5


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        record = []
        groups = []

        for line in [line.strip().split() for line in doc]:
            record.append(line[0])
            groups.append([int(n) for n in line[1].split(",")])

        unfold(record, groups)

        sum = 0
        for i in range(len(record)):
            sum += arrangements(record[i], tuple(groups[i]), 0)

        print(sum)


if __name__ == "__main__":
    main()
