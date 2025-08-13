from manim import *
class DifferentRotations(ThreeDScene):
    def construct(self):
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
        z_label = Text("OUT", font_size=24).next_to(axes.z_axis.get_end(), OUT)
        self.add(axes, x_label, y_label, z_label)
        left_square = Square(color=BLUE, fill_opacity=0.7)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        anim_phi = self.camera.phi_tracker.animate.set_value(40 * DEGREES)
        anim_theta = self.camera.theta_tracker.animate.set_value(40 * DEGREES)
        self.play(anim_phi, anim_theta, run_time=10)

        self.play(
            # left_square.animate.rotate(DEGREES * 120), \
            Rotate(left_square,DEGREES * 120),
            run_time=20
        )
        self.wait()