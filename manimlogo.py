from manim import *
class ManimLoga(Scene):
    def construct(self):
        m = MathTex(r'\mathbb{M}',fill_color = WHITE).scale(7)
        move_m = m.animate.shift(2.25 * LEFT + 1.5 * UP)
        square = Square(fill_color=GREEN_D)
        move_square = square.animate.shift(UP)
        circle = Circle(fill_color = RED_D)
        move_circle = circle.animate.shift(LEFT)
        triangle = Triangle(fill_color=BLUE_D)
        move_triangle = triangle.animate.shift(RIGHT)
        self.camera.background_color = "#ece6e2"
        self.play(Create(m),Create(circle))
        self.play(Create(square),Create(triangle))
        self.play(move_m,move_circle)
        self.play(move_square,move_triangle)
        logo = VGroup(triangle,square,circle,m)
        self.play(logo.animate.move_to(ORIGIN))
        self.play(logo.animate.set_fill(opacity=1))
