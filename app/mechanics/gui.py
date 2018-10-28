from pgu import text, gui as pgui
import app.game as game
import pygame
from .gfx import GFX


class GUI:
    def __init__(self):
        self.app = pgui.App()
        self.layout = pgui.Container(align=-1,valign=-1)
        self.checkbox_values = {}
        self.gui_rects = []
        self.checkbox_group = pgui.Group(value=[])

    def paint(self):
        self._randomize_all_button()
        self._mate_selected_button()
        self._rotate_all_button()
        self.app.init(self.layout, screen=game.gfx.screen)
        self.app.paint()

    def event(self, event):
        # maybe dirty this rect every time
        self.app.event(event)

    def _randomize_all_button(self):
        btn1 = pgui.Button("Randomize all")
        btn1.connect(pgui.CLICK, game.cryptid_manager.spawn_posse)
        self.layout.add(btn1, game.SCREEN[0]-150, 20)

    def _mate_selected_button(self):
        btn1 = pgui.Button("Mate Selected")
        btn1.connect(pgui.CLICK, game.cryptid_manager.mate_selected)
        self.layout.add(btn1, game.SCREEN[0]-150, 60)

    def _rotate_all_button(self):
        btn1 = pgui.Button("Rotate all")
        btn1.connect(pgui.CLICK, game.cryptid_manager.rotate_all)
        self.layout.add(btn1, game.SCREEN[0]-150, 100)

    def _select_slot(self, slot):
        check = pgui.Checkbox(self.checkbox_group, value=slot)
        check.connect(pgui.CLICK, game.cryptid_manager.select_slot, slot)
        self.layout.add(check,  slot[0]+135, slot[1]-30)

    def _randomize_slot(self, slot):
        btn1 = pgui.Button("Randomize Me")
        btn1.connect(pgui.CLICK, game.cryptid_manager.randomize_slot, slot)
        self.layout.add(btn1, slot[0]+170, slot[1]-30)

    def _add_random_cryptid(self, text):
        game.cryptid_manager.add_random_cryptid()
        print(text)
