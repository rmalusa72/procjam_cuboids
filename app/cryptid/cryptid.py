from app.cryptid.assets import DEFAULT_TORSO


class Cryptid:

    # Color = color across all body parts
    # Bodyparts = list of body parts.
    # Note that their connection structure is reflected in ports/parents, & the order of this list is arbitrary
    # Coords = 2xn array of coords for body parts, in same order as above

    def __init__(self, color, bodyparts, coords):
        self.color = color
        self.bodyparts = bodyparts
        self.coords = coords

    def rotate(steps):
        # Use matrix multiplication on coordinates matrix to rotate the creature
        return None

    def makeSprite():
        # Generate sprite from bodyparts and coords
        # To render legs & heads we are going to need to check their position relative to their parent
        # (Or else store which way they are facing and update it when the creature rotates)
        return None


class Torso:

    # Variant = torso sprite type
    # Ports will point to limb or additional torso segments, or null

    def __init__(self, variant=DEFAULT_TORSO, port1=None, port2=None, port3=None, port4=None, port5=None, port6=None):
        self.variant = variant
        self.port1 = port1
        self.port2 = port2
        self.port3 = port3
        self.port4 = port4
        self.port5 = port5
        self.port6 = port6


class Limb:

    # Variant = limb sprite type
    # Parent points back to torso from which the limb sprouts

    def __init__(self, variant, parent):
        self.variant = variant
        self.parent = parent


class Head:

    # Variant = head sprite type
    # Parent points back to torso from which head sprouts

    def __init__(self, variant, parent):
        self.variant = variant
        self.parent = parent
