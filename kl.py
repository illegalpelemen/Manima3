print("hello world")
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # circle = Circle(color = BLUE ,fill_color=RED ,fill_opacity=0.1)
        # circleeanim = Create(circle)
        # self.add(circle)
        # movingcircle = circle.animate.move_to(RIGHT*3+UP*2)
        # movingcircle1 = circle.animate.move_to(LEFT * 3 )
        # movingcircle2 = circle.animate.move_to(DOWN * 2)
        # self.play(movingcircle)
        # self.play(movingcircle1)
        # self.play(movingcircle2)
        # fadeout = FadeOut(circle)
        #
        # self.play(fadeout)
        circle = Circle(color=YELLOW).shift(LEFT * 2)
        self.add(circle)

        self.play(circle.animate.move_to(ORIGIN))
        self.wait()

        self.play(circle.animate.shift(UP * 2))
        self.wait()

        self.play(circle.animate.to_edge(DOWN))
        self.wait()
