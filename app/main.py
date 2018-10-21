import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
