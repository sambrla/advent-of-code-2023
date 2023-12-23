"""
Advent of Code 2023
Day 10.2
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


def print_map(map: list[str]):
    for line in map:
        print(line)
    print()


def walk_loop(map: list[str], start: tuple[int, int], next: tuple[int, int],
              dir: Heading) -> tuple[list[tuple[int, int]],
                                     list[tuple[int, int]]]:
    route = [next]
    cross = [] # for counting edge crossings

    # If the S (start) tile is a |, L, or J, record it as an edge crossing
    r, c = start
    if map[r-1][c] in "|F7" and (map[r][c+1] in "-7J" or map[r][c-1] in "-LF"):
        cross.append(start)

    while start != next:
        r, c = next
        match map[r][c]:
            case  "|":
                cross.append(next)
                next = (r + (1 if dir == Heading.SOUTH else -1), c)
            case  "-":
                next = (r, c + (1 if dir == Heading.EAST else -1))
            case  "L":
                cross.append(next)
                if dir == Heading.WEST:
                    next = (r-1, c)
                    dir = Heading.NORTH
                else: # SOUTH
                    next = (r, c+1)
                    dir = Heading.EAST
            case  "J":
                cross.append(next)
                if dir == Heading.SOUTH:
                    next = (r, c-1)
                    dir = Heading.WEST
                else: # EAST
                    next = (r-1, c)
                    dir = Heading.NORTH
            case  "7":
                if dir == Heading.EAST:
                    next = (r+1, c)
                    dir = Heading.SOUTH
                else: # NORTH
                    next = (r, c-1)
                    dir = Heading.WEST
            case  "F":
                if dir == dir.WEST:
                    next = (r+1, c)
                    dir = Heading.SOUTH
                else: # NORTH
                    next = (r, c+1)
                    dir = Heading.EAST
        route.append(next)
    return (route, cross)


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
        route, cross = walk_loop(map, *start)
        # print_map(map)

        count = 0
        for r in range(len(map)):
            is_inside = False
            for c in range(len(map[0])):
                if (r, c) in route and (r,c) in cross:
                    is_inside = not is_inside

                if is_inside and (r,c) not in route:
                    count += 1
                    # map[r] = map[r][:c] + "#" + map[r][c+1:]

        # print_map(map)
        print(count)


if __name__ == "__main__":
    main()
