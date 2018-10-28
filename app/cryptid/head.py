from app.assets import *


class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, asset_type="app/cryptid/assets/head1_"):
        self.asset_type = asset_type
        self.orientation = orientation

    def get_asset(self, creature_orientation):
        head_orientation = self.orientation
        if array_equal(creature_orientation, EAST):
            head_orientation = ROT90 @ head_orientation
        elif array_equal(creature_orientation, SOUTH):
            head_orientation = ROT180 @ head_orientation
        elif array_equal(creature_orientation, WEST):
            head_orientation = ROT270 @ head_orientation

        head_assettype = self.asset_type

        if array_equal(head_orientation, NORTH):
            head_assettype = head_assettype + "N"
        elif array_equal(head_orientation, EAST):
            head_assettype = head_assettype + "E"
        elif array_equal(head_orientation, SOUTH):
            head_assettype = head_assettype + "S"
        elif array_equal(head_orientation, WEST):
            head_assettype = head_assettype + "W"

        return head_assettype + ".png"
