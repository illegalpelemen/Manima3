from manim import *
import random
class Check(Scene):

    def gen_list(self):
        svx = 8
        svy = 8
        a = []

        for q in range(svy):
            b = []

            for i in range(svx):
                b.append(0)


            a.append(b)
        return a
    def construct(self):
        a = self.gen_list()
        c = 7
        r = range(0,c, 1)
        for e in r:

            self.add(Square(color=BLUE).move_to([e+e-6,0,0]))
            print(e)
