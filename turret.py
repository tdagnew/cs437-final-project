#turret.py
import pygame

TURRET_IMAGE = "tank_top.png"

class Turret(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(TURRET_IMAGE)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    def setAngle(self, deg):
        self.angleDeg = deg
