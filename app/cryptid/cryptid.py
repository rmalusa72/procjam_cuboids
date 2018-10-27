import numpy as np
import pygame
from app.cryptid.torso import Torso
from app.assets import *
from app.cryptid.appendage import Head, Limb
import random


DEFAULT_THORAX_COORD = np.array([[0], [0]])


def nparray_in_list(nparray, nparraylist):
    for element in nparraylist:
        if np.array_equal(element, nparray):
            return True
    return False


class Cryptid:
    def __init__(self, color, orientation=np.array([[0], [1]])):
        self.color = color
        self.thorax = Torso()
        self.orientation = orientation
        self.body_list = []
        self.coords = []
        self.num_bodyparts = 1
        self.updateCoords()
        self.sprite = None

    def randomize(self, max_torsos):
        self.thorax = Torso()
        self.max_torsos = max_torsos
        coords_filled = [DEFAULT_THORAX_COORD]
        self._randomize(self.thorax, DEFAULT_THORAX_COORD, coords_filled)
        self.updateCoords()

    def _randomize(self, current_torso, current_coords, coords_filled):
        if not self.max_torsos == 0:
            socket_vectors = [NORTH, EAST, SOUTH, WEST]

            for i in range(0, len(socket_vectors)):
                next_coords = current_coords + socket_vectors[i]
                if not nparray_in_list(next_coords, coords_filled):
                    # Then corresponding socket is empty
                    child_class = random.choice([Head, Limb, Torso, None])
                    if child_class:

                        coords_filled.append(next_coords)

                        if child_class == Torso:
                            self.max_torsos = self.max_torsos - 1
                            child = Torso()
                            child.put_in_socket((i+2) % 4, current_torso)
                            current_torso.put_in_socket(i, child)
                            self._randomize(child, next_coords, coords_filled)

                        elif child_class == Head:
                            child = Head(socket_vectors[i])
                            current_torso.put_in_socket(i, child)

                        elif child_class == Limb:
                            child = Limb(ROT90 @ socket_vectors[i], socket_vectors[i])
                            current_torso.put_in_socket(i, child)

    def getCoords(self):
        self.updateCoords()
        return self.coords

    # Updates body_list, coords, and num_bodyparts for current state
    # Body_list = arbitrarily ordered list of body parts generated as-needed
    # Coords = list of (x,y) coords in same order as above
    def updateCoords(self):
        self.body_list = []
        self.coords = []
        self._updateCoords(self.thorax, DEFAULT_THORAX_COORD)
        self.num_bodyparts = len(self.body_list)

    def _updateCoords(self, bodypart, current_coords):
        if bodypart and not (bodypart in self.body_list):
            self.body_list.append(bodypart)

            for coord in self.coords:
                if (coord == current_coords).all():
                    raise Exception("Creature collision with self")

            self.coords.append(current_coords)

            if isinstance(bodypart, Torso):
                self._updateCoords(bodypart.head, current_coords + self.orientation)
                self._updateCoords(bodypart.right, current_coords - ROT90 @ self.orientation)
                self._updateCoords(bodypart.tail, current_coords - self.orientation)
                self._updateCoords(bodypart.left, current_coords + ROT90 @ self.orientation)

    def rotate(self, newOrientation):
        self.orientation = newOrientation
        self.updateCoords()

    def makeSprite(self):
        self.updateCoords()
        # Work out each body part's relative distance from the camera
        layers = []
        min_layer = 0
        max_layer = 0
        leftmost = 0
        rightmost = 0
        for i in range(0, self.num_bodyparts):
            layer = self.coords[i][0][0] - self.coords[i][1][0]
            lateral = self.coords[i][0][0] + self.coords[i][1][0]
            layers.append(layer)
            if layer < min_layer:
                min_layer = layer
            if layer > max_layer:
                max_layer = layer
            if lateral < leftmost:
                leftmost = lateral
            if lateral > rightmost:
                rightmost = lateral

        num = (DEFAULT_TORSO_WIDTH + (rightmost - leftmost)*DEFAULT_TORSO_X_OFFSET,
               DEFAULT_TORSO_HEIGHT + (max_layer - min_layer)*DEFAULT_TORSO_Y_OFFSET)
        sprite = pygame.Surface(num)
        sprite.set_colorkey((255, 0, 255))
        sprite.fill((255, 0, 255))

        for cur_layer in range(min_layer, max_layer + 1):
            # print(cur_layer)
            # pygame.image.save(sprite, "testsprite" + str(cur_layer) + ".png")
            y_pos = 0 + (cur_layer - min_layer) * DEFAULT_TORSO_Y_OFFSET
            for i in range(0, self.num_bodyparts):
                if layers[i] == cur_layer:
                    x_pos = 0 + (self.coords[i][0][0] + self.coords[i][1][0] - leftmost) * DEFAULT_TORSO_X_OFFSET
                    sprite.blit(pygame.image.load(getBodypartSprite(self.body_list[i], self.orientation)),
                                (x_pos, y_pos))

        # pygame.image.save(sprite, "testsprite.png")
        self.sprite = sprite
        return sprite


def getBodypartSprite(bodypart, creature_orientation):

    if isinstance(bodypart, Torso):
        return DEFAULT_TORSO
    elif isinstance(bodypart, Head):
        head_orientation = bodypart.orientation
        if np.array_equal(creature_orientation, EAST):
            head_orientation = ROT90 @ head_orientation
        elif np.array_equal(creature_orientation, SOUTH):
            head_orientation = ROT180 @ head_orientation
        elif np.array_equal(creature_orientation, WEST):
            head_orientation = ROT270 @ head_orientation

        head_assettype = bodypart.asset_type

        if np.array_equal(head_orientation, NORTH):
            head_assettype = head_assettype + "N"
        elif np.array_equal(head_orientation, EAST):
            head_assettype = head_assettype + "E"
        elif np.array_equal(head_orientation, SOUTH):
            head_assettype = head_assettype + "S"
        elif np.array_equal(head_orientation, WEST):
            head_assettype = head_assettype + "W"

        return head_assettype + ".png"

        return "app/cryptid/assets/head1_f.png"
    elif isinstance(bodypart, Limb):
        limb_orientation = bodypart.orientation
        limb_shoulder = bodypart.shoulder

        # Update relative orientation vectors to absolute orientation vectors
        if np.array_equal(creature_orientation, EAST):
            limb_orientation = ROT90 @ limb_orientation
            limb_shoulder = ROT90 @ limb_shoulder
        elif np.array_equal(creature_orientation, SOUTH):
            limb_orientation = ROT180 @ limb_orientation
            limb_shoulder = ROT180 @ limb_shoulder
        elif np.array_equal(creature_orientation, WEST):
            limb_orientation = ROT270 @ limb_orientation
            limb_shoulder = ROT270 @ limb_shoulder

        # Retrieve correct asset
        limb_assettype = bodypart.asset_type

        # Is there an easier way to get a sprite by limb and shoulder orientation .. a grid?
        if np.array_equal(limb_orientation, NORTH):
            limb_assettype = limb_assettype + "N"
        elif np.array_equal(limb_orientation, EAST):
            limb_assettype = limb_assettype + "E"
        elif np.array_equal(limb_orientation, SOUTH):
            limb_assettype = limb_assettype + "S"
        elif np.array_equal(limb_orientation, WEST):
            limb_assettype = limb_assettype + "W"

        if np.array_equal(limb_shoulder, NORTH):
            limb_assettype = limb_assettype + "N"
        elif np.array_equal(limb_shoulder, EAST):
            limb_assettype = limb_assettype + "E"
        elif np.array_equal(limb_shoulder, SOUTH):
            limb_assettype = limb_assettype + "S"
        elif np.array_equal(limb_shoulder, WEST):
            limb_assettype = limb_assettype + "W"

        return limb_assettype + ".png"
