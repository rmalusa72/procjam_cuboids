from app.cryptid.assets import DEFAULT_TORSO


#       {head}
#        ---
# left -|   |- right
#        ---
#        tail


class Torso:

    # asset_type = collection of assets that represent different permutations of the same asset
    # Ports will point to limb or additional torso segments, or null

    def __init__(self, asset_type=DEFAULT_TORSO, head=None, right=None, tail=None, left=None):
        self.asset_type = asset_type
        self.head = head
        self.right = right
        self.tail = tail
        self.left = left
