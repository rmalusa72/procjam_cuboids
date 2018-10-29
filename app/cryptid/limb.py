from app.assets import *


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, shoulder=None, toes=None, asset_type=LEG1):
        self.asset_type = asset_type
        self.toes = toes
        self.toes = toes
        self.shoulder = shoulder
        if self.toes is None:
            self.toes = ROT90 @ self.shoulder

    # This is to update the orientation of the limb (not in use)
    def align(self, orientation):
        self.toes, self.shoulder = realign(orientation, self.toes, self.shoulder)

    # This gets relative orientation to creature north
    def asset(self, creature_orientation):
        toes, shoulder = realign(creature_orientation, self.toes, self.shoulder)
        return get_asset(self.asset_type, toes, shoulder)
