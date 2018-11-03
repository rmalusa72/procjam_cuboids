from app.assets import *
import app.game as game
from app.water_world.background import Background
from app.cryptid.cryptid import Cryptid

class CryptidManager:
    def __init__(self):
        self.cryptid_slots = {
            (0,50): [None, False],
            (0,370): [None, False],
            (500,50): [None, False],
            (500,370): [None, False]
        }
        # This adds the buttons to randomize an individual slot

    def mate_selected(self):
        pass

    def spawn_posse(self):
        self.fill_all_slots()
        self.add_randomize_buttons()
        self.add_checkboxes()
        self.paint_all_slots()

    def paint_all_slots(self):
        Background.paint()
        game.gui.paint()
        for slot, value in self.cryptid_slots.items():
            self._paint_cryptid_at(value[0], slot)

    @staticmethod
    def _paint_cryptid_at(cryptid, coords):
        sprite = cryptid.makeSprite()
        rect = game.gfx.screen.blit(sprite, coords)
        game.gfx.dirty(rect)

    def randomize_slot(self, slot):
        new_cryptid = Cryptid(1).randomize(4)
        self.cryptid_slots[slot][0] = new_cryptid
        self.paint_all_slots()

    def fill_all_slots(self):
        for slot, _ in self.cryptid_slots.items():
            self.cryptid_slots[slot][0] = Cryptid(1).randomize(4)

    def select_slot(self, slot):
        self.cryptid_slots[slot][1] = True
        # Not quite correct
        self.paint_all_slots()

    def add_checkboxes(self):
        for slot, _ in self.cryptid_slots.items():
            game.gui._select_slot(slot)

    def add_randomize_buttons(self):
        for slot, _ in self.cryptid_slots.items():
            game.gui._randomize_slot(slot)

    def rotate_all(self):
        for _, value in self.cryptid_slots.items():
            value[0].rotate(ROT90 @ value[0].orientation)
        self.paint_all_slots()

    @staticmethod
    def random_coord():
        return randint(-100, game.SCREEN[0]-200), randint(-100, game.SCREEN[1]-200)
