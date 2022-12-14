import enum
import os
from typing import Union


class Content(enum.Enum):
    AIR = "."
    ROCK = "#"
    SAND = "o"
    SAND_POUR = "+"


class Position:
    def __init__(self, x: int, y: int, content: Content):
        self.x = x
        self.y = y
        self.content = content


    def __str__(self) -> str:
        return f"({self.x}, {self.y}): {self.content}"


    def __hash__(self) -> int:
        return hash(str(self))


    @property
    def coords(self) -> tuple[int]:
        return (self.x, self.y)



class Solver:
    def __init__(self):
        self._known_positions = dict()
        self._sand_pour_position = Position(500, 0, Content.SAND_POUR)
        self._max_y = self._sand_pour_position.y
        self._grid_size = 0


    def _with_prepared_input(func):
        def inner(self, *args, **kwargs):
            self._known_positions.clear()
            self._add_positions(self._sand_pour_position)
            _min_x = _max_x = self._sand_pour_position.x
            self._max_y = self._sand_pour_position.y
            for line in self._read_input().splitlines():
                positions = []
                for coordinates in line.split(" -> "):
                    x, y = [int(val) for val in coordinates.split(",")]
                    positions.append(Position(x, y, Content.ROCK))
                self._add_positions(positions)
                self._max_y = max(self._max_y, *[position.y for position in positions])
                _min_x = min(_min_x, *[position.x for position in positions])
                _max_x = max(_max_x, *[position.x for position in positions])
                for position_index, current_position in enumerate(positions[1:], 1):
                    self._add_positions(self._calculate_positions_between(positions[position_index - 1], current_position))
            self._grid_size = (_max_x - _min_x + 1) * (self._max_y + 1)
            return func(self, *args, **kwargs)
        return inner


    def _read_input(self) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
            return f.read()


    def _add_positions(self, positions: Union[list[Position], Position]) -> None:
        if not hasattr(positions, "__iter__"):
            positions = [positions]
        for position in positions:
            self._known_positions[position.coords] = position


    def _calculate_positions_between(self, position_1: Position, position_2: Position) -> list[Position]:
        if position_1.x == position_2.x:
            start_y, end_y = sorted([position_1.y, position_2.y])
            return [Position(position_1.x, y, Content.ROCK) for y in range(start_y + 1, end_y)]
        if position_1.y == position_2.y:
            start_x, end_x = sorted([position_1.x, position_2.x])
            return [Position(x, position_1.y, Content.ROCK) for x in range(start_x + 1, end_x)]


    def _spawn_sand(self) -> Position:
        spawn_x = self._sand_pour_position.x
        spawn_y = self._sand_pour_position.y
        return Position(spawn_x, spawn_y, Content.SAND)


    def _check_if_grid_exhausted(self) -> None:
        if len(self._known_positions) > self._grid_size * self._max_y:
            raise RuntimeError("Grid exhausted")


    def _check_if_position_is_outside_grid(self, position: Position) -> bool:
        return position.y > self._max_y


    def _try_move_sand(self, sand: Position, with_floor: bool=False) -> bool:
        sand_x, sand_y = sand.coords
        new_y = sand_y + 1
        if with_floor and new_y >= self._max_y + 2:
            return False
        for new_x in (sand_x, sand_x - 1, sand_x + 1):
            if (new_x, new_y) not in self._known_positions:
                sand.x = new_x
                sand.y = new_y
                return True
        return False


    @_with_prepared_input
    def solve_puzzle_1(self) -> int:
        sand_has_fallen_into_void = False
        number_of_sands = 0
        while not sand_has_fallen_into_void:
            self._check_if_grid_exhausted()
            current_sand = self._spawn_sand()
            sand_moving = True
            while sand_moving:
                if self._check_if_position_is_outside_grid(current_sand):
                    sand_has_fallen_into_void = True
                    break
                if self._try_move_sand(current_sand):
                    continue
                number_of_sands += 1
                self._add_positions(current_sand)
                sand_moving = False
        return number_of_sands


    @_with_prepared_input
    def solve_puzzle_2(self) -> int:
        sand_poring_blocked = False
        number_of_sands = 0
        while not sand_poring_blocked:
            self._check_if_grid_exhausted()
            current_sand = self._spawn_sand()
            sand_moving = True
            while sand_moving:
                if self._try_move_sand(current_sand, True):
                    continue
                if current_sand.coords == self._sand_pour_position.coords:
                    sand_poring_blocked = True
                number_of_sands += 1
                self._add_positions(current_sand)
                sand_moving = False
        return number_of_sands


if __name__ == "__main__":
    print(f"Solution puzzle 1: {Solver().solve_puzzle_1()}")
    print(f"Solution puzzle 2: {Solver().solve_puzzle_2()}")