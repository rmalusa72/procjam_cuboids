from app.assets import *


class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, asset_type=HEAD1):
        self.asset_type = asset_type
        self.orientation = orientation

    def asset(self, creature_orientation):
        if array_equal(creature_orientation, EAST):
            self.orientation = ROT90 @ self.orientation
        elif array_equal(creature_orientation, SOUTH):
            self.orientation = ROT180 @ self.orientation
        elif array_equal(creature_orientation, WEST):
            self.orientation = ROT270 @ self.orientation

        return get_asset(self.asset_type, self.orientation)
