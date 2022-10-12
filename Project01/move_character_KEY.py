from pico2d import *


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

kyoko_dir= 'D:\GIT\2DGP_Project\Project01\Resource\classification\Player\kyoko\run'
kyoko_image=['RCG_Kyoko_run0001_anio.png','RCG_Kyoko_run0002_anio.png','RCG_Kyoko_run0003_anio.png','RCG_Kyoko_run0004_anio.png','RCG_Kyoko_run0005_anio.png','RCG_Kyoko_run0006_anio.png','RCG_Kyoko_run0007_anio.png','RCG_Kyoko_run0008_anio.png'
    ,'RCG_Kyoko_run0009_anio.png','RCG_Kyoko_run0010_anio.png','RCG_Kyoko_run0011_anio.png','RCG_Kyoko_run0012_anio.png','RCG_Kyoko_run0013_anio.png','RCG_Kyoko_run0014_anio.png','RCG_Kyoko_run0015_anio.png','RCG_Kyoko_run0016_anio.png']

def handle_events():
    global Game_running
    global dir_lr, dir_ud
    global last_dir
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_running = False
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_lr += 1
                last_dir = 1
            elif event.key == SDLK_LEFT:
                dir_lr -= 1
                last_dir = -1
            elif event.key == SDLK_UP:
                dir_ud +=1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                Game_running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
               dir_lr-=1
            elif event.key == SDLK_LEFT:
                dir_lr+=1
            elif event.key == SDLK_UP:
                dir_ud-=1
            elif event.key == SDLK_DOWN:
                dir_ud+=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game_running = False

def Animation_change():

    if dir_lr > 0 and dir_ud == 0:
        character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
    elif dir_lr < 0 and dir_ud == 0:
        character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
    elif dir_lr == 0 and dir_ud == 0:
        if last_dir == 1:
            character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
        else:
            character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
    elif dir_ud >0:
        if last_dir == 1:
            character.clip_draw(frame * 40, 70 * 0, 35, 70, x, y)
        else:
            character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
    elif dir_ud <0:
        if last_dir == 1:
            character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
        else:
            character.clip_draw(frame * 40, 70 * 0, 40, 70, x, y)
    delay(0.05)

def stop_search():
    global x,y
    if x<=0:
        x+=5
    elif x>=KPU_WIDTH:
        x-=5
    elif y<=0:
        y+=5
    elif y>=KPU_HEIGHT:
        y-=5

open_canvas(KPU_WIDTH, KPU_HEIGHT)

character=[]

for i in range(len(kyoko_image)):
    character.append = load_image(kyoko_image[i])
kpu_ground = load_image('grass.png')

Game_running = True
dir_ud=0
dir_lr=0
x=800/2
y=800/2

last_dir=0

frame = 0
hide_cursor()


while Game_running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    Animation_change()
    update_canvas()
    frame = (frame + 1) % 8

    x+=dir_lr*5
    y+=dir_ud*5
    handle_events()
    #delay(0.01)
    stop_search()

close_canvas()




