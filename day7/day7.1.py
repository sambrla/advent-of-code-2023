"""
Advent of Code 2023
Day 7.1
"""

import re
import sys


def calculate_winnings(hands: list[tuple[str, int]]) -> int:
    winnings = 0
    for i, hand in enumerate(reversed(hands)):
        winnings += hand[1] * (i+1)
    return winnings


def rank(hands: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    Hand values:
    50000 -> Five of a kind
    41000 -> Four of a kind
    32000 -> Full house
    31100 -> Three of a kind
    22100 -> Two pair
    21110 -> One pair
    11111 -> High card
    """

    # Mapping of cards to rank for sorting equal 'valued' hands
    RANKS = { "A": "n", "K": "m", "Q": "l", "J": "k", "T": "j",
              "9": "i", "8": "h", "7": "g", "6": "f", "5": "e",
              "4": "d", "3": "c", "2": "b", "1": "a" }

    count = { "A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0,
              "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "1": 0 }

    ranked = []
    for hand, bid in hands:
        rank_val = ""
        for card in hand:
            count[card] += 1
            rank_val += RANKS[card]

        # Sort by the count of each card
        count_desc = sorted(count.items(), key=lambda v: -v[1])

        # Create a hand 'value' based on the card count
        # Only the first 5 chars are relevant as each hand is 5 cards
        hand_val = "".join(str(v[1]) for v in count_desc)[:5]

        ranked.append((hand, hand_val, rank_val, bid))
        count = count.fromkeys(count, 0)

    # Finally, sort by hand then by rank
    ranked = sorted(ranked, key=lambda x: (x[1], x[2]), reverse=True)

    return [(v[0], v[3]) for v in ranked] # (hand, bid)


def parse_hands(input: list[str]) -> list[tuple[str, int]]:
    hands = []
    for line in input:
        match = re.match(r"(\w{5}) (\d+)", line)
        if match:
            hands.append((match.group(1), int(match.group(2))))
    return hands # (hand, bid)


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        hands = parse_hands(doc.readlines())
        hands = rank(hands)
        print(calculate_winnings(hands))


if __name__ == "__main__":
    main()
