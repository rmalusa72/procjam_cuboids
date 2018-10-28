# noqa

from app.cryptid.cryptid import Cryptid
from app.cryptid.torso import Torso
from app.cryptid.appendage import Head, Limb
import pygame
import numpy as np

pop = []

for i in range(0, 10):
    print("Cryptid index: " + str(i))
    cur = Cryptid(1)
    cur.randomize(5)
    cur.getCoords()
    pygame.image.save(cur.makeSprite(), "sprite" + str(i) + ".png")
    pop.append(cur)

baby = pop[0].reproduce(pop[1])
if baby:
    pygame.image.save(baby.makeSprite(), "BABY.png")


# # Create a cryptid with default body plan of "one beautiful cube"
# sasquatch = Cryptid("blue")

# # Add another cube at the front
# sasquatch.thorax.head = Torso()
# sasquatch.thorax.head.tail = sasquatch.thorax.head # Doubly linked

# # Add another cube to the side
# sasquatch.thorax.left = Torso()
# sasquatch.thorax.left.right = sasquatch.thorax.left # Doubly linked

# # Add a head
# sasquatch.thorax.left.head = Head("app/cryptid/assets/head1", np.array([[0],[-1]]))

# # Add a limb
# sasquatch.thorax.left.tail = Limb("app/cryptid/assets/leg1_", np.array([[-1],[0]]), np.array([[0],[-1]]))

# # Add a limb
# sasquatch.thorax.right = Limb("app/cryptid/assets/leg1_", np.array([[0],[1]]), np.array([[1],[0]]))

# # Update coordinates
# sasquatch.getCoords()

# # Save sprite
# pygame.image.save(sasquatch.makeSprite(), "sprite1.png")

# # Rotate cryptid to face the other way (180 degrees)
# # Coords are automatically updated
# sasquatch.rotate(np.array([[0],[-1]]))

# # Save new sprite
# pygame.image.save(sasquatch.makeSprite(), "sprite2.png")
