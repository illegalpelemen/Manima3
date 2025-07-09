print("hello world")
from manim import *
class Spheres(ThreeDScene):
    def construct(self):
        anim = Create(Sphere())
        self.play(anim)
        self.wait(10)
