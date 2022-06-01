import pygame as pg
import os
class Ball:
    bg = pg.image.load(os.path.join('Assets', 'AZ.jpg'))
    ball_image = pg.transform.scale(bg, (20, 20))
    x_plus = -1
    y_plus = -1
    def __init__(self, x , y, win, count):
        self.x = x
        self.y = y
        self.win = win
        self.count = count

    def show(self):
        self.win.blit(self.ball_image, (self.x,self.y))

    def TColl(self, all_blocks, i ,j):
        
        if(self.y == all_blocks[i][j].y + 30):
            self.y_plus *= -1
            all_blocks[i][j].hp -= 1
        elif(self.y + 20 == all_blocks[i][j].y):
            self.y_plus *= -1
            all_blocks[i][j].hp -= 1
        elif(self.x + 20 == all_blocks[i][j].x):
            self.x_plus *= -1
            all_blocks[i][j].hp -= 1
        elif(self.x == all_blocks[i][j].x + 30):
            self.x_plus *= -1
            all_blocks[i][j].hp -= 1
        else:
            all_blocks[i][j].hp -= 1
            self.x_plus *= -1
            self.y_plus *= -1

    def check_blocks(self, all_blocks):
        for i in range(30):
            for j in range(10):
                XColl = False
                YColl = False
                if ((self.x + 20 >= all_blocks[i][j].x) and (self.x <= all_blocks[i][j].x + 30)):
                    XColl = True
                if ((self.y + 20 >= all_blocks[i][j].y) and (self.y <= all_blocks[i][j].y + 30)):
                    YColl = True
                if(all_blocks[i][j].hp > 0 and (XColl and YColl)):
                    self.TColl(all_blocks, i ,j)
                    if (all_blocks[i][j].hp == 0):
                        self.count -= 1
                    return
                    

    def physics(self, all_blocks, platforms):
        #Платформа
        self.x += self.x_plus
        self.y += self.y_plus
        if(platforms.x - 20 <= self.x <= platforms.x + 100 and platforms.y == self.y + 20):
            if(platforms.x - 20 <= self.x <= platforms.x + 10 or platforms.x + 71 <= self.x <= platforms.x + 100):
                if(self.x_plus > 0):
                    self.x_plus = 1
                else:
                    self.x_plus = -1
                self.y_plus *= -1
            elif(platforms.x + 11 <= self.x <= platforms.x + 70):
                if(self.x_plus > 0):
                    self.x_plus = 2
                else:
                    self.x_plus = -2
                self.y_plus *= -1
        elif(self.x <= 0 or self.x >= 880):
            self.x_plus *= -1
        elif(self.y >= 600 or self.y == 0):
            self.y_plus *= -1
        #Блоки
        if(self.x):
            self.check_blocks(all_blocks)
            
        

    