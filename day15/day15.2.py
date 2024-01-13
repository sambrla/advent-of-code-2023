"""
Advent of Code 2023
Day 15.2
"""

from collections import deque
import re
import sys


def hash(input: str) -> int:
    val = 0
    for c in input:
        val += ord(c)
        val *= 17
        val &= (255) # Use bitwise AND trick (divisor-1) as 256 is a power of 2
    return val


def find(target: str, boxes: list[deque], box: int) -> int:
    for i, b in enumerate(boxes[box]):
        label, _ = b
        if label == target:
            return i
    return -1


def process_seq(seq: list[str], boxes: list[deque]):
    for s in seq:
        m = re.match(r"([a-z]+)(=|-)(\d*)", s)
        if m:
            label, op, f = m.groups()
            box  = hash(label)
            lens = find(label, boxes, box)
            match op:
                # Replace or add lens
                case "=":
                    if lens != -1:
                        boxes[box][lens] = (label, int(f))
                    else:
                        boxes[box].append((label, int(f)))
                # Remove lens
                case "-":
                    if lens != -1:
                        boxes[box].remove(boxes[box][lens])


def focusing_power(boxes: list[deque]) -> int:
    """
    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    The focal length of the lens.
    """
    fp = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            fp += (1 + i) * (j + 1) * lens[1]
    return fp


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <input>".format(sys.argv[0]))

    with open(sys.argv[1]) as doc:
        seq = doc.read().strip().split(",")
        boxes = [deque() for _ in range(256)]
        process_seq(seq, boxes)
        print(focusing_power(boxes))


if __name__ == "__main__":
    main()
