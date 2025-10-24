from manim import *
import random
class Gradient(Scene):
    def gen_list(self,svx,svy):

        a = []
        hh = 255
        for q in range(svy):
            b = []
            for i in range(svx):
                if q == 0 or q == svy-1 or i == 0 or i == svx-1 or q == i or q + i == svy-1:
                    b.append(hh)
                else:
                    b.append(i)

            a.append(b)
        for r in a:
            for x in r:
                print(str(x).zfill(3),end =" ")
            print()
        return a
    def construct(self):

        a = self.gen_list(50,50)


        imageArray = np.uint8(a)
        image = ImageMobject(imageArray).scale(20)
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