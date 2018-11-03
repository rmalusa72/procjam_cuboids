from app.assets import *
import app.game as game
from app.water_world.background import Background
from app.cryptid.cryptid import Cryptid
import pygame

class CryptidManager:
    def __init__(self):
        self.cryptid_slots = {
            (0,50): None,
            (0,370): None,
            (500,50): None,
            (500,370): None
        }
        # This adds the buttons to randomize an individual slot
        self.selected_parents = []
        self.heart = pygame.image.load(HEART)

    def mate_selected(self):
        if len(self.selected_parents) == 2:
            parent1 = self.cryptid_slots[self.selected_parents[0]]
            parent2 = self.cryptid_slots[self.selected_parents[1]]
            baby = parent1.mate(parent2)
            
            slot_list = list(self.cryptid_slots.keys())
            slot_list.remove(self.selected_parents[0])
            slot_list.remove(self.selected_parents[1])
            baby_slot = choice(slot_list)
            self.cryptid_slots[baby_slot] = baby
            self.paint_all_slots()

    def spawn_posse(self):
        self.fill_all_slots()
        self.add_randomize_buttons()
        self.add_select_buttons()
        self.paint_all_slots()

    def paint_all_slots(self):
        Background.paint()
        game.gui.paint()
        for slot, value in self.cryptid_slots.items():
            self._paint_cryptid_at(value, slot)
        self.paint_all_hearts()

    @staticmethod
    def _paint_cryptid_at(cryptid, coords):
        sprite = cryptid.makeSprite()
        rect = game.gfx.screen.blit(sprite, coords)
        game.gfx.dirty(rect)

    def paint_all_hearts(self):
        for parent_slot in self.selected_parents:
            rect = game.gfx.screen.blit(self.heart, (parent_slot[0] + 100, parent_slot[1]-10))
            game.gfx.dirty(rect)

    def randomize_slot(self, slot):
        new_cryptid = Cryptid(1).randomize(4)
        self.cryptid_slots[slot] = new_cryptid
        self.paint_all_slots()

    def fill_all_slots(self):
        for slot, _ in self.cryptid_slots.items():
            self.cryptid_slots[slot] = Cryptid(1).randomize(4)

    def select_slot(self, slot):
        if not slot in self.selected_parents:
            self.selected_parents.append(slot)
            if len(self.selected_parents) > 2:
                self.selected_parents = self.selected_parents[-2:]
            self.paint_all_slots()

    def add_select_buttons(self):
        for slot, _ in self.cryptid_slots.items():
            game.gui._select_slot(slot)

    def add_randomize_buttons(self):
        for slot, _ in self.cryptid_slots.items():
            game.gui._randomize_slot(slot)

    def rotate_all(self):
        for _, value in self.cryptid_slots.items():
            value.rotate(ROT90 @ value.orientation)
        self.paint_all_slots()

    @staticmethod
    def random_coord():
        return randint(-100, game.SCREEN[0]-200), randint(-100, game.SCREEN[1]-200)
