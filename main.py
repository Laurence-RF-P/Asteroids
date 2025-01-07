import pygame
from constants import *
from circleshape import *
from player import *

def main():
	pygame.init()
	Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	fps = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		player.update(dt)
		Screen.fill("black")
		player.draw(Screen)
		pygame.display.flip()

		#fps limit to 60
		dt = fps.tick(60) / 1000


if __name__ == "__main__":
	main()
