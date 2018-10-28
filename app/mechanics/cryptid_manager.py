from app.assets import *
import app.game as game
from app.cryptid.cryptid import Cryptid


class CryptidManager:
    def __init__(self):
        self.cryptids = []

    def add_random_cryptid(self):
        cryptid = Cryptid(1)
        cryptid.randomize(5)
        random_x = randint(-100, game.SCREEN[0]-200)
        random_y = randint(-100, game.SCREEN[1]-200)
        random_coordinates = (random_x,random_y)
        self._paint_cryptid_at(cryptid, random_coordinates)
        self.cryptids.append(cryptid)

    def _paint_cryptid_at(self, cryptid, coords):
        sprite = cryptid.makeSprite()
        rect = game.gfx.screen.blit(sprite, coords)
        game.gfx.dirty(rect)
