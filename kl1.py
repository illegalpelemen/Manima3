print("hello world")
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle(color = BLUE ,fill_color=RED ,fill_opacity=0.1)
        circle1 = Circle(color=BLUE , fill_color=RED , fill_opacity=0.1)
        square = Square (color = RED , fill_color=BLUE , fill_opacity=0.9)
        sphere = Sphere ( )
        squareanim = Create(circle)
        transformation = Transform(circle, square)
        transformation1 = Transform(circle, circle1)
        transformation2 = Transform(circle1, sphere)
        transformation3 = Transform(sphere, circle)

        fadeout = FadeOut(circle)
        self.play(squareanim)
        self.play(transformation)
        self.play(transformation1)
        self.play(transformation2)
        self.play(transformation3)
        self.play(FadeOut(sphere))
        self.play(fadeout)
