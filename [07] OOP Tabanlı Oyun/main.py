import sys
from player import *
from bullet import *
import pygame
from pygame.locals import *
class Main():

    def __init__(self):

        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        player1 = Player(150, 650, 150, 50, screen,1)
        bullet = Bullet(player1.x, player1.y - 55, 6, 6, screen)

        while True:
            screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player1.right = True

                    if event.key == pygame.K_LEFT:
                        player1.left = True
                    if event.key == pygame.K_SPACE:
                        bullet.x = player1.x
                        bullet.create()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player1.right = False
                    if event.key == pygame.K_LEFT:
                        player1.left = False
                    if event.key == pygame.K_SPACE:
                        bullet.Isfire = False







            player1.move()
            player1.draw()
            bullet.draw()
            bullet.fire()


            pygame.display.update()


run = Main()
run()
