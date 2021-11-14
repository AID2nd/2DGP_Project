from pico2d import *

# Game object class here

class Background:
    def __init__(self):
        self.image = load_image('spring.png')

    def draw(self):
        self.image.draw(400, 300)

class Grass:
    def __init__(self): # 생성자(객체의 속성에 대한 초기값을 설정해주는 함수). __init__ 이게 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Mokoko:
    def __init__(self):
        self.image = load_image('mokoko_animation2.png')
        self.x, self.y = 0, 90
        self.frame = 0

    def update(self):   # 모코코 애니메이션
        if(dir>0):
            self.image = load_image('mokoko_animation2.png')
        elif(dir<0):
            self.image = load_image('mokoko_animation3.png')

        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    global dir
    global injump
    if injump == -2:
        injump = 0      # 일단 대충 버그수정
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_SPACE:
                if injump != -1:
                    injump += 1
                # print(injump)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_SPACE:
                if injump != -1:
                    injump -= 2
                # print(injump)



# initialization code

open_canvas()

background1 = Background()  # 배경 객체 생성
grass1 = Grass()    # 잔디 객체 생성
mokoko = Mokoko()   # 모코코 객체(플레이어) 생성

running = True
x = 800 // 2
frame = 0
dir = 0     # -1 left, +1 right
injump = 0  # -1 낙하중, +1 점프중


# game main loop code

while running:
    handle_events()     # 키 입력 받아들이는 처리..

    # Game logic
    if dir == -1:
        mokoko.x -= 3
    elif dir == 1:
        mokoko.x += 3

    if injump == 1:
        mokoko.y += 15
    if injump == -1:
        mokoko.y -= 15
        if mokoko.y <= 90:
            injump += 1
            # print(injump)

    mokoko.update()     # 모코코의 상호작용


    # Game drawing
    clear_canvas()
    background1.draw()
    grass1.draw()
    mokoko.draw()


    update_canvas()
    
    delay(0.01)     # 너무 빠르면 딜레이좀


# finalization code
