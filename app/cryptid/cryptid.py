from app.cryptid.torso import Torso

class Cryptid:

    # Color = color across all body parts
    # Bodyparts = list of body parts.
    # Note that their connection structure is reflected in ports/parents, & the order of this list is arbitrary
    # Coords = 2xn array of coords for body parts, in same order as above

    def __init__(self, color, thorax=Torso(), orientation):
        self.color = color
        self.thorax = thorax
        self.orientation = orientation
        self.coords = None

    def derive_coords(self):
        return None

    def rotate(steps):
        # Use matrix multiplication on coordinates matrix to rotate the creature
        return None

    def makeSprite():
        # Generate sprite from bodyparts and coords
        # To render legs & heads we are going to need to check their position relative to their parent
        # (Or else store which way they are facing and update it when the creature rotates)
        return None
