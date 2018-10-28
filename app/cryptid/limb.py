from app.assets import *


class Limb:

    # asset_type = collection of assets that represent different permutations of the same asset
    # orientation = vector from tail to head

    def __init__(self, toes, shoulder, asset_type=LEG1):
        self.asset_type = asset_type
        self.toes = toes
        self.shoulder = shoulder

    def align(self, orientation):
        self.toes, self.shoulder = realign(orientation, self.toes, self.shoulder)

    def asset(self):
        return get_asset(self.asset_type, self.toes, self.shoulder)
