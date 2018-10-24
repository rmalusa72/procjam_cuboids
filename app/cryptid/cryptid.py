import numpy as np
from app.cryptid.torso import Torso
from app.cryptid.appendage import Appendage

rot90 = np.array([[0,-1],[1,0]])

class Cryptid:

    def __init__(self, color, orientation=np.array([[0],[1]]), thorax=Torso()):
        self.color = color
        self.thorax = thorax
        self.orientation = orientation
        self.getCoords()

    # Updates body_list, coords, and num_bodyparts for current state
    # Body_list = arbitrarily ordered list of body parts generated as-needed
    # Coords = list of (x,y) coords in same order as above
    def getCoords(self):
        self.body_list = []
        self.coords = []
        self.getCoords_rec(self.thorax, np.array([[0],[0]]))
        self.num_bodyparts = len(self.body_list)

    def getCoords_rec(self, bodypart, current_coords):
        if bodypart and not (bodypart in self.body_list): 
            self.body_list.append(bodypart)
            self.coords.append(current_coords)

            if isinstance(bodypart, Torso):
                self.getCoords_rec(bodypart.head, current_coords + self.orientation)
                self.getCoords_rec(bodypart.right, current_coords - rot90 @ self.orientation)
                self.getCoords_rec(bodypart.tail, current_coords - self.orientation)
                self.getCoords_rec(bodypart.left, current_coords + rot90 @ self.orientation)

    def rotate(self, newOrientation):
        self.orientation = newOrientation
        self.getCoords()

    def makeSprite(self):
        # Generate sprite from bodyparts and coords
        # To render legs & heads we are going to need to check their position relative to their parent
        # (Or else store which way they are facing and update it when the creature rotates)
        return None
