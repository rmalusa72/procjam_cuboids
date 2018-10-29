from app.assets import *


class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # nose = vector from tail to head

    def __init__(self, nose=NORTH, asset_type=HEAD1):
        self.asset_type = asset_type
        self.nose = nose

    def align(self, orientation):
        pass # [self.nose] = realign(orientation, self.nose)

    def asset(self, creature_orientation):
        nose_orientation = self.nose
        if array_equal(creature_orientation, EAST):
            nose_orientation = ROT270 @ nose_orientation
        elif array_equal(creature_orientation, SOUTH):
            nose_orientation = ROT180 @ nose_orientation
        elif array_equal(creature_orientation, WEST):
            nose_orientation = ROT90 @ nose_orientation

        return get_asset(self.asset_type, nose_orientation)
