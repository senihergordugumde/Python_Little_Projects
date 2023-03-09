import sys
from player import *
from bullet import *
from blocks import *
import pygame
from pygame.locals import *
class Main():

    def __init__(self):

        pygame.init()
        screen_width = 800
        screen = pygame.display.set_mode((screen_width, 800))
        player1 = Player(150, 650, 150, 50, screen,1)
        bullet = Bullet(player1.x, player1.y - 55, 6, 6, screen)
        block = Blocks(screen,5,5,15,12)
        for i in range(int(screen_width / block.width)):
            block.create()
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

                        block.move()
                        for i in range(int(screen_width / block.width)):
                            block.create()
                        block.add = 0


                    if event.key == pygame.K_x:

                            for i in range(int(screen_width / block.width)):
                                 block.create()
                            block.add = 0





                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player1.right = False
                    if event.key == pygame.K_LEFT:
                        player1.left = False


            player1.move()
            player1.draw()
            bullet.draw()
            bullet.fire()
            block.draw()

            pygame.display.update()


run = Main()
run()
