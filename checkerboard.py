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
        amount_of_squares = len(a[0])
        amount_of_squaresy = len(a)
        r = range(0, amount_of_squares, 1)
        for e in r:
            self.add(self.square(amount_of_squares, amount_of_squaresy, e,1))

    def square(self, amount_of_squaresx, amount_of_squaresy, which_squarex,which_squarey):
        scale = 14 / amount_of_squaresx
        scaley = 6 / amount_of_squaresy
        lighted_square = (Square(color=BLUE, side_length=scale)
                          .move_to([which_squarex * scale - 7 + 0.5 * scale, which_squarey * scaley - 0.5* scaley , 0]))
        return lighted_square
