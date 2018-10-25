from app.cryptid.cryptid import Cryptid
from app.cryptid.torso import Torso
import pygame
import numpy as np

# Create a cryptid with default body plan of "one beautiful cube"
sasquatch = Cryptid("blue")

# Add another cube at the front
sasquatch.thorax.head = Torso()
sasquatch.thorax.head.tail = sasquatch.thorax.head # Doubly linked

# Add another cube to the side
sasquatch.thorax.left = Torso()
sasquatch.thorax.left.right = sasquatch.thorax.left # Doubly linked

# Update coordinates
sasquatch.getCoords()

# Save sprite
pygame.image.save(sasquatch.makeSprite(), "sprite1.png")

# Rotate cryptid to face the other way (180 degrees)
# Coords are automatically updated
sasquatch.rotate(np.array([[0],[-1]]))

# Save new sprite
pygame.image.save(sasquatch.makeSprite(), "sprite2.png")