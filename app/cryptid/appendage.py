from app.assets import HEAD1, LEG1, LEG2
import random

class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, asset_type=HEAD1):
        self.asset_type = asset_type
        self.orientation = orientation


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, orientation, shoulder, asset_type=None):
        self.orientation = orientation
        self.shoulder = shoulder
        if asset_type:
            self.asset_type = asset_type
        else:
            self.asset_type = random.choice([LEG1, LEG2])
