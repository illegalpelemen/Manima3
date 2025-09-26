import random
from manim import *

x1 = 0


def graphic(x):
    global x1
    rand = random.choice([0.1, -0.1])
    x1 = x1 + rand
    return float(x1)


class GraphCreate(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_numbers": True}
        )
        graph = plane.plot(graphic, color=RED)
        coords = graphic(0)
        print(coords)
        dot = Dot([0, coords, 0], color=BLUE)
        text = Text(str(coords))
        self.add(plane, dot)
        self.add(text.next_to(dot, UP, buff=SMALL_BUFF))
        self.play(Create(graph), run_time=3)  # график рисуется за 3 секунды
        self.wait()
