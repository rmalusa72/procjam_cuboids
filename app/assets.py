import random
from numpy import array, array_equal
from os.path import abspath, dirname
##
# assuming the existance of abs file paths will cause a bug if we use zipping etc
##
__app_path__ = abspath(dirname(__file__))

##
# Sprites
##
HEAD1_F = F"{__app_path__}/cryptid/assets/head1_f.png"
BODY1 = F"{__app_path__}/cryptid/assets/body1.png"
LEG1_B_DOWN = F"{__app_path__}/cryptid/assets/leg1_b_down.png"
LEG1_F_DOWN = F"{__app_path__}/cryptid/assets/leg1_f_down.png"


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
