################################################################################
#                             Tank Volleyball                                  #
#                       Corey Stockton, Thomas Agnew                           #
#                               CSCI 43700                                     #
#                                11/27/18                                      #
################################################################################
import pygame
from ball import Ball
from player import Player

pygame.init()

def main():
	screen = pygame.display.set_mode((1600,900),pygame.RESIZABLE)
	pygame.display.set_caption("Tank Volleyball")

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((255, 255, 255))
	screen.blit(background, (0, 0))

	#create planet and players
	ball = Ball(screen)

	player1 = Player(screen, ball, 1)
	player2 = Player(screen, ball,  2)

	#group sprites
	ballSprite = pygame.sprite.Group(ball)
	playerSprites = pygame.sprite.Group(player1,player2)

	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)

		screen.blit(background, (0, 0))

		#clear sprites
		ballSprite.clear(screen, background)
		playerSprites.clear(screen, background)

		#update sprites
		ballSprite.update()
		playerSprites.update()

		#draw sprites
		ballSprite.draw(screen)
		playerSprites.draw(screen)

		pygame.display.flip()

if __name__ == "__main__":
	main()
