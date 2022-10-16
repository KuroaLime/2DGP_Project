import pico2d
import game_framework

import logo_state
import play_state
import title_state

from canvas_size import *

pico2d.open_canvas(WID,HEI)
game_framework.run(play_state)

pico2d.close_canvas()

