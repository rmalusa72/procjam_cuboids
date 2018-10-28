import pygame
import app.game as game
from .event_manager import EventManager
from .cryptid_manager import CryptidManager
from .gfx import GFX
from app.water_world.background import Background
from .gui import GUI

__all__ = ["gfx", "event_manager", "cryptid_manager"]


def initialize():
    pygame.init()
    game.event_manager = EventManager()
    game.gfx = GFX()
    game.gui = GUI()
    game.cryptid_manager = CryptidManager()
    game.cryptid_manager.spawn_posse()
    game.event_manager.listen() # Listen must be called last
