import random

import pygame

class Blocks():
    def __init__(self,screen,x,y,width,height):
        self.blocks = []
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.add = 0

    def create(self):
        self.block = pygame.Rect(self.x + self.add,self.y,5,5)
        self.blocks.append(self.block)
        self.add += 18

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen,(255,0,0),pygame.Rect(block[0],block[1],self.width,self.height))
    def move(self):
        for block in self.blocks:
            block[1] += 15