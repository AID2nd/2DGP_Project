from pico2d import *

class Block1:
    def __init__(self):
        self.image = load_image('block2.png')

    def update(self):
        pass

    def draw(self):
        for i in range(70, 290, 33):
            self.image.draw(i, 400)