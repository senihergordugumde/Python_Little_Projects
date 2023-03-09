import pygame
class Player():
    def __init__(self,x,y,width,height,screen,vel,rectangle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.left = False
        self.right = False
        self.vel = vel
        self.rectangle = rectangle
    def move(self):
        if self.right:
            self.x += self.vel
        if self.left:
            self.x -= self.vel

    def draw(self):
        self.rectangle = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(self.screen,(255,255,255),self.rectangle)
