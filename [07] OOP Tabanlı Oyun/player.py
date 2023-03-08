import pygame
class Player():
    def __init__(self,x,y,width,height,screen,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.left = False
        self.right = False
        self.vel = vel
    def move(self):
        if self.right:
            self.x += 1
        if self.left:
            self.x -= 1

    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(self.x,self.y,self.width,self.height))
