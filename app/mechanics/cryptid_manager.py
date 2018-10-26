import numpy as np
import app.game as game
from app.cryptid.cryptid import *
from app.cryptid.torso import Torso
from app.cryptid.appendage import Head, Limb

MAX_TORSOS = 5


class CryptidManager:
    def __init__(self):
        self.cryptids = []

    def add_random_cryptid(self):
        cryptid = Cryptid(1)
        cryptid.randomize(5)
        random_coordinates = (300,300)
        self._paint_cryptid_at(cryptid, random_coordinates)
        self.cryptids.append(cryptid)

    # def _generate_random_cryptid(self):
    #     sasquatch = Cryptid("blue")

    #     # Add another cube at the front
    #     sasquatch.thorax.head = Torso()
    #     sasquatch.thorax.head.tail = sasquatch.thorax.head # Doubly linked

    #     # Add another cube to the side
    #     sasquatch.thorax.left = Torso()
    #     sasquatch.thorax.left.right = sasquatch.thorax.left # Doubly linked

    #     # Add a head
    #     sasquatch.thorax.left.head = Head("app/cryptid/assets/head1", np.array([[0],[-1]]))

    #     # Add a limb
    #     sasquatch.thorax.left.tail = Limb("app/cryptid/assets/leg1_", np.array([[-1],[0]]), np.array([[0],[-1]]))

    #     # Add a limb
    #     sasquatch.thorax.right = Limb("app/cryptid/assets/leg1_", np.array([[0],[1]]), np.array([[1],[0]]))

    #     # Update coordinates
    #     sasquatch.getCoords()
    #     generic_cryptid = Cryptid(1)
    #     return generic_cryptid

    def _paint_cryptid_at(self, cryptid, coords):
        sprite = cryptid.makeSprite()
        rect = game.gfx.screen.blit(sprite, coords)
        game.gfx.dirty(rect)
