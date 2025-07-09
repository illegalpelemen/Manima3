
from manim import *
print(config.renderer)
class SquareToCircle(ThreeDScene):
    def construct(self):
        earth = Sphere()
        #earth.set_style()
        #earth.set_shade_in_3d(True)
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

        anim = Create(earth)
        fadeout = FadeOut(earth)
        circle_path = Circle(2)
        orbit = MoveAlongPath(earth,circle_path)
        # anim_phi = self.camera.phi_tracker.animate.set_value(40 * DEGREES)
        # anim_theta = self.camera.theta_tracker.animate.set_value(40 * DEGREES)
        self.play(anim)
        # self.play(orbit,anim_phi,anim_theta,run_time = 10)

        self.play(fadeout)
