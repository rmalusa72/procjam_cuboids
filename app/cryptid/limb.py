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

    def align(self, orientation):
        pass # self.toes, self.shoulder = realign(orientation, self.toes, self.shoulder)

    def asset(self, creature_orientation):
        toe_orientation = self.toes
        limb_shoulder = self.shoulder

        # Update relative orientation vectors to absolute orientation vectors
        if array_equal(creature_orientation, EAST):
            toe_orientation = ROT270 @ toe_orientation
            limb_shoulder = ROT270 @ limb_shoulder
        elif array_equal(creature_orientation, SOUTH):
            toe_orientation = ROT180 @ toe_orientation
            limb_shoulder = ROT180 @ limb_shoulder
        elif array_equal(creature_orientation, WEST):
            toe_orientation = ROT90 @ toe_orientation
            limb_shoulder = ROT90 @ limb_shoulder

        return get_asset(self.asset_type, toe_orientation, limb_shoulder)
