import numpy as np

# anatomy
DEFAULT_TORSO = "app/cryptid/assets/body1.png"
DEFAULT_TORSO_X_OFFSET = 71
DEFAULT_TORSO_Y_OFFSET = 31
DEFAULT_TORSO_WIDTH = 179
DEFAULT_TORSO_HEIGHT = 188

# Matrices
ROT0 = np.array([[1,0],[0,1]])
ROT90 = np.array([[0,-1],[1,0]])
ROT180 = np.array([[-1,0],[0,-1]])
ROT270 = np.array([[0,1],[-1,0]])
NORTH = np.array([[0],[1]])
EAST = np.array([[1],[0]])
SOUTH = np.array([[0],[-1]])
WEST = np.array([[-1],[0]])