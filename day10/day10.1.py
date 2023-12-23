"""
Advent of Code 2023
Day 10.1
"""

from enum import Enum
import re
import sys


"""
| is a vertical pipe connecting NORTH and SOUTH.
- is a horizontal pipe connecting EAST and WEST.
L is a 90-degree bend connecting NORTH and EAST.
J is a 90-degree bend connecting NORTH and WEST.
7 is a 90-degree bend connecting SOUTH and WEST.
F is a 90-degree bend connecting SOUTH and EAST.
. is ground; there is no pipe in this tile.
"""


class Heading(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def walk_loop(map: list[str], start: tuple[int, int], next: tuple[int, int],
              head: Heading) -> int:
    steps = 0
    while start != next:
        r, c = next
        match map[r][c]:
            case  "|":
                next = (r + (1 if head == Heading.SOUTH else -1), c)
            case  "-":
                next = (r, c + (1 if head == Heading.EAST else -1))
            case  "L":
                if head == Heading.WEST:
                    next = (r-1, c)
                    head = Heading.NORTH
                else: # SOUTH
                    next = (r, c+1)
                    head = Heading.EAST
            case  "J":
                if head == Heading.SOUTH:
                    next = (r, c-1)
                    head = Heading.WEST
                else: # EAST
                    next = (r-1, c)
                    head = Heading.NORTH
            case  "7":
                if head == Heading.EAST:
                    next = (r+1, c)
                    head = Heading.SOUTH
                else: # NORTH
                    next = (r, c-1)
                    head = Heading.WEST
            case  "F":
                if head == head.WEST:
                    next = (r+1, c)
                    head = Heading.SOUTH
                else: # NORTH
                    next = (r, c+1)
                    head = Heading.EAST
        steps += 1
    return steps


def find_start(map: list[str]) -> tuple[tuple[int, int], tuple[int, int], Heading]:
    start = (0, 0)
    next = start
    head = None

    for r, line in enumerate(map):
        match = re.search("S", line)
        if match:
            start = (r, match.span()[0])
            break

    r, c = start
    if map[r][c+1] in "-7J":
        next = (start[0], start[1]+1)
        head = Heading.EAST
    elif map[r+1][c] in "|LJ":
        next = (start[0]+1, start[1])
        head = Heading.SOUTH
    elif map[r][c-1] in "-FL":
        next = (start[0], start[1]-1)
        head = Heading.WEST
    else: # map[r-1][c] in "|7F"
        next = (start[0]-1, start[1])
        head = Heading.NORTH

    return (start, next, head)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        map = [line.strip() for line in doc]
        start = find_start(map)
        steps = walk_loop(map, *start)
        print(steps // 2 + 1)


if __name__ == "__main__":
    main()
