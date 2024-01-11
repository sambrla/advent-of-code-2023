"""
Advent of Code 2023
Day 15.1
"""

import sys


def hash(input: str) -> int:
    val = 0
    for c in input:
        val += ord(c)
        val *= 17
        val &= (255) # Use bitwise AND trick (divisor-1) as 256 is a power of 2
    return val


def proces_seq(seq: list[str]) -> int:
    sum = 0
    for s in seq:
        sum += hash(s)
    return sum


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        seq = doc.read().strip().split(",")
        print(proces_seq(seq))


if __name__ == "__main__":
    main()
