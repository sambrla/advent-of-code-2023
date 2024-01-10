"""
Advent of Code 2023
Day 14.2
"""

import sys


def calculate_load(cp):
    load = 0
    for i, line in enumerate(cp):
        for c in line:
            if c == "O":
                load += len(cp)-i

    return load


def tilt(cp: list[str]) -> list[str]:
    """
    Tilts rocks (O) to the east
    """
    for i in range(len(cp)):
        for j in range(len(cp[i])-1, -1, -1):
            if cp[i][j] in "#O":
                continue
            # cp[i][j] must be "."
            for k in range(j-1, -1, -1):
                # If we hit a cube-shaped rock, we can't perform a swap
                if cp[i][k] == "#":
                    break
                # Swap j and k
                if cp[i][k] == "O":
                    cp[i] = cp[i][:k] + cp[i][j] + cp[i][k+1:j] + cp[i][k] + cp[i][j+1:]
                    break
    return cp


def rotate_right(cp):
    return ["".join(l[::-1]) for l in zip(*cp)]


def rotate_left(cp):
    return ["".join(l) for l in zip(*cp)][::-1]


def spin_cycle(cp):
    # North
    cp = rotate_right(cp)
    cp = tilt(cp)

    # West
    cp = rotate_right(cp)
    cp = tilt(cp)

    # South
    cp = rotate_right(cp)
    cp = tilt(cp)

    # East
    cp = rotate_right(cp)
    cp = tilt(cp)

    return cp


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        cp = [line.strip() for line in doc.readlines()]

        CYCLE = 147 # Pattern repeats
        for i in range(CYCLE):
            cp = spin_cycle(cp)
        for i in range(1000000000 % CYCLE):
            cp = spin_cycle(cp)

        print(calculate_load(cp))


if __name__ == "__main__":
    main()
