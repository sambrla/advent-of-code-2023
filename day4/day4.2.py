"""
Advent of Code 2023
Day 4.2
"""

import re
import sys

def card_counting(card_points: list[int]) -> int:
    card_qtys = [1] * len(card_points)
    for i, points in enumerate(card_points):
        # Each copy of this card will need to be processed
        for _ in range(card_qtys[i]):
            # Update copies based on pre-calc points
            for k in range(1, points+1):
                # "Cards will never make you copy a card past the end of the table."
                card_qtys[i+k] += 1

    return sum(card_qtys)


def calculate_points(cards: list[str]) -> list[int]:
    num_re = re.compile(r"Card\s+\d+:\s+([^\|]+)\s+\|\s+([^\|]+)\n")

    all_points = []
    # Calc the number of points for each card
    for line in cards:
        points = 0

        nums = num_re.findall(line)
        if not nums:
            continue

        want, have = nums[0]
        want = want.split()
        have = have.split()

        # Check if 'have' numbers are in 'want' list
        for n in have:
            if n in want:
                points += 1

        all_points.append(points)
    return all_points


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        card_points = calculate_points(doc.readlines())
        print(card_counting(card_points))


if __name__ == "__main__":
    main()
