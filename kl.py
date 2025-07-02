print("hello world")
from manim import *
#config.pixel_width = 1920
#config.pixel_height = 1080
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
        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        x_label = Text("X", font_size=24).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("Y", font_size=24).next_to(axes.y_axis.get_end(), UP)
        z_label = Text("Z", font_size=24).next_to(axes.z_axis.get_end(), OUT)
        self.add(axes, x_label, y_label, z_label)
        square = Square(fill_color= YELLOW,fill_opacity=1)
        square1 = Square(fill_color= RED,fill_opacity=1)


        self.add(square)
        self.add(square1)
        square1.move_to([0,3,1])
        #self.play(square.animate.move_to(ORIGIN))
        self.wait(3)
        #self.set_camera_orientation(theta= 45)
        #self.move_camera(phi = 40 * DEGREES,run_time = 3)
        #self.move_camera(theta=-30 * DEGREES, run_time=3)
        anim_phi = self.camera.phi_tracker.animate.set_value(40 * DEGREES)
        anim_theta = self.camera.theta_tracker.animate.set_value(40 * DEGREES)
        moving_square = square.animate.move_to(RIGHT*3+UP*2)

        #self.move_camera(phi=60 * DEGREES, run_time=3)
        self.wait(1)
        self.play(anim_phi,anim_theta,run_time = 10)



        self.wait(3)

