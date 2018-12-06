#ball.py
import pygame
import random
import math

BALL_IMAGE = "ball.png"
BALL_WIDTH = 75
BALL_HEIGHT = 75

class Ball(pygame.sprite.Sprite):
	def __init__(self, screen, player1, player2, state):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(BALL_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = BALL_WIDTH
		self.height = BALL_HEIGHT
		self.size = 75
		self.image = pygame.transform.scale(self.image, (self.size,self.size))
		self.rect = self.image.get_rect()
		self.radius = self.size / 2
		
		self.state = state
		self.screen = screen
		self.player1 = player1
		self.player2 = player2
		
		self.x = self.screen.get_width() / 2
		self.y = self.screen.get_height() / 3
		self.dx = 0
		self.dy = 0
		self.ddx = 0
		self.ddy = 0
		self.theta = 0
		self.dtheta = 0
		
		self.isFalling = True
		
		self.rect.center = (self.x, self.y)
		
	def setAngularVelocity(self):
		self.theta = (self.dx / self.radius)
		
	def updateSpeeds(self):
		self.x += self.dx
		self.dx += self.ddx
		self.y += self.dy
		self.dy += self.ddy
		
		self.setAngularVelocity()
		self.theta += self.dtheta
		
	def getUnitVector(self, mousePos):
		dx = self.rect.centerx - mousePos[0]
		dy = self.rect.midtop[1] - mousePos[1]
		mag = math.sqrt(((dx**2) + (dy**2)))
		
		try:
			unitVec = (dx/mag, dy/mag)
		except:
			unitVec = (0, -1)
			
		return unitVec
	
	def checkClick(self):
		clicks = pygame.mouse.get_pressed()
		position = pygame.mouse.get_pos()
		
		if (clicks[0] and ((self.rect[0] <= position[0] <= self.rect[0]+self.rect[2]) and (self.rect[1] <= position[1] <= self.rect[1]+self.rect[3]))):
			unitVec = self.getUnitVector(position)
			new_dx = unitVec[0] * 4
			new_dy = unitVec[1] * -3
			
			if self.dy > 0:
				self.dx += new_dx
				self.dy = -new_dy
				self.isFalling = True
			elif self.dy <= 0:
				self.dx += new_dx
				self.dy -= new_dy
				self.isFalling = True
	
	def checkGravity(self):
		if (self.isFalling == True):
			self.ddy = .15
		else:
			self.ddy = 0

	def checkBounds(self):
		#ceiling
		if self.y - (self.height / 2) < 0:
			self.y = 0 + (self.height / 2)
			self.dy = -self.dy
		#ground
		if self.y + (self.height / 2) > self.screen.get_height():
			self.y = self.screen.get_height() - (self.height / 2)
			self.dx = 0
			self.dy = 0
			self.isFalling = False
			
			#add score
			if self.x > (self.screen.get_width() / 2):
				self.player1.score += 1
			else:
				self.player2.score += 1
				
			#reset for next round
			self.__init__(self.screen, self.player1, self.player2, "RUNNING")
		
		#left border
		if self.x - (self.width / 2) < 0:
			self.x = 0 + (self.width / 2)
			self.dx = -self.dx * .4
		#right border
		if self.x + (self.width / 2) > self.screen.get_width():
			self.x = self.screen.get_width() - (self.width / 2)
			self.dx = -self.dx * .4
		
	def pause(self):
		self.state = "PAUSED"

	def unpause(self):
		self.state = "RUNNING"
	
	def update(self):
		self.checkBounds()
		
		if self.state == "RUNNING":
			self.updateSpeeds()
		
		self.checkClick()
		self.checkGravity()
	
		self.rect.center = (self.x, self.y)