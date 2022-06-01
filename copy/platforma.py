import pygame as pg
class Platform:
    def __init__(self, x , y, win):
        self.x = x
        self.y = y
        self.win = win
        #pass
    def show(self):
        pg.draw.rect(self.win, (0, 0, 255), [self.x , self.y , 100, 10])