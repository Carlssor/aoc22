import os


class Position:
    def __init__(self):
        self._x = 0
        self._y = 0


    def __str__(self) -> str:
        return f"({self._x}, {self._y})"


    def __hash__(self) -> int:
        return hash(str(self))


    def move_one(self, direction: str) -> None:
        if direction == "R":
            self._x += 1
        elif direction == "L":
            self._x -= 1
        elif direction == "U":
            self._y += 1
        elif direction == "D":
            self._y -= 1
        else:
            raise RuntimeError(f"Unknown direction, '{direction}'")


    def move_towards(self, position: "Position") -> None:
        x_position_diff = position._x - self._x
        y_position_diff = position._y - self._y
        if abs(x_position_diff) > 1 or abs(y_position_diff) > 1:
            if x_position_diff != 0:
                self._x += 1 if x_position_diff > 0 else -1
            if y_position_diff != 0:
                self._y += 1 if y_position_diff > 0 else -1



class Solver:
    def __init__(self):
        self._moves = []
        for line in self._read_input().splitlines():
            direction, length = line.split()
            self._moves.append([direction, int(length)])


    def _read_input(self) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
            return f.read()


    def solve_puzzle_1(self) -> int:
        tail_positions = set()
        head_position = Position()
        tail_position = Position()
        tail_positions.add(tail_position)
        for (direction, length) in self._moves:
            for _ in range(length):
                head_position.move_one(direction)
                tail_position.move_towards(head_position)
                tail_positions.add(tail_position)

        return len(tail_positions)


    def solve_puzzle_2(self) -> int:
        tail_positions = set()
        knot_positions = [Position() for _ in range(10)]
        tail_positions.add(knot_positions[-1])
        for (direction, length) in self._moves:
            for _ in range(length):
                knot_positions[0].move_one(direction)
                for previous_knot_index, knot in enumerate(knot_positions[1:]):
                    knot.move_towards(knot_positions[previous_knot_index])
                tail_positions.add(knot_positions[-1])
        return len(tail_positions)


if __name__ == "__main__":
    print(f"Solution puzzle 1: {Solver().solve_puzzle_1()}")
    print(f"Solution puzzle 2: {Solver().solve_puzzle_2()}")