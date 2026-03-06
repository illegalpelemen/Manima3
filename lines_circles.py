from manim import *
class Lines(Scene):
    def construct(self):
        self.line1 = Line(LEFT,RIGHT)
        self.dot1 = Dot(radius=0.2,color=WHITE)
        self.gr1  = Group(self.line1,self.dot1)
        self.x = 0
        self.add(self.gr1)

        self.gr1.add_updater(self.rot)
        self.dot1.add_updater(self.move)
        #self.play(MoveAlongPath(dot1, self.line1))
        #self.play(MoveAlongPath(dot1, self.line1.reverse_direction()))
        self.wait(10)
    def rot(self,mob,dt):
        mob.rotate(DEGREES * 5)
    def move(self,mob,dt):

        self.x += 0.01
        if self.x > 1:
            self.x = 1
        point = self.line1.point_from_proportion(self.x)
        mob.move_to(point)



