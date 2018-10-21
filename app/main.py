import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False

# Draw the ground
pygame.draw.rect(screen, pygame.Color("#77AB59"), pygame.Rect(0, 290, 300, 10))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
