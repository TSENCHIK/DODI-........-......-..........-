import pygame as pg
import os
import Block
import platforma
import Ball
import random
pg.init()

WIDTH = 900
HEIGHT = 600
FPS = 120
WIN = pg.display.set_mode((WIDTH, HEIGHT))

run = True
all_blocks = []
smallfont = pg.font.SysFont('Arial.ttf', 32)
bg = pg.image.load(os.path.join('Assets', 'menu_bg.jpg'))
bg_image = pg.transform.scale(bg, (WIDTH, HEIGHT))

current_game_status = 0 #
is_game_new = True

platforms = platforma.Platform(WIDTH/2, HEIGHT/5, WIN)
ball = Ball.Ball(100, 100, WIN, 0)

def key_work(key):
    global current_game_status
    global is_game_new
    if(current_game_status == 1):
        mouse_pos = pg.mouse.get_pos()
        if(mouse_pos[0] < 850 and mouse_pos[0] > 50):
            platforms.x = mouse_pos[0] - 50
    if(current_game_status == 2 or current_game_status == 3
        or current_game_status == 4):
        if(key[pg.K_UP]):
            current_game_status = 1
            is_game_new = True

def mouse_work():
    global current_game_status
    global run
    if (check(0, 0)):
        current_game_status = 1
    elif(check(0, 120)):
        run = False

def check(game_status, height):
    mouse_pos = pg.mouse.get_pos()
    global current_game_status
    if  (
        game_status == current_game_status 
        and WIDTH/2 - 70 <= mouse_pos[0] <= WIDTH/2 + 70 
        and HEIGHT/2 + height <= mouse_pos[1] <= HEIGHT/2 + height + 40
        ):
        return True
    return False

def start_game():
    global all_blocks
    all_blocks = [[''] * 10 for i in range(30)]
    for i in range(30):
        for j in range(10):
            xy = random.randint(1,2)
            if(xy == 1):
                all_blocks[i][j] = Block.Block(i * 30, j * 30, WIN)
            elif(xy==2):
                all_blocks[i][j] = Block.X2Block(i * 30, j * 30, WIN)
    platforms.x = 470
    platforms.y = HEIGHT - 50
    ball.x = 400
    ball.y = 400
    ball.x_plus = -2
    ball.y_plus = -2
    ball.count = 300

def draw_loss():
    text = 'You loss!!!'
    font = pg.font.SysFont('Arial.ttf', 65)
    WIN.blit(font.render(text, True, (0, 255, 0)), (350, 200))
    pg.display.update()

def draw_win():
    text = 'You win!!!'
    font = pg.font.SysFont('Arial.ttf', 65)
    WIN.blit(font.render(text, True, (0, 255, 0)), (350, 200))
    pg.display.update()

def victor_ysh():
    text = 'VITYA TI KUDA'
    font = pg.font.SysFont('Arial.ttf', 100)
    WIN.blit(font.render(text, True, (255, 0, 0)), (200, 200))
    pg.display.update()

def draw_game_window():
    global bg_image
    WIN.blit(bg_image, (0 ,0))
    global all_blocks
    global is_game_new
    global current_game_status

    if(is_game_new):
        start_game()
        is_game_new = False
    ball.physics(all_blocks, platforms)
    for i in range(30):
        for j in range(10):
            all_blocks[i][j].show()
    platforms.show()
    ball.show()
    if ball.y > 575:
        current_game_status = 2
    if ball.count == 0:
        current_game_status = 3
    if ball.x > 900 or ball.x < 0 or ball.y > 600 or ball.y < 0: 
        current_game_status = 4
    pg.display.update()

def draw_menu_button(button_numb):
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    mouse_pos = pg.mouse.get_pos()
    if (
        WIDTH/2 - 70 <= mouse_pos[0] <= WIDTH/2 + 70 
        and HEIGHT/2 + 40*(button_numb) <= mouse_pos[1] <= HEIGHT/2+40*(button_numb+1)
        ):
        pg.draw.rect(WIN,color_light,[WIDTH/2 - 70,HEIGHT/2 + 40 * button_numb,140,40])  
    else:
        pg.draw.rect(WIN,color_dark,[WIDTH/2 - 70,HEIGHT/2 + 40 * button_numb,140,40])

def draw_menu_window():
    global smallfont
    global WIN
    global bg_image
    WIN.blit(bg_image, (0 ,0))
    button_collor = (0, 0, 0)

    menu_texts = (
                smallfont.render('Start game', True, button_collor),
                smallfont.render('Quit', True, button_collor)
                )
    high_fix = 10
    draw_menu_button(0)
    WIN.blit(menu_texts[0], (WIDTH/2 - 57,HEIGHT/2 + high_fix))
    draw_menu_button(3)
    WIN.blit(menu_texts[1], (WIDTH/2 - 25,HEIGHT/2 + 120 + high_fix))

    pg.display.update()

def main():
    global current_game_status
    clock = pg.time.Clock()
    global run
    
    while run:
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_work()

            key_pressed = pg.key.get_pressed()
            key_work(key_pressed)
        if current_game_status == 0:
            draw_menu_window()
        elif current_game_status == 1:
            draw_game_window()
        elif current_game_status == 2:
            draw_loss()
        elif current_game_status == 3:
            draw_win()
        elif current_game_status == 4:
            victor_ysh()

if  __name__ == "__main__":
    main()