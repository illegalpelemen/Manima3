from manim import *

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0.7, tip_shape= StealthTip)
        arrow.add_tip(tip_shape = ArrowTriangleTip,at_start=True)
        dot_end = Dot([2, 2, 0])
        numberplane = NumberPlane(faded_line_ratio=3,axis_config={"include_numbers": True})
        graph = numberplane.plot(self.functons)
        #origin_text = Text('(0, 0)').next_to(dot, DOWN)
        #tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        #self.add(numberplane, dot, arrow, origin_text, tip_text)
        #self.play(Create(arrow),Create(dot),Create(dot_end))
        self.add(numberplane,graph)
        self.play(ShowPassingFlash(graph))
        #self.wait(1)
    def functons (self,x):
        return x * x * x * x - 7*x * 7*x