from enum import Enum
import os


SCORE_LOSE = 0
SCORE_DRAW = 3
SCORE_WIN = 6


class Play:
    class _Shape(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def __init__(self, text: str):
        if text in ("A", "X"):
            self.shape = self._Shape.ROCK
        elif text in ("B", "Y"):
            self.shape = self._Shape.PAPER
        elif text in ("C", "Z"):
            self.shape = self._Shape.SCISSORS
        else:
            raise ValueError(f"Unsupported text, {text}")

    @property
    def score(self) -> int:
        return self.shape.value

    def beats(self, other_play: "Play") -> bool:
        return (self.shape == self._Shape.ROCK and other_play.shape == self._Shape.SCISSORS) or \
            (self.shape == self._Shape.PAPER and other_play.shape == self._Shape.ROCK) or \
            (self.shape == self._Shape.SCISSORS and other_play.shape == self._Shape.PAPER)

    def ties(self, other_play: "Play") -> bool:
        return self.shape == other_play.shape


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


total_score = 0


for game_play in read_data.splitlines():
    opponent_play = Play(game_play.split()[0])
    my_play = Play(game_play.split()[1])
    total_score += my_play.score
    if my_play.beats(opponent_play):
        total_score += SCORE_WIN
    elif my_play.ties(opponent_play):
        total_score += SCORE_DRAW
    else:
        total_score += SCORE_LOSE


print(total_score)
