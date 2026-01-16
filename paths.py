from manim import *
import random

#to_fill = (v % 2 == 0 and e % 2 !=0) or (e % 2 == 0 and v % 2 !=0)
class Check(Scene):
    def gen_list(self):
        x = 9
        y = 5
        svx = x
        svy = y
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

        for v in range(amount_of_squaresy):

            for e in r:
                value = a[v][e]
                to_fill = value != 0
                square_on_grid = self.square(amount_of_squares, amount_of_squaresy, e, v)



                self.add(square_on_grid)
        size,x_coord,y_coord = self.oordinate(amount_of_squares, amount_of_squaresy, 0, 0)
        self.add(Circle(size * 0.5,BLUE).move_to([x_coord,y_coord,0]))


    def square(self, amount_of_squaresx, amount_of_squaresy, which_squarex,which_squarey):
        recommended, x_coord, y_coord = self.oordinate(amount_of_squaresx, amount_of_squaresy, which_squarex, which_squarey)


        lighted_square = (Square(color=WHITE, side_length=recommended,fill_opacity=0.9)
                           .move_to([x_coord,y_coord,0]))
        return lighted_square
    def oordinate(self,amount_of_squaresx, amount_of_squaresy, which_squarex,which_squarey):
        scale = 14 / amount_of_squaresx
        scaley = 8 / amount_of_squaresy
        if scale > scaley:
            recommended = scaley
        else:
            recommended = scale
        x_coord = which_squarex * recommended - 7 + 0.5 * recommended
        y_coord = -1 * which_squarey * recommended + 4 - 0.5 * recommended

        return recommended, x_coord, y_coord