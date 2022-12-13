import math
import os


class Solver:
    def __init__(self):
        self._all_trees = []
        for line in self._read_input().splitlines():
            self._all_trees.append([int(height) for height in line])
        self._trees_grid_height = len(self._all_trees)
        self._trees_grid_width = len(self._all_trees[0])


    def _read_input(self) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
            return f.read()


    def _check_tree_visible_from_left(self, row: int, col: int) -> bool:
        current_tree_height = self._all_trees[row][col]
        for check_col in range(col):
            if self._all_trees[row][check_col] >= current_tree_height:
                return False
        return True


    def _check_tree_visible_from_right(self, row: int, col: int) -> bool:
        current_tree_height = self._all_trees[row][col]
        for check_col in range(col + 1, self._trees_grid_width):
            if self._all_trees[row][check_col] >= current_tree_height:
                return False
        return True


    def _check_tree_visible_from_top(self, row: int, col: int) -> bool:
        current_tree_height = self._all_trees[row][col]
        for check_row in range(row):
            if self._all_trees[check_row][col] >= current_tree_height:
                return False
        return True


    def _check_tree_visible_from_bottom(self, row: int, col: int) -> bool:
        current_tree_height = self._all_trees[row][col]
        for check_row in range(row + 1, self._trees_grid_height):
            if self._all_trees[check_row][col] >= current_tree_height:
                return False
        return True


    def _check_viewing_distance_left(self, row: int, col: int) -> int:
        current_tree_height = self._all_trees[row][col]
        viewing_distance = 0
        for check_col in range(col - 1, -1, -1):
            viewing_distance += 1
            if self._all_trees[row][check_col] >= current_tree_height:
                break
        return viewing_distance


    def _check_viewing_distance_right(self, row: int, col: int) -> int:
        current_tree_height = self._all_trees[row][col]
        viewing_distance = 0
        for check_col in range(col + 1, self._trees_grid_width):
            viewing_distance += 1
            if self._all_trees[row][check_col] >= current_tree_height:
                break
        return viewing_distance


    def _check_viewing_distance_up(self, row: int, col: int) -> int:
        current_tree_height = self._all_trees[row][col]
        viewing_distance = 0
        for check_row in range(row - 1, -1, -1):
            viewing_distance += 1
            if self._all_trees[check_row][col] >= current_tree_height:
                break
        return viewing_distance


    def _check_viewing_distance_down(self, row: int, col: int) -> int:
        current_tree_height = self._all_trees[row][col]
        viewing_distance = 0
        for check_row in range(row + 1, self._trees_grid_height):
            viewing_distance += 1
            if self._all_trees[check_row][col] >= current_tree_height:
                break
        return viewing_distance


    def solve_puzzle_1(self) -> int:
        visible_trees = 0
        for row in range(self._trees_grid_width):
            for col in range(self._trees_grid_height):
                if self._check_tree_visible_from_left(row, col) or \
                        self._check_tree_visible_from_right(row, col) or \
                        self._check_tree_visible_from_top(row, col) or \
                        self._check_tree_visible_from_bottom(row, col):
                    visible_trees += 1

        return visible_trees


    def solve_puzzle_2(self) -> int:
        highest_scenic_score = 0
        for row in range(self._trees_grid_width):
            for col in range(self._trees_grid_height):
                scores = [
                    self._check_viewing_distance_left(row, col),
                    self._check_viewing_distance_right(row, col),
                    self._check_viewing_distance_up(row, col),
                    self._check_viewing_distance_down(row, col) 
                    ]
                highest_scenic_score = max(highest_scenic_score, math.prod(scores))
        return highest_scenic_score


if __name__ == "__main__":
    print(f"Solution puzzle 1: {Solver().solve_puzzle_1()}")
    print(f"Solution puzzle 2: {Solver().solve_puzzle_2()}")