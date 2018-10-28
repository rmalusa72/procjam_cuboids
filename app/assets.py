from random import randint, choice
from numpy import array, array_equal
from os.path import abspath, dirname
##
# assuming the existance of abs file paths will cause a bug if we use zipping etc
##
__app_path__ = abspath(dirname(__file__))

##
# Sprites
##
HEAD1 = "head1"
BODY1 = "body1"
LEG1 = "leg1"

##
# Cryptid bodyplan presets #
##

DOG = 1
WEIRD_DOG = 2
LEFTWARD_DOG = 3
FROG = 4

##
# Shared color library
##
class crayons:
    CALM_BROWN = (100, 50, 50)
    NIGHT_BLUE = (5, 18, 37)


##
# Error messages:
##
NO_GRAPHICS_ERROR = 'Cannot Initialize Graphics'
INTERUPT_ERROR = 'Keyboard Interrupt...\nExiting!'

##
# Strings:
##
CAPTION = 'Proc Party'


##
# Anatomy consts:
##
MAX_TORSOS = 5
DEFAULT_TORSO = BODY1
DEFAULT_TORSO_X_OFFSET = 71
DEFAULT_TORSO_Y_OFFSET = 31
DEFAULT_TORSO_WIDTH = 179
DEFAULT_TORSO_HEIGHT = 188
DEFAULT_THORAX_COORD = array([[0], [0]])

##
# Matrix rotations
##
ROT0 = array([[1,0],[0,1]])
ROT90 = array([[0,-1],[1,0]])
ROT180 = array([[-1,0],[0,-1]])
ROT270 = array([[0,1],[-1,0]])

##
# Orientations
##
NORTH = array([[0],[1]])
EAST = array([[1],[0]])
SOUTH = array([[0],[-1]])
WEST = array([[-1],[0]])


##
# Helpful Functions
##
def nparray_in_list(nparray, list):
    return any((nparray == l).all() for l in list)

def _orientation_string(o):
    if array_equal(o, NORTH): return "N"
    elif array_equal(o, EAST): return "E"
    elif array_equal(o, SOUTH): return "S"
    elif array_equal(o, WEST): return "W"


def get_asset(type, *orientations):
    varient = "".join(map(_orientation_string, orientations))
    if varient != "":
        varient = "_" + varient
    return F"{__app_path__}/cryptid/assets/{type}{varient}.png"
