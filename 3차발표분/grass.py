from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('block1.png')

    def update(self):
        pass

    def draw(self):
        for i in range(18, 500, 33):
            self.image.draw(i, 0)
        for i in range(18, 500, 33):
            self.image.draw(i, 35)
        # 500~590 바닥 비어있음
        for i in range(590, 1000, 33):
            self.image.draw(i, 0)
        for i in range(590, 1000, 33):
            self.image.draw(i, 35)
        # 1000~1090 바닥 비어있음
        for i in range(1090, 1900, 33):
            self.image.draw(i, 0)
        for i in range(1090, 1900, 33):
            self.image.draw(i, 35)