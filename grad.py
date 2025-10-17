from manim import *
import numpy as np
import random

class Gradient(Scene):
    def construct(self):
        self.svx = 2
        self.svy = 1

        # создаём начальный массив
        a = np.linspace(100, 0, 100).reshape(100, 1)
        imageArray = np.repeat(a, 200, axis=1).astype(np.uint8)
        self.image = ImageMobject(imageArray).scale(2)

        self.add(self.image)
        self.image.add_updater(self.newimage)
        self.wait(5)

    def newimage(self, mob, dt):
        # делаем лёгкие случайные колебания
        shift = random.uniform(-0.1, 0.1)
        y = np.linspace(100, 0, 100).reshape(100, 1)
        y = y + np.sin(self.time + y * 0.1) * 10 * shift
        imageArray = np.repeat(y, 200, axis=1).astype(np.uint8)
        mob.set_image(imageArray)