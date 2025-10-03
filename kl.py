import random
from manim import *

y = 0.3
id_x = None

def graphic(x):
    global y, id_x

    rand = random.choice([0.1, -0.1])
    y = y + rand
    print(y)
    if round(y,2) == 0:
        id_x = x

    return float(y)


class GraphCreate(Scene):
    def construct(self):
        global y
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_numbers": True}
        )
        graph = plane.plot(graphic, color=RED)

        # print(coords)
        dot = Dot([0, 3, 0], color=BLUE)
        text = Text(str(round(y, 2)), color=BLUE)
        self.add(plane, dot)
        if id_x is not None:
            self.add(Dot([id_x,0,0],color=BLUE))
        self.add(text.next_to(dot, UP))
        self.play(Create(graph), run_time=3)  # график рисуется за 3 секунды
        self.wait()
