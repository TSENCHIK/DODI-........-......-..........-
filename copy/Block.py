import pygame as pg
import os
pg.init()
class Block:
    bg = pg.image.load(os.path.join('Assets', 'viktor.jpg'))#выбрать другое фото
    block_image = pg.transform.scale(bg, (30, 30))
    hp = 1
    tochki_x = [0 , 0]
    tochki_y = [0 , 0]
    def __init__(self, x , y, win):
        self.x = x
        self.y = y
        self.win = win
 
    def show(self):
        if (self.hp > 0):
            self.win.blit(self.block_image, (self.x,self.y) )

class X2Block(Block):
    bg = pg.image.load(os.path.join('Assets', 'vk_0.jpg'))#выбрать другое фото
    block_image = pg.transform.scale(bg, (30, 30))
    bg = pg.image.load(os.path.join('Assets', 'viktor.jpg'))#выбрать другое фото
    block_image2 = pg.transform.scale(bg, (30, 30))
    hp = 2
    def show(self):
        if(self.hp>0):
            if(self.hp == 1):
                self.win.blit(self.block_image2, (self.x,self.y))
            else:
                self.win.blit(self.block_image, (self.x,self.y))


    
    