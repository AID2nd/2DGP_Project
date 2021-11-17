import game_framework
from pico2d import *
from rock import Rock
import game_world

# Mokoko Run Speed
PIXEL_PER_METER = (10.0 / 0.3)                      # 현실 1미터의 길이(약 33픽셀)
RUN_SPEED_KMPH = 20.0                               # 시속 20km
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)    # 1분간 달리는 m거리
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)              # 1초간 달리는 m거리
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)   # 1초간 달리는 픽셀거리

# Mokoko Action Speed
TIME_PER_ACTION = 0.5                               # 1개의 액션을 하는데 걸리는 시간
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION             # 일정 시간 동안 할 수 있는 액션의 양
FRAMES_PER_ACTION = 8                               # 1개의 액션을 하는데 걸리는 프레임



# Mokoko Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, A_DOWN, S_DOWN = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN
}


# Mokoko States

class NormalState:        # 일반적인 상태

    def enter(mokoko, event):
        if event == RIGHT_DOWN:
            mokoko.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mokoko.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mokoko.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mokoko.velocity += RUN_SPEED_PPS
        mokoko.dir = clamp(-1, mokoko.velocity, 1)  # mokoko.velocity의 최솟값과 최댓값을 -1과 1 범위로 한정하여 방향으로 설정해줌

    def exit(mokoko, event):
        if event == A_DOWN:
            mokoko.throw_rock()
        elif event == S_DOWN:
            mokoko.y += 50
        pass

    def do(mokoko):
        mokoko.frame = (mokoko.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mokoko.x += mokoko.velocity * game_framework.frame_time
        mokoko.x = clamp(25, mokoko.x, 1600 - 25)

    def draw(mokoko):
        if mokoko.dir == 1 or (mokoko.dir == 0 and mokoko.lastdir == 1):
            mokoko.image.clip_draw(int(mokoko.frame) * 50, 50, 50, 50, mokoko.x, mokoko.y)
            mokoko.lastdir = 1
        elif mokoko.dir == -1 or (mokoko.dir==0 and mokoko.lastdir == -1):
            mokoko.image.clip_draw(int(mokoko.frame) * 50, 0, 50, 50, mokoko.x, mokoko.y)
            mokoko.lastdir = -1


    print('NormalState')


class SuperState:

    def enter(mokoko, event):
        if event == RIGHT_DOWN:
            mokoko.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mokoko.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mokoko.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mokoko.velocity += RUN_SPEED_PPS
        mokoko.dir = clamp(-1, mokoko.velocity, 1)

    def exit(mokoko, event):
        if event == S_DOWN:
            mokoko.y -= 50
        pass

    def do(mokoko):
        mokoko.frame = (mokoko.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mokoko.x += RUN_SPEED_PPS * game_framework.frame_time * 2   # 오른쪽 방향 고정으로 2배속
        mokoko.x = clamp(25, mokoko.x, 1600 - 25)

    def draw(mokoko):
        mokoko.superimage.clip_draw(int(mokoko.frame) * 0, 0, 210, 210, mokoko.x, mokoko.y)

    print('SuperState')






next_state_table = {
    NormalState: {RIGHT_UP: NormalState, LEFT_UP: NormalState, RIGHT_DOWN: NormalState, LEFT_DOWN: NormalState, A_DOWN: NormalState, S_DOWN: SuperState},
    SuperState: {RIGHT_UP: SuperState, LEFT_UP: SuperState, LEFT_DOWN: SuperState, RIGHT_DOWN: SuperState, A_DOWN: SuperState, S_DOWN: NormalState}
}



class Mokoko:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('mokoko_animations.png')
        self.superimage = load_image('super.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1            # 방향
        self.lastdir = 1        # 마지막으로 움직인 방향(정지상태일때 캐릭터가 바라볼 방향을 지정해줌)
        self.velocity = 0       # 속력
        self.frame = 0
        self.event_que = []
        self.cur_state = NormalState
        self.cur_state.enter(self, None)


    def throw_rock(self):
        rock = Rock(self.x, self.y, self.lastdir*25)
        game_world.add_object(rock, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 40, 'rock: unlimit', (0, 0, 255))
        # 이 부분 나중에 맵으로 빼야함
        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

