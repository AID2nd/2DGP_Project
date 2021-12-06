from pico2d import *

class BackGround:
    def __init__(self):
        self.spring = load_image('back_spring.png')
        self.coin = load_image('coin.png')
        self.mushroom = load_image('mushroom.png')

    def update(self):
        pass

    def draw(self):
        mushroom0 = 1       # 일단 ㅈㅁ
        self.spring.draw(0, 0)
        for i in range(380, 480, 30):
            self.coin.draw(i, 75)
        for i in range(1180, 1260, 30):
            self.coin.draw(i, 75)
        if mushroom0 == 1:
            self.mushroom.draw(1400, 70)