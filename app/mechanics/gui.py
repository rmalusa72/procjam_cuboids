from pgu import text, gui as pgui
import app.game as game
import pygame
from .gfx import GFX


class GUI:
    def __init__(self, screen):
        self.app = pgui.App()
        self.layout = pgui.Container(align=-1,valign=-1)
        self._add_random_cryptid_button()
        self.app.init(self.layout, screen=screen)
        self.app.paint()

    def event(self, event):
        # maybe dirty this rect every time
        self.app.event(event)

    def _add_random_cryptid_button(self):
        btn1 = pgui.Button("Add random cryptid")
        btn1.connect(pgui.CLICK, game.cryptid_manager.add_random_cryptid)
        self.layout.add(btn1, game.SCREEN[0]-195, 20)

    def _add_random_cryptid(self, text):
        game.cryptid_manager.add_random_cryptid()
        print(text)
