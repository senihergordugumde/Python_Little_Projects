import sys
from player import *
import pygame
from pygame.locals import *
class Main():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        player1 = Player(150, 650, 150, 50, screen,1)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player1.right = True

                    elif event.key == pygame.K_LEFT:
                        player1.left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player1.right = False
                    elif event.key == pygame.K_LEFT:
                        player1.left = False



            screen.fill((0, 0, 0))
            player1.move()
            player1.draw()
            pygame.display.update()


run = Main()
run()
