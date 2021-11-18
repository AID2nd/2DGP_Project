from pico2d import *

class BackGround:
    def __init__(self):
        self.image = load_image('back_spring.png')
        self.tempimg1 = load_image('coin.png')
        self.tempimg2 = load_image('mushroom.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(0, 0)
        for i in range(380, 480, 30):
            self.tempimg1.draw(i, 400)
        self.tempimg2.draw(140, 430)