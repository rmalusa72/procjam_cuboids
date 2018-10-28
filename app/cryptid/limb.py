from app.assets import *


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, shoulder, asset_type="app/cryptid/assets/leg1_"):
        self.asset_type = asset_type
        self.orientation = orientation
        self.shoulder = shoulder

    def get_asset(self, creature_orientation):
        limb_orientation = self.orientation
        limb_shoulder = self.shoulder

        # Update relative orientation vectors to absolute orientation vectors
        if array_equal(creature_orientation, EAST):
            limb_orientation = ROT90 @ limb_orientation
            limb_shoulder = ROT90 @ limb_shoulder
        elif array_equal(creature_orientation, SOUTH):
            limb_orientation = ROT180 @ limb_orientation
            limb_shoulder = ROT180 @ limb_shoulder
        elif array_equal(creature_orientation, WEST):
            limb_orientation = ROT270 @ limb_orientation
            limb_shoulder = ROT270 @ limb_shoulder

        # Retrieve correct asset
        limb_assettype = self.asset_type

        # Is there an easier way to get a sprite by limb and shoulder orientation .. a grid?
        if array_equal(limb_orientation, NORTH):
            limb_assettype = limb_assettype + "N"
        elif array_equal(limb_orientation, EAST):
            limb_assettype = limb_assettype + "E"
        elif array_equal(limb_orientation, SOUTH):
            limb_assettype = limb_assettype + "S"
        elif array_equal(limb_orientation, WEST):
            limb_assettype = limb_assettype + "W"

        if array_equal(limb_shoulder, NORTH):
            limb_assettype = limb_assettype + "N"
        elif array_equal(limb_shoulder, EAST):
            limb_assettype = limb_assettype + "E"
        elif array_equal(limb_shoulder, SOUTH):
            limb_assettype = limb_assettype + "S"
        elif array_equal(limb_shoulder, WEST):
            limb_assettype = limb_assettype + "W"

        return limb_assettype + ".png"
