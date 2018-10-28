from app.assets import *


class Head:

    # asset_type = collection of assets that represent different permutations of the same asset
    # nose = vector from tail to head

    def __init__(self, nose, asset_type=HEAD1):
        self.asset_type = asset_type
        self.nose = nose

    def align(self, orientation):
        [self.nose] = realign(orientation, self.nose)

    def asset(self):
        return get_asset(self.asset_type, self.nose)
