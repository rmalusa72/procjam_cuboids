import pygame
import app.game as game
from .event_manager import EventManager
from .gfx import GFX
from app.water_world.background import Background

__all__ = ["gfx", "event_manager"]


def initialize():
    pygame.init()
    game.event_manager = EventManager()
    game.gfx = GFX()
    Background.paint()
    game.event_manager.listen()
