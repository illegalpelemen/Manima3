
from manim import *

class GraphCreate(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            axis_config={"include_numbers": True}
        )
        graph = plane.plot(lambda x: x**2, color=RED)

        self.add(plane)
        self.play(Create(graph), run_time=3)  # график рисуется за 3 секунды
        self.wait()

