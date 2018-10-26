import pygame
from app.assets import CAPTION, NO_GRAPHICS_ERROR
from app.game import SCREEN_SIZE

##
# Handles all paints and updates to graphics
##


class GFX:
    def __init__(self):
        self.dirty_rects = []
        try:
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption(CAPTION)
        except pygame.error:
            raise(pygame.error, NO_GRAPHICS_ERROR)

    ##
    # Partial updates improves performance
    # Most draw fns return a rect which you can pass to dirty, look at # paint backdrop for an example.
    ##
    def update(self):
        pygame.display.update(self.dirty_rects)
        del self.dirty_rects[:]

    def dirty(self, rect):
        self.dirty_rects.append(rect)
