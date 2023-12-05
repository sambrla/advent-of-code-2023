"""
Advent of Code 2023
Day 2.2
"""

import re
import sys

def game_power(game: str) -> int:
    # Extract cube info
    cubes_r = re.findall(r"(\d+) red", game)
    cubes_g = re.findall(r"(\d+) green", game)
    cubes_b = re.findall(r"(\d+) blue", game)

    # Convert to ints
    cubes_r = [ int(i) for i in cubes_r ]
    cubes_g = [ int(i) for i in cubes_g ]
    cubes_b = [ int(i) for i in cubes_b ]

    # Multiplying the highest occurrence of each = the 'power'
    return max(cubes_r) * max(cubes_g) * max(cubes_b)


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
