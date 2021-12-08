from pico2d import *

class BackGround:
    def __init__(self):
        self.spring = load_image('back_spring.png')
        self.mushroom = load_image('mushroom.png')

    def update(self):
        pass

    def draw(self):
        mushroom0 = 1
        self.spring.draw(0, 0)
        if mushroom0 == 1:
            self.mushroom.draw(1400, 70)