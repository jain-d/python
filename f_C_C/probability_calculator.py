import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents: list[str] = [ball for ball, times in kwargs.items() for _ in range(times)]

    def draw(self, balls_to_draw: int) -> list[str]:
        balls_removed: list[str]
        ball_sack_copy = self.contents.copy()
        if balls_to_draw < len(self.contents):
            balls_removed = [self.contents.pop(random.randint(0, len(self.contents) - 1)) for _ in range(balls_to_draw)]

        else:
            balls_removed = self.contents.copy()
            self.contents.clear()

        self.contents = ball_sack_copy.copy()

        return balls_removed


def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int):
    success: int = 0
    for _ in range(num_experiments):
        match: bool = True
        balls_drawn = hat.draw(num_balls_drawn)
        for ball, times in expected_balls.items():
            if balls_drawn.count(ball) < times:
                match ^= True
        if match:
            success += 1
    return success / num_experiments


"""
hat = Hat(black=6, red=4, green=3)
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
"""

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
