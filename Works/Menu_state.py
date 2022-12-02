import game_framework
from pico2d import *
import menu_world
import play_state
from phone_window import Phone_boarder
from phone_background import Phone_background
from phone_window_option import *
import server


def enter():
    hide_cursor()

    server.Menu_window = Phone_boarder()
    server.Menu_background = Phone_background()
    server.Menu_option = [Phone_option_music(), Phone_option_soundEffect(), Phone_option_voice(),  Phone_option_save_exit()]


    menu_world.add_object(server.Menu_background, 0)
    menu_world.add_object(server.Menu_window, 1)
    menu_world.add_objects(server.Menu_option, 2)

def exit():
    pass

def update():
    for game_object in menu_world.all_objects():
        game_object.update()
def draw():
    clear_canvas()
    draw_menu()
    update_canvas()

def draw_menu():
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
                    if server.Menu_button_location < 3:
                        server.Menu_button_location += 1
                case pico2d.SDLK_w:
                    if server.Menu_button_location >0:
                        server.Menu_button_location -= 1
                case pico2d.SDLK_j:
                    if server.Menu_button_location == 0:
                        pass
                    elif server.Menu_button_location == 1:
                        pass
                    elif server.Menu_button_location == 2:
                        pass
                    elif server.Menu_button_location == 3:
                        pass