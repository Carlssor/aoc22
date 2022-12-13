import functools
import itertools
import math
import os
from typing import Union


class Solver:
    def __init__(self):
        self._packet_pairs = [[]]
        for line in self._read_input().splitlines():
            if len(line.strip()) == 0:
                self._packet_pairs.append([])
                continue
            self._packet_pairs[-1].append(eval(line))


    def _read_input(self) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
            return f.read()


    def _fix_types(self, left: Union[list, bool], right: Union[list, bool]) -> tuple:
        if type(left) == type(right):
            return left, right
        if isinstance(left, int):
            return [left], right
        if isinstance(right, int):
            return left, [right]
        raise ValueError(f"Unsupported types, {type(left)} and {type(right)}")


    def _check_pair_correct_order(self, left: list, right: list) -> bool:
        for left_value, right_value in itertools.zip_longest(left, right):
            if left_value is None:
                return True
            if right_value is None:
                return False
            left_value, right_value = self._fix_types(left_value, right_value)
            if type(left_value) == type(right_value) == int:
                if left_value == right_value:
                    continue
                return left_value < right_value
            if type(left_value) == type(right_value) == list:
                list_compare_result = self._check_pair_correct_order(left_value, right_value)
                if list_compare_result is not None:
                    return list_compare_result
        return None


    def _compare_packets(self, left: list, right: list) -> int:
        return -1 if self._check_pair_correct_order(left, right) else 1


    def solve_puzzle_1(self) -> int:
        sum_of_pair_numnbers_in_correct_order = 0
        for pair_number, pair in enumerate(self._packet_pairs, 1):
            pair_in_correct_order = self._check_pair_correct_order(*pair)
            if pair_in_correct_order is None:
                raise RuntimeError(f"Could not find a solution for pair {pair_number}.")
            if pair_in_correct_order:
                sum_of_pair_numnbers_in_correct_order += pair_number
        return sum_of_pair_numnbers_in_correct_order


    def solve_puzzle_2(self) -> int:
        all_packets = []
        divider_packets = [[[2]], [[6]]]
        for pair in self._packet_pairs:
            all_packets.extend(pair)
        all_packets.extend(divider_packets)
        all_packets.sort(key=functools.cmp_to_key(self._compare_packets))
        divider_packet_indicies = [(all_packets.index(divider_packet) + 1) for divider_packet in divider_packets]
        return math.prod(divider_packet_indicies)


if __name__ == "__main__":
    print(f"Solution puzzle 1: {Solver().solve_puzzle_1()}")
    print(f"Solution puzzle 2: {Solver().solve_puzzle_2()}")