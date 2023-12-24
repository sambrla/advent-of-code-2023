"""
Advent of Code 2023
Day 11.2
"""

import sys


def expansion(univ: list[str]) -> list[str]:
    """
    Using @ symbols to denote expansion zones.
    """
    expanded = []

    # Expand rows
    for r in range(len(univ)):
        if all(c == "." for c in univ[r]):
            expanded.append("@" * len(univ[r]))
        expanded.append(univ[r])

    # Expand cols
    colexp = []
    for c in range(len(univ[0])):
        if all(px == "." for px in map(lambda r: r[c], univ)):
            colexp.append(c)

    for c in reversed(colexp):
        for r in range(len(expanded)):
            expanded[r] = expanded[r][:c] + "@" + expanded[r][c:]

    return expanded


def find_galaxies(univ: list[str]):
    galaxies = []

    factor = 999998 # an @ row/col counts as 1 each
    rmulti = 0
    for r in range(len(univ)):
        cmulti = 0
        if all(c == "@" for c in univ[r]):
            rmulti += factor
            continue
        for c in range(len(univ[0])):
            if univ[r][c] == "@":
                cmulti += factor
            if univ[r][c] == "#":
                galaxies.append((r + rmulti, c + cmulti))

    return galaxies


def dist_between_galaxies(galaxies: list[tuple[int, int]]) -> int:
    offset = 1
    dist = 0

    for r, c in galaxies:
        # The offset excludes pair dists that have
        # already been added in prior iterations
        for rp, cp in galaxies[offset:]:
            x = abs(cp - c)
            y = abs(rp - r)
            dist += (x + y)
        offset += 1

    return dist


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        univ = [line.strip() for line in doc]
        univ = expansion(univ)
        galaxies = find_galaxies(univ)
        print(dist_between_galaxies(galaxies))


if __name__ == "__main__":
    main()
