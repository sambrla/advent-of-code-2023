"""
Advent of Code 2023
Day 2.1
"""

import re
import sys

def validate_game(sets: list[str]) -> bool:
    MAX_R = 12
    MAX_G = 13
    MAX_B = 14

    for set in sets:
        # Extract cube info
        cubes_r = re.findall(r"(\d+) red", set)
        cubes_g = re.findall(r"(\d+) green", set)
        cubes_b = re.findall(r"(\d+) blue", set)

        # Count total of {red, green, blue} cubes
        sum_r = sum(int(i) for i in cubes_r)
        sum_g = sum(int(i) for i in cubes_g)
        sum_b = sum(int(i) for i in cubes_b)

        if (sum_r > MAX_R or
            sum_g > MAX_G or
            sum_b > MAX_B):
            # Game is not possible
            return False

    return True


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        valid_ids = []
        for line in doc:
            # Extract game ID
            id = int(re.search("[0-9]+", line).group(0))

            # Split game up into its constituent sets
            game_sets = re.split("[;]", line)
            if validate_game(game_sets):
                # Game is possible; record ID
                valid_ids.append(id)

        print(sum(valid_ids))


if __name__ == "__main__":
    main()
