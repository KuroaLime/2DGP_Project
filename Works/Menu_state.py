import game_framework
from pico2d import *
import menu_world
import play_state
from phone_window import Phone_boarder
from phone_background import Phone_background
from phone_window_option import *
from cursor import Cursor

Menu_window = None
Menu_background = None
Menu_Cursor =None
Menu_option = []
def enter():
    hide_cursor()
    global Menu_window,Menu_background,Menu_Cursor

    Menu_window = Phone_boarder()
    Menu_background = Phone_background()
    Menu_option = [Phone_option_instruction(),Phone_option_music(), Phone_option_soundEffect(), Phone_option_voice(), Phone_option_language(), Phone_option_subtitle(), Phone_option_textSpeed(),  Phone_option_save_exit()]
    Menu_Cursor= Cursor()

    menu_world.add_object(Menu_background, 0)
    menu_world.add_object(Menu_window, 1)
    for i in range(len(Menu_option)):
        menu_world.add_object(Menu_option[i], 2)
    menu_world.add_object(Menu_Cursor,2)

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
                case pico2d.SDLK_s:
                    if Menu_Cursor.my_button_dir < 6:
                        Menu_Cursor.my_button_dir += 1
                case pico2d.SDLK_w:
                    if Menu_Cursor.my_button_dir >0:
                        Menu_Cursor.my_button_dir -= 1