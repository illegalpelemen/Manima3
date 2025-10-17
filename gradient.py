from manim import *
import random
class Gradient(Scene):
    def construct(self):
        svx = 3
        svy = 3
        a= []


        for q in range(svy):
            b = []
            for i in range(svx):
                b.append(i)
            a.append(b)
        for r in a:
            print(r)


        imageArray = np.uint8(a)
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, color=GREEN)
        self.add(image)
    #     self.image.add_updater(self.newimage)
    #     self.wait(5)
    # def newimage(self,mob,dt):
    #     a = []
    #     for q in range(100, 0, random.randint(-3,-1)):
    #         b = []
    #         for i in range(200):
    #             b.append(q)
    #         a.append(b)
    #
    #     imageArray = np.uint8(a)
    #     image = ImageMobject(imageArray).scale(2)
    #     # image.background_rectangle = SurroundingRectangle(image, color=GREEN)
    #     mob.set_image(image)
e = Gradient()
e.construct()