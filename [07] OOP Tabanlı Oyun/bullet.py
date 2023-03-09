import pygame

class Bullet():

    def __init__(self,x,y,width,height,screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.bullets = []

    def create(self):

          self.bullet = pygame.Rect(self.x ,self.y,self.width,self.height)
          self.bullets.append(self.bullet)
    def fire(self):
       for bullet in self.bullets:
           bullet[1] -= 2



    def draw(self):
        for bullet in self.bullets:

              pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(bullet[0]+55,bullet[1],self.width,self.height))