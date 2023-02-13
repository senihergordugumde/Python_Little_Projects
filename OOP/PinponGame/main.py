
import pygame, sys
import time
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Absolutely Simple Pinpon Game")

class Player1():

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self):
        self.x -= 10

    def draw(self):
        pass



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass


    
    pygame.display.update()