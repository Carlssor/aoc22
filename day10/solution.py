import os
from typing import Generator


NOOP = "noop"
ADDX = "addx"


class Solver:
    def __init__(self):
        self._instructions = self._read_input().splitlines()


    def _read_input(self) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
            return f.read()


    def _run_program(self) -> Generator[tuple[int, int], None, None]:
        cycle_number = 1
        register_value = 1
        for instruction in self._instructions:
            instruction_name = instruction.split()[0]
            if instruction_name == NOOP:
                cycles_to_run = 1
            elif instruction_name == ADDX:
                cycles_to_run = 2
                instruction_argument = int(instruction.split()[1])
            else:
                raise RuntimeError(f"Unknown instruction, '{instruction_name}'")
            for _ in range(cycles_to_run):
                yield cycle_number, register_value
                cycle_number += 1
            if instruction_name == ADDX:
                register_value += instruction_argument


    def solve_puzzle_1(self) -> int:
        cycles_to_check = [20, 60, 100, 140, 180, 220]
        sum_signal_strength = 0
        for cycle_number, register_value in self._run_program():
            if cycle_number in cycles_to_check:
                sum_signal_strength += (cycle_number * register_value)
        return sum_signal_strength


    def solve_puzzle_2(self) -> None:
        drawn = [["."] * 40 for _ in range(6)]
        for cycle_number, register_value in self._run_program():
            pixel_number = cycle_number - 1
            x = pixel_number % 40
            y = pixel_number // 40
            if x - 1 <= register_value <= x + 1:
                drawn[y][x] = "#"
        for line in drawn:
            print("".join(line))


if __name__ == "__main__":
    print(f"Solution puzzle 1: {Solver().solve_puzzle_1()}")
    print(f"Solution puzzle 2:")
    Solver().solve_puzzle_2()