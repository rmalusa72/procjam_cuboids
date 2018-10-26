import pygame
import app.game as game

##
# EventManager manages the external input queue (keystrokes, mouse)
# Note that current position of any device is availible separately
# EventManager ticks the clock
##


class EventManager:
    def __init__(self):
        game.clock = pygame.time.Clock()

    def listen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            game.gfx.update()
            game.ticks = game.clock.tick(30)
