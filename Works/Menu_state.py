import game_framework
from pico2d import *
import menu_world
import play_state
from phone_window import Phone_boarder
from phone_background import Phone_background
from phone_window_option import *
import server
import title_state
from menu_icon import select_Menu_icon,non_select_Menu_icon
def enter():
    hide_cursor()
    if server.Menu_icon == None:
        server.Menu_window = Phone_boarder()
        server.Menu_background = Phone_background()
        server.Menu_option = [Phone_option_music(), Phone_option_soundEffect(), Phone_option_voice(),  Phone_option_save_exit()]
        server.Menu_icon = [select_Menu_icon(), non_select_Menu_icon()]

        menu_world.add_object(server.Menu_background, 0)
        menu_world.add_object(server.Menu_window, 1)
        menu_world.add_objects(server.Menu_option, 2)
        menu_world.add_objects(server.Menu_icon, 2)
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
                case pico2d.SDLK_a:
                    if server.Menu_button_location == 0:
                        if server.music_volume >0:
                            server.Menu_icon[0].x[server.Menu_button_location] -= 2
                            server.Menu_icon[1].x[server.Menu_button_location] -= 2
                            server.music_volume -= 2
                    elif server.Menu_button_location == 1:
                        if server.effect_volume > 0:
                            server.Menu_icon[0].x[server.Menu_button_location] -= 2
                            server.Menu_icon[1].x[server.Menu_button_location] -= 2
                            server.effect_volume -= 2
                    elif server.Menu_button_location == 2:
                        if server.volume > 0:
                            server.Menu_icon[0].x[server.Menu_button_location] -= 2
                            server.Menu_icon[1].x[server.Menu_button_location] -= 2
                            server.volume -= 2
                case pico2d.SDLK_d:
                    if server.Menu_button_location == 0:
                        if server.music_volume < 128:
                            server.Menu_icon[0].x[server.Menu_button_location] += 2
                            server.Menu_icon[1].x[server.Menu_button_location] += 2
                            server.music_volume += 2
                    elif server.Menu_button_location == 1:
                        if server.effect_volume < 128:
                            server.Menu_icon[0].x[server.Menu_button_location] += 2
                            server.Menu_icon[1].x[server.Menu_button_location] += 2
                            server.effect_volume += 2
                    elif server.Menu_button_location == 2:
                        if server.volume < 128:
                            server.Menu_icon[0].x[server.Menu_button_location] += 2
                            server.Menu_icon[1].x[server.Menu_button_location] += 2
                            server.volume += 2
                case pico2d.SDLK_j:
                    if server.Menu_button_location == 3:
                        # game_world.save()
                        game_world.clear()
                        game_framework.change_state(title_state)