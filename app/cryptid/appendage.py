class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, asset_type, orientation):
        self.asset_type = asset_type
        self.orientation = orientation

class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, asset_type, orientation, shoulder):
        self.asset_type = asset_type
        self.orientation = orientation
        self.shoulder = shoulder
