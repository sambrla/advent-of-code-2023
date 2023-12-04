"""
Advent of Code 2023
Day 2.2
"""

import re
import sys

def game_power(game: str) -> int:
    # Extract cube info
    cubes_r = re.findall(r"(\d+) (red)", game)
    cubes_g = re.findall(r"(\d+) (green)", game)
    cubes_b = re.findall(r"(\d+) (blue)", game)

    # The highest occurrence = the number required
    hi_r = int(max(cubes_r, key=lambda t: int(t[0]))[0])
    hi_g = int(max(cubes_g, key=lambda t: int(t[0]))[0])
    hi_b = int(max(cubes_b, key=lambda t: int(t[0]))[0])

    # Multiplication of these = the 'power'
    return hi_r * hi_g * hi_b


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        power_sum = 0
        for line in doc:
            power_sum += game_power(line)
        print(power_sum)


if __name__ == "__main__":
    main()
