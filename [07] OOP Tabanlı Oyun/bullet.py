import pygame
from blocks import *
class Bullet(Blocks):

    def __init__(self,screen,x,y,width,height):
        super().__init__(screen,x,y,width,height)
        self.bullets = []
        self.rect = pygame.Rect(self.x ,self.y,self.width,self.height)


    def create(self):

          self.bullet = pygame.Rect(self.x ,self.y,self.width,self.height)
          self.bullets.append(self.bullet)
    def fire(self):
       for bullet in self.bullets:
           bullet[1] -= 2




    def draw(self):
        for bullet in self.bullets:

            self.rect=pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(bullet[0],bullet[1],self.width,self.height))
