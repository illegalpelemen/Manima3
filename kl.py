import random
from manim import *

y = 0.3
id_x = []

def graphic(x):
    global y, id_x

    rand = random.choice([0.1, -0.1])
    y = y + rand
    if round(y,2) == 0:
        id_x.append(x)

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
        for i in id_x:
            self.add(Dot([i,0,0],color=BLUE))
        self.add(text.next_to(dot, UP))
        print(id_x)
        self.play(Create(graph), run_time=3)  # график рисуется за 3 секунды
        self.wait()
