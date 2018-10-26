from app.assets import BODY1


#       {head}
#        ---
# left -|   |- right
#        ---
#        tail


class Torso:

    # asset_type = collection of assets that represent different permutations of the same asset
    # Ports will point to limb or additional torso segments, or null

    def __init__(self, asset_type = BODY1, head=None, right=None, tail=None, left=None):
        self.asset_type = asset_type
        self.head = head
        self.right = right
        self.tail = tail
        self.left = left

    def put_in_socket(self, index, thing_to_go_in_socket):
        if index == 0:
            self.head = thing_to_go_in_socket
        elif index == 1:
            self.right = thing_to_go_in_socket
        elif index == 2:
            self.tail = thing_to_go_in_socket
        elif index == 3: 
            self.left = thing_to_go_in_socket
