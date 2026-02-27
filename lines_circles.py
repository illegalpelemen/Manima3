from manim import *
class Lines(Scene):
    def construct(self):
        line1 = Line(LEFT,RIGHT)
        dot = Dot(radius=0.2,color=WHITE)
        self.add(line1)
        for q in range(1,5):
            self.play(MoveAlongPath(dot,line1))
            self.wait(1)
            self.play(dot.animate.move_to(line1.start))
            self.wait(1)
            self.play(Rotate(line1,45))
