from manim import *
import random

#to_fill = (v % 2 == 0 and e % 2 !=0) or (e % 2 == 0 and v % 2 !=0)
class Check(Scene):

    def gen_list(self):
        n = 11
        svx = n
        svy = n
        a = []

        for q in range(svy):
            b = []

            for i in range(svx):
                if i == n // 2 or q == n // 2 or q == i or q+i+1 == n:
                    b.append(1)
                else:
                    b.append(0)

            a.append(b)
        return a

    def construct(self):
        a = self.gen_list()
        amount_of_squares = len(a[0])
        amount_of_squaresy = len(a)
        r = range(0, amount_of_squares, 1)
        for v in range(amount_of_squaresy):

            for e in r:

                value = a[v][e]
                to_fill =  value != 0


                self.add(self.square(amount_of_squares, amount_of_squaresy, e,v,to_fill))


    def square(self, amount_of_squaresx, amount_of_squaresy, which_squarex,which_squarey,to_fill):
        scale = 14 / amount_of_squaresx
        scaley = 8 / amount_of_squaresy
        if scale > scaley:
            recommended = scaley
        else:
            recommended = scale
        if to_fill:
            color = PURPLE_B
        else:
            color = None
        lighted_square = (Square(color=BLUE, side_length=recommended,fill_color= color,fill_opacity=0.9)
                           .move_to([which_squarex * recommended - 7 + 0.5 * recommended  , -1 * which_squarey * recommended + 4 - 0.5* recommended,0]))

        return lighted_square
