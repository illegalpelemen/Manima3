3import random
from manim import *
from manim.utils.space_ops import rotate_vector


class Vectors(Scene):
    def construct(self):
        #self.add(Vector(RIGHT))
        #math_vector = rotate_vector(RIGHT, DEGREES * 90)

        self.line = Line([-2, -2, 0], [2, 2, 0], color=ORANGE)
        self.line_vector = self.line.get_unit_vector()
        self.moving_vector = Vector(self.line_vector)
        self.brace = Brace(self.line, self.line_vector)

        self.add(self.moving_vector)
        self.x = 1
        self.add(self.line)
        self.add(self.brace)
        self.moving_vector.add_updater(self.newvec)
        self.brace.add_updater(self.newbrac)
        self.wait(16)


    def newvec(self, mob, dt):

        self.x += 5
        self.math_vector = rotate_vector(self.line_vector, DEGREES * self.x)
        moving_vector = Vector(self.math_vector)
        mob.become(moving_vector)


    def newbrac(self,mob):
        brace = Brace(self.line, self.math_vector)
        mob.become(brace)