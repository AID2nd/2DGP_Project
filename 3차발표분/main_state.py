import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mokoko import Mokoko
from grass import Grass
from background import BackGround
from blocks import Block1


name = "MainState"

mokoko = None

def enter():
    global mokoko
    mokoko = Mokoko()
    grass = Grass()
    background = BackGround()
    blocks = Block1()
    game_world.add_object(background, 0)
    game_world.add_object(grass, 0)
    game_world.add_object(blocks, 0)
    game_world.add_object(mokoko, 1)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mokoko.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






