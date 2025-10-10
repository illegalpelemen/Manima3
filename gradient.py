from manim import *
class Gradient(Scene):
    def construct(self):
        svx =
        svy =
        a= []
        for q in range(100):
            b = []
            for i in range(200):
                b.append(i)
            a.append(b)
        for s in range(100):
            b = []
            for d in range(500):
                b.append(d)
            a.append(b)
        imageArray = np.uint8(a)
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, color=GREEN)
        self.add(image, image.background_rectangle)