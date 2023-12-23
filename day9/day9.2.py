"""
Advent of Code 2023
Day 9.2
"""

import sys


def next_sequence(dataset: list[int]) -> int:
    starts = [dataset[0]]
    diff = [] # diff between pairs
    prev = 0

    while True:
        for i in range(len(dataset)-1):
            diff.append(dataset[i+1] - dataset[i])
        starts.append(diff[0])
        if all(v == 0 for v in diff):
            break
        dataset = diff
        diff = []

    for i in reversed(starts):
        prev = i - prev

    return prev


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
