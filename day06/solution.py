import collections
import os
import re


def read_input() -> str:
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        return f.read()


def find_start_sequence(number_unique_chars: int) -> int:
    raw_data = read_input()
    for index in range(number_unique_chars, len(raw_data)):
        sequence = raw_data[index - number_unique_chars: index]
        if len(set(sequence)) == number_unique_chars:
            return index
    else:
        raise RuntimeError("No start sequence found")


if __name__ == "__main__":
    print(f"Solution puzzle 1: {find_start_sequence(4)}")
    print(f"Solution puzzle 1: {find_start_sequence(14)}")