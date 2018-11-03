from app.cryptid.cryptid import Cryptid
from app.cryptid.torso import Torso
from app.assets import *
from app.cryptid.head import Head
from app.cryptid.limb import Limb


class Dog(Cryptid):
    def __init__(self, color=crayons.RED, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.head = Torso()
        self.thorax.head.tail = self.thorax
        self.thorax.head.head = Head(NORTH)
        self.thorax.head.left = Limb(WEST, NORTH, asset_type=LEG1)
        self.thorax.head.right = Limb(EAST, NORTH, asset_type=LEG1)
        self.thorax.left = Limb(WEST, NORTH, asset_type=LEG1)
        self.thorax.right = Limb(EAST, NORTH, asset_type=LEG1)
        self.updateCoords()


class WeirdDog(Cryptid):
    def __init__(self, color=crayons.BLUERAZZ, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.head = Torso()
        self.thorax.head.tail = self.thorax
        self.thorax.tail = Torso()
        self.thorax.tail.head = self.thorax
        self.thorax.head.right = Head(EAST)
        self.thorax.head.head = Head(NORTH)
        self.thorax.left = Limb(WEST, NORTH, asset_type=LEG1)
        self.thorax.tail.left = Limb(WEST, NORTH, asset_type=LEG1)
        self.thorax.right = Limb(EAST, NORTH, asset_type=LEG1)
        self.thorax.tail.right = Limb(EAST, NORTH, asset_type=LEG1)
        self.updateCoords()


class LeftwardDog(Cryptid):
    def __init__(self, color=crayons.RED, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.left = Torso()
        self.thorax.left.right = self.thorax
        self.thorax.left.left = Head(WEST)
        self.thorax.left.head = Limb(NORTH, WEST, asset_type=LEG1)
        self.thorax.left.tail = Limb(SOUTH, WEST, asset_type=LEG1)
        self.thorax.head = Limb(NORTH, WEST, asset_type=LEG1)
        self.thorax.tail = Limb(SOUTH, WEST, asset_type=LEG1)
        self.updateCoords()


class Frog(Cryptid):
    def __init__(self, color=crayons.KEYLIME, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.tail = Head(SOUTH)
        self.thorax.left = Limb(WEST, SOUTH, asset_type=LEG2)
        self.thorax.right = Limb(EAST, SOUTH, asset_type=LEG2)
        self.updateCoords()


class EyeSpider(Cryptid):
    def __init__(self, color=crayons.SILVERBLUE, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.right = Head(EAST, asset_type=HEAD2)
        self.thorax.head = Head(NORTH, asset_type=HEAD2)
        self.thorax.tail = Head(SOUTH, asset_type=HEAD2)
        self.thorax.left = Torso()
        self.thorax.left.right = self.thorax.left
        self.thorax.left.head = Limb(NORTH, EAST, asset_type=LEG3)
        self.thorax.left.tail = Limb(SOUTH, EAST, asset_type=LEG3)
        self.updateCoords()

class LongBoy(Cryptid):
    def __init__(self, color=crayons.RED, orientation=NORTH):
        super().__init__(color, orientation)
        self.thorax.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail = Torso()
        self.thorax.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail = Torso()
        self.thorax.tail.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail = Torso()
        self.thorax.tail.tail.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail = Torso()
        self.thorax.tail.tail.tail.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.tail = Torso()
        self.thorax.tail.tail.tail.tail.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.tail.tail = Torso()
        self.thorax.tail.tail.tail.tail.tail.tail.left = Limb(WEST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.tail.tail.right = Limb(EAST, SOUTH, asset_type=LEG1)
        self.thorax.tail.tail.tail.tail.tail.tail.tail = Head(SOUTH, asset_type=HEAD1)
        self.updateCoords()
