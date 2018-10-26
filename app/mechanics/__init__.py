import pygame
import app.game as game
from .event_manager import EventManager
from .cryptid_manager import CryptidManager
from .gfx import GFX
from app.water_world.background import Background

__all__ = ["gfx", "event_manager", "cryptid_manager"]


def initialize():
    pygame.init()
    game.event_manager = EventManager()
    game.gfx = GFX()
    game.cryptid_manager = CryptidManager()
    Background.paint() # Background paint happens after gfx is initialized
    game.cryptid_manager.add_random_cryptid()
    game.event_manager.listen() # Listen must be called last
