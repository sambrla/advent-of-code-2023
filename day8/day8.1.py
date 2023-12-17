"""
Advent of Code 2023
Day 8.1
"""

import re
import sys


def follow_map(inst: str, map: dict[str, tuple[str, str]], node: str) -> int:
    steps = 0
    found = False
    while not found:
        for i in inst:
            match i:
                case "L":
                    node = map[node][0]
                case "R":
                    node = map[node][1]
                case _:
                    print("This shouldn't happen")
            steps += 1
            if node == "ZZZ":
                found = True
                break

    return steps


def parse_input(input: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    reg = re.compile(r"([A-Z]{3}).*([A-Z]{3}).*([A-Z]{3})")

    instr = input[0].strip()
    nodes = {}
    for line in input[2:]:
        match = reg.match(line)
        if match:
            n = match.group(1)
            l = match.group(2)
            r = match.group(3)
            nodes[n] = (l, r)

    return (instr, nodes)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        inst, map = parse_input(doc.readlines())
        print(follow_map(inst, map, "AAA"))


if __name__ == "__main__":
    main()
