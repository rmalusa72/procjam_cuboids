from app.assets import *


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, shoulder, asset_type=LEG1):
        self.asset_type = asset_type
        self.orientation = orientation
        self.shoulder = shoulder

    def asset(self, creature_orientation):
        if array_equal(creature_orientation, EAST):
            self.orientation = ROT90 @ self.orientation
            self.shoulder = ROT90 @ self.shoulder
        elif array_equal(creature_orientation, SOUTH):
            self.orientation = ROT180 @ self.orientation
            self.shoulder = ROT180 @ self.shoulder
        elif array_equal(creature_orientation, WEST):
            self.orientation = ROT270 @ self.orientation
            self.shoulder = ROT270 @ self.shoulder

        return get_asset(self.asset_type, self.orientation, self.shoulder)
