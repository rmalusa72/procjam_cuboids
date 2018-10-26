##
# Shared state, use sparingly
##

##
# Size of the whole screen
# All resizable dimensions should reference this.
##
SCREEN_SIZE = (1000, 700)

##
# current manager class instances
##
event_manager = None
gfx = None

##
# clock info
##
clock = None
ticks = 1

##
# Background thread, set stopthread = 1 to terminate
##
thread = None
stopthread = 0


version = "0.1.0"
DEBUG = 0
