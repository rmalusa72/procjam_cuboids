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
