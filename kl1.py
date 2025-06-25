print("hello world")
from manim import *

class SquareToCircle(ThreeDScene):
    def construct(self):
        sphere = Sphere(fill_color=RED,fill_opacity=1)
        sphere.set_shade_in_3d(True)
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
        anim = Create(sphere)
        fadeout = FadeOut(sphere)
        circle_path = Circle(2)
        orbit = MoveAlongPath(sphere,circle_path)
        self.play(anim)
        self.play(orbit,Rotate(self.renderer.get_frame(),30 * DEGREES,UP),

                  run_time= 10)

        self.play(fadeout)
