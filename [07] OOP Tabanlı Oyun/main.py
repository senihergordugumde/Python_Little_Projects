import sys
from player import *
from bullet import *
from blocks import *
import pygame
class Main:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen = pygame.display.set_mode((self.screen_width, 800))
        self.player1 = Player(150, 650, 30, 50, self.screen, 1, "playerrect")
        self.bullet = Bullet(self.screen, self.player1.x, self.player1.y - 55, 18, 18)
        self.block = Blocks(self.screen, 5, 5, 15, 12)

        for i in range(int(self.screen_width / self.block.width)):
           self.block.create()

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player1.right = True

                    if event.key == pygame.K_LEFT:
                        self.player1.left = True
                    if event.key == pygame.K_SPACE:

                        self.bullet.x = self.player1.x
                        self.bullet.create()
                        self.block.move()  # Blokların aşağı hareketinden sorumlu method

                        for i in range(int(self.screen_width / self.block.width)):
                            self.block.create()
                        self.block.add = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player1.right = False
                    if event.key == pygame.K_LEFT:
                        self.player1.left = False

            self.player1.move()
            self.player1.draw()
            self.bullet.draw()
            self.bullet.fire()
            self.block.draw()

            for blo in self.block.blocks:     # Bu iç içe döngü Mermilerin ve Blokların Çarpışmalarını Kontrol Ediyor
                for bul in self.bullet.bullets:
                    if bul.colliderect(blo):
                        self.bullet.bullets.remove(bul)
                        self.block.blocks.remove(blo)
                if blo.colliderect(self.player1.rectangle):
                    print("cOLLİDE")

            pygame.display.update()


App = Main()
App.run()
