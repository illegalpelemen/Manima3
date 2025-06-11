print("hello world")
from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
class SquareToCircle(ThreeDScene):
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
        #circle = Circle(color=YELLOW).shift(LEFT * 2)
        #self.add(circle)
        square = Square(fill_color= YELLOW,fill_opacity=1)
        square1 = Square(fill_color= RED,fill_opacity=1)
        axes = Axes()
        self.add(axes)
        self.add(square)
        self.add(square1)
        square1.move_to([0,3,6])
        #self.play(square.animate.move_to(ORIGIN))
        self.wait(3)
        #self.set_camera_orientation(theta= 45)
        self.camera.set_focal_distance(1)
        self.move_camera(theta = 360 * DEGREES,run_time = 6)
        self.wait(3)

