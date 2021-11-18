from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('block1.png')

    def update(self):
        pass

    def draw(self):
        for i in range(18, 1000, 33):
            self.image.draw(i, 0)
        for i in range(18, 1000, 33):
            self.image.draw(i, 35)

        for i in range(1090, 1650, 33):
            self.image.draw(i, 0)
        for i in range(1090, 1650, 33):
            self.image.draw(i, 35)