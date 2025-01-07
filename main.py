import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	asteroidfield = AsteroidField()

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
		for obj in updatable:
			obj.update(dt)
		for aster in asteroids:
			if aster.is_colliding(player):
				print("Game Over!")
				sys.exit()
		for aster in asteroids:
			for shot in shots:
				if aster.is_colliding(shot):
					aster.split()
					shot.kill()

		Screen.fill("black")
		for obj in drawable:
			obj.draw(Screen)
		pygame.display.flip()

		#fps limit to 60
		dt = fps.tick(60) / 1000


if __name__ == "__main__":
	main()
