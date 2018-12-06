#turret.py
import pygame
import math

TURRET_IMAGE = "tank_top.png"

class Turret(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load(TURRET_IMAGE)
        self.imageMaster = self.imageMaster.convert_alpha()
        self.rect = self.imageMaster.get_rect()
        self.image = self.imageMaster
        self.x = 0
        self.y = 0
        self.angleDeg = 0
        self.player = player
        if (self.player.number == 1):
            self.imageMaster = pygame.transform.flip(self.imageMaster, True, False)
            self.image = self.imageMaster


    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    def setAngle(self):
        rads = self.player.shotAngle
        self.angleDeg = -rads*(180/math.pi)
        if(self.player.number == 2):
            self.angleDeg = self.angleDeg + 180
            #print("Degrees: {}".format(self.angleDeg))
        #else:
            #print("Degrees: {}".format(self.angleDeg))

    def pause(self):
        self.state = "PAUSED"

    def unpause(self):
        self.state = "RUNNING"

    def update(self):
        self.setAngle()
        if (self.player.number == 1):
            self.image = pygame.transform.rotozoom(self.imageMaster, self.angleDeg, 1)
            self.rect = self.image.get_rect(center=(self.player.x, self.player.y-13))
        elif(self.player.number == 2):
            self.image = pygame.transform.rotozoom(self.imageMaster, self.angleDeg, 1)
            self.rect = self.image.get_rect(center=(self.player.x, self.player.y-13))
