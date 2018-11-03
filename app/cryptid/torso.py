from app.assets import *
from app.cryptid.head import Head
from app.cryptid.limb import Limb


#       {head}
#        ---
# left -|   |- right
#        ---
#        tail

appendage_options = [Head, Limb, None, None]
socket_vectors = [NORTH, EAST, SOUTH, WEST]

def _random_appendage(orientation):
    appendage = choice(appendage_options)
    if appendage: return appendage(orientation)

class Torso:

    # asset_type = collection of assets that represent different permutations of the same asset
    # Ports will point to limb or additional torso segments, or null

    def __init__(self, head=None, right=None, tail=None, left=None, asset_type=BODY1):
        self.asset_type = asset_type
        self.head = head
        self.right = right
        self.tail = tail
        self.left = left

    @classmethod
    def random(cls):
        return Torso(*[_random_appendage(vector) for vector in socket_vectors])

    @classmethod
    def random_port_name(cls):
        return choice(['head', 'right', 'tail', 'left'])

    def put_in_socket(self, index, thing_to_go_in_socket):
        if index == 0:
            self.head = thing_to_go_in_socket
        elif index == 1:
            self.right = thing_to_go_in_socket
        elif index == 2:
            self.tail = thing_to_go_in_socket
        elif index == 3:
            self.left = thing_to_go_in_socket

    def asset(self, _):
        return get_asset(self.asset_type)
