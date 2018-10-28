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


# Gives dest torso deep copies of the children of source torso
# I'M SO SORRY ABOUT HOW UGLY THIS CODE IS
def copy_torso_attributes(source, dest, direction_omitted=None):
        if not np.array_equal(direction_omitted, NORTH):
            if isinstance(source.head, Torso):
                dest.head = Torso(source.head.asset_type)
                copy_torso_attributes(source.head, dest.head, SOUTH)
            if isinstance(source.head, Head):
                dest.head = Head(source.head.orientation, source.head.asset_type)
            if isinstance(source.head, Limb):
                dest.head = Limb(source.head.orientation, source.head.shoulder, source.head.asset_type)
        if not np.array_equal(direction_omitted, EAST):
            if isinstance(source.right, Torso):
                dest.right = Torso(source.right.asset_type)
                copy_torso_attributes(source.right, dest.right, WEST)
            if isinstance(source.right, Head):
                dest.right = Head(source.right.orientation, source.right.asset_type)
            if isinstance(source.right, Limb):
                dest.right = Limb(source.right.orientation, source.right.shoulder, source.right.asset_type)
        if not np.array_equal(direction_omitted, SOUTH):
            if isinstance(source.tail, Torso):
                dest.tail = Torso(source.tail.asset_type)
                copy_torso_attributes(source.tail, dest.tail, NORTH)
            if isinstance(source.tail, Head):
                dest.tail = Head(source.tail.orientation, source.tail.asset_type)
            if isinstance(source.tail, Limb):
                dest.tail = Limb(source.tail.orientation, source.tail.shoulder, source.tail.asset_type)
        if not np.array_equal(direction_omitted, WEST):
            if isinstance(source.left, Torso):
                dest.left = Torso(source.left.asset_type)
                copy_torso_attributes(source.left, dest.left, EAST)
            if isinstance(source.left, Head):
                dest.left = Head(source.left.orientation, source.left.asset_type)
            if isinstance(source.left, Limb):
                dest.left = Limb(source.left.orientation, source.left.shoulder, source.left.asset_type)


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
        self.torsos_left = max_torsos - 1
        coords_filled = [DEFAULT_THORAX_COORD]
        self._randomize(self.thorax, DEFAULT_THORAX_COORD, coords_filled)
        self.updateCoords()

    def _randomize(self, current_torso, current_coords, coords_filled):
        socket_vectors = [NORTH, EAST, SOUTH, WEST]

        for i in range(0, len(socket_vectors)):
            next_coords = current_coords + socket_vectors[i]
            if not nparray_in_list(next_coords, coords_filled):
                # Then corresponding socket is empty
                if self.torsos_left > 0:
                    options = [Head, Limb, Torso, Torso, None, None]
                else:
                    options = [Head, Limb, None, None]
                child_class = random.choice(options)
                if child_class:

                    coords_filled.append(next_coords)

                    if child_class == Torso:
                        child = Torso()
                        self.torsos_left = self.torsos_left - 1
                        child.put_in_socket((i+2) % 4, current_torso)
                        current_torso.put_in_socket(i, child)
                        self._randomize(child, next_coords, coords_filled)

                    elif child_class == Head:
                        child = Head(socket_vectors[i])
                        current_torso.put_in_socket(i, child)

                    elif child_class == Limb:
                        child = Limb(ROT90 @ socket_vectors[i], socket_vectors[i])
                        current_torso.put_in_socket(i, child)

    # Tries for baby 20 times, returns clone of a parent if can't find valid baby
    def reproduce(self, other):
        # Instantiate baby and modifiable copies of parents (to preserve originals)
        baby = Cryptid(random.choice([self.color, other.color]))
        babysuccess = False
        babytries = 0

        parent1 = self
        parent2 = other
        parent1.updateCoords()
        parent2.updateCoords()

        while not babysuccess:
            # pick one torso from each parent to attempt to connect
            parent1_connection_point = None
            while not isinstance(parent1_connection_point, Torso):
                parent1_connection_point = random.choice(parent1.body_list)

            # print("parent1 coords: ")
            # print("parent1 point: " + str(parent1.coords[parent1.body_list.index(parent1_connection_point)]))

            parent2_connection_point = None
            while not isinstance(parent2_connection_point, Torso):
                parent2_connection_point = random.choice(parent2.body_list)

            # print("parent2 point: " + str(parent2.coords[parent2.body_list.index(parent2_connection_point)]))

            # pick a direction to attempt to connect them (vector from parent1 torso to parent2 torso)
            connection_direction = random.choice([NORTH, EAST, SOUTH, WEST])

            # print("dir: " + str(connection_direction))

            # Figure out what coordinates are occupied by semi-cryptids when aligned and attached
            parent1partialcoords = [np.array([[0],[0]])]
            parent2partialcoords = [np.copy(connection_direction)]
            if not np.array_equal(connection_direction, NORTH):
                self._getPartialCoords(parent1_connection_point.head, [parent1_connection_point], NORTH, parent1partialcoords)
                self._getPartialCoords(parent2_connection_point.tail, [parent2_connection_point], SOUTH, parent2partialcoords)
            if not np.array_equal(connection_direction, EAST):
                self._getPartialCoords(parent1_connection_point.right, [parent1_connection_point], EAST, parent1partialcoords)
                self._getPartialCoords(parent2_connection_point.left, [parent2_connection_point], WEST, parent2partialcoords)
            if not np.array_equal(connection_direction, SOUTH):
                self._getPartialCoords(parent1_connection_point.tail, [parent1_connection_point], SOUTH, parent1partialcoords)
                self._getPartialCoords(parent2_connection_point.head, [parent2_connection_point], NORTH, parent2partialcoords)
            if not np.array_equal(connection_direction, WEST):
                self._getPartialCoords(parent1_connection_point.left, [parent1_connection_point], WEST, parent1partialcoords)
                self._getPartialCoords(parent2_connection_point.right, [parent2_connection_point], EAST, parent2partialcoords)           

            # print("parent1 partial coords: " + str(parent1partialcoords))
            # print("parent2 partial coords: " + str(parent2partialcoords))

            # test1 = Cryptid(1)
            # test2 = Cryptid(2)
            # copy_torso_attributes(parent1_connection_point, test1.thorax, connection_direction)
            # copy_torso_attributes(parent2_connection_point, test2.thorax, ROT180 @ connection_direction)
            # pygame.image.save(test1.makeSprite(), "test1.png")
            # pygame.image.save(test2.makeSprite(), "test2.png")

            coord_conflict = False

            # Look for duplicate coordinates
            for coord1 in parent1partialcoords:
                for coord2 in parent2partialcoords:
                    if np.array_equal(coord1, coord2):
                        coord_conflict = True

            if coord_conflict:
                # print("Fuckt up baby ):")
                babytries = babytries + 1
                if babytries >= 20:
                    # Return a copy of parent1 or parent2
                    identical_parent = random.choice([parent1, parent2])
                    copy_torso_attributes(identical_parent.thorax, baby.thorax)
                    return baby
                continue

            # If no coordinate conflict then we can proceed in constructing the baby
            babysuccess = True
            # print("Baby !!")

            parent2_half_copy = Torso(parent2_connection_point.asset_type)

            copy_torso_attributes(parent1_connection_point, baby.thorax, connection_direction)
            copy_torso_attributes(parent2_connection_point, parent2_half_copy, ROT180 @ connection_direction)

            if np.array_equal(connection_direction, NORTH):
                baby.thorax.head = parent2_half_copy
                parent2_half_copy.tail = baby.thorax
            if np.array_equal(connection_direction, EAST):
                baby.thorax.right = parent2_half_copy
                parent2_half_copy.left = baby.thorax
            if np.array_equal(connection_direction, SOUTH):
                baby.thorax.tail = parent2_half_copy
                parent2_half_copy.head = baby.thorax
            if np.array_equal(connection_direction, WEST):
                baby.thorax.left = parent2_half_copy
                parent2_half_copy.right = baby.thorax

            baby.updateCoords()

        return baby

    def _getPartialCoords(self, bodypart, visited, current_coords, partial_coords):
        if bodypart and not (bodypart in visited):
            visited.append(bodypart)
            partial_coords.append(current_coords)

            if isinstance(bodypart, Torso):
                self._getPartialCoords(bodypart.head, visited, current_coords + NORTH, partial_coords)
                self._getPartialCoords(bodypart.right, visited, current_coords + EAST, partial_coords)
                self._getPartialCoords(bodypart.tail, visited, current_coords + SOUTH, partial_coords)
                self._getPartialCoords(bodypart.left, visited, current_coords + WEST, partial_coords)

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
