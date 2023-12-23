"""
Advent of Code 2023
Day 9.1
"""

import sys


def next_sequence(dataset: list[int]) -> int:
    ends = [dataset[-1]]
    diff = [] # diff between pairs
    next = 0

    while True:
        for i in range(len(dataset)-1):
            diff.append(dataset[i+1] - dataset[i])
        ends.append(diff[-1])
        if all(v == 0 for v in diff):
            break
        dataset = diff
        diff = []

    for i in reversed(ends):
        next = next + i

    return next


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        sum = 0
        for line in doc:
            sum += next_sequence([int(n) for n in line.split()])
        print(sum)


if __name__ == "__main__":
    main()
