from app.assets import *
import app.game as game
from app.water_world.background import Background
from app.cryptid.cryptid import Cryptid

class CryptidManager:
    def __init__(self):
        self.cryptid_slots = {
            (0,50): None,
            (0,370): None,
            (500,50): None,
            (500,370): None
        }
        # This adds the buttons to randomize an individual slot


    def spawn_posse(self):
        self.fill_all_slots()
        self.add_randomize_buttons()
        self.paint_all_slots()

    def paint_all_slots(self):
        Background.paint()
        game.gui.paint()
        for slot, cryptid in self.cryptid_slots.items():
            self._paint_cryptid_at(cryptid, slot)

    @staticmethod
    def _paint_cryptid_at(cryptid, coords):
        sprite = cryptid.makeSprite()
        rect = game.gfx.screen.blit(sprite, coords)
        game.gfx.dirty(rect)

    def randomize_slot(self, slot):
        new_cryptid = Cryptid(1).randomize(4)
        self.cryptid_slots[slot] = new_cryptid
        self.paint_all_slots()

    def fill_all_slots(self):
        for slot, _ in self.cryptid_slots.items():
            self.cryptid_slots[slot] = Cryptid(1).randomize(4)

    def add_randomize_buttons(self):
        for slot, _ in self.cryptid_slots.items():
            game.gui._randomize_slot(slot)

    @staticmethod
    def random_coord():
        return randint(-100, game.SCREEN[0]-200), randint(-100, game.SCREEN[1]-200)
