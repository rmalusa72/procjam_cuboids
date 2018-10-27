import pygame
from app.assets import crayons
import app.game as game

##
# Rendering class for background stuff
##


class Background:
    @classmethod
    def paint(cls):
        Background._fill_screen()
        Background._draw_ground()

    @classmethod
    def _fill_screen(cls):
        rect = game.gfx.screen.fill(crayons.NIGHT_BLUE)
        game.gfx.dirty(rect)

    @classmethod
    def _draw_ground(cls):
        rect = pygame.Rect(0, game.SCREEN[1]-100, game.SCREEN[0], 100)
        pygame.draw.rect(game.gfx.screen, crayons.CALM_BROWN, rect)
        game.gfx.dirty(rect)
