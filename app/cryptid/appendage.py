class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, asset_type="app/cryptid/assets/head1_"):
        self.asset_type = asset_type
        self.orientation = orientation


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, shoulder, asset_type="app/cryptid/assets/leg1_"):
        self.asset_type = asset_type
        self.orientation = orientation
        self.shoulder = shoulder
