from manim import *
import random
import trajectories

#to_fill = (v % 2 == 0 and e % 2 !=0) or (e % 2 == 0 and v % 2 !=0)
class Check(Scene):
    def gen_list(self):
        x = 1
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
        self.amount_of_squares = len(a[0])
        self.amount_of_squaresy = len(a)
        r = range(0, self.amount_of_squares, 1)

        for v in range(self.amount_of_squaresy):

            for e in r:
                value = a[v][e]
                to_fill = value != 0
                square_on_grid = self.square(e, v)



                self.add(square_on_grid)
        size,x_coord,y_coord = self.oordinate(0, 0)

        # for d in range(5):
        #     circ = Circle(size * 0.5, BLUE)
        #     _,_,r = self.oordinate(0, d)
        #     self.add(circ.move_to([x_coord,r,0]))
        # #self.add(circ.move_to([x_coord,y_coord,0]))
        #     self.trajectory(circ,[[0,d],[d+1,d]])
        # self.wait(8)
        circ = Circle(size * 0.5,BLUE)
        list_of_trajectories = [[[0,0],[1,0]] ]+[[2,0]]
        self.add(circ.move_to([x_coord,y_coord,0]))

        list_of_trajectories = trajectories.list_of_traject()
        self.trajectory(circ, list_of_trajectories)

    def trajectory(self,c,list_of_movements):
        lists = list_of_movements

        for v in range(1,len(lists)):
            self.play(self.line_draw(c,lists[v-1][0],lists[v-1][1],lists[v][0],lists[v][1] ))

    def line_draw(self,c, x1, y1, x2, y2):
        _,x1,y1 = self.oordinate(x1,y1)
        _, x2, y2 = self.oordinate(x2, y2)
        line = Line([x1,y1,0],[x2,y2,0])
        anim = MoveAlongPath(c,line)
        return anim

    def square(self, which_squarex,which_squarey):
        recommended, x_coord, y_coord = self.oordinate( which_squarex, which_squarey)


        lighted_square = (Square(color=WHITE, side_length=recommended,fill_opacity=0.9)
                           .move_to([x_coord,y_coord,0]))
        return lighted_square
    def oordinate(self,which_squarex,which_squarey):
        scale = 14 / self.amount_of_squares
        scaley = 8 / self.amount_of_squaresy
        if scale > scaley:
            recommended = scaley
        else:
            recommended = scale
        x_coord = which_squarex * recommended - 7 + 0.5 * recommended
        y_coord = -1 * which_squarey * recommended + 4 - 0.5 * recommended

        return recommended, x_coord, y_coord