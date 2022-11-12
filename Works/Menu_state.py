import game_framework
from pico2d import *
import menu_world
import play_state
from phone_window import Phone_boarder
from phone_background import Phone_background


Menu_window=None
Menu_background=None

def enter():
    hide_cursor()
    global Menu_window,Menu_background

    Menu_window = Phone_boarder()
    Menu_background = Phone_background()

    menu_world.add_object(Menu_window, 1)
    menu_world.add_object(Menu_background, 0)

def exit():
    pass

def update():
    for game_object in menu_world.all_objects():
        game_object.update()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    play_state.draw_world()
    for game_object in menu_world.all_objects():
        game_object.draw()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()