"""
Advent of Code 2023
Day 13.1
"""

import sys


def reflect(lines: list[str], l: int, r: int) -> tuple[int, int]:
    """
    Returns tuple of reflected line count as (above, below)
    """
    start_l = l
    start_r = r

    # Check reflected lines
    while l >= 0 and r < len(lines):
        if lines[l] != lines[r]:
            return (0, 0) # No perfect relection
        l -= 1
        r += 1

    return (start_l+1, len(lines)-start_r)


def find_reflections(lines: list[str]) -> tuple[int, int]:
    res = (0, 0)
    i = 0

    # Find lines of reflection
    while i < len(lines)-1:
        if lines[i] == lines[i+1]:
            res = reflect(lines, i, i+1)
            if res != (0, 0):
                break
        i += 1

    return res


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        patterns = doc.read()
        patterns = patterns.split("\n\n")
        patterns = [[line for line in p.split("\n") if line] for p in patterns]

        ans = 0
        for p in patterns:
            # Horizontal
            up, _ = find_reflections(p)
            ans += 100 * up

            # Vertical
            t = ["".join(reversed(l)) for l in zip(*p)]
            left, _ = find_reflections(t)
            ans += left

        print(ans)


if __name__ == "__main__":
    main()
