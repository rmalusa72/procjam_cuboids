import numpy as np
from .torso import Torso

rot90 = np.array([[0, -1], [1, 0]])


class Cryptid:

    def __init__(self, color, orientation=np.array([[0], [1]]), thorax=Torso()):
        self.color = color
        self.thorax = thorax
        self.orientation = orientation
        self.getCoords()

    # Updates body_list, coords, and num_bodyparts for current state
    # Body_list = arbitrarily ordered list of body parts generated as-needed
    # Coords = list of (x,y) coords in same order as above
    def getCoords(self):
        self.body_list = []
        self.coords = []
        self.getCoords_rec(self.thorax, np.array([[0], [0]]))
        self.num_bodyparts = len(self.body_list)

    def getCoords_rec(self, bodypart, current_coords):
        if bodypart and not (bodypart in self.body_list):
            self.body_list.append(bodypart)
            self.coords.append(current_coords)

            if isinstance(bodypart, Torso):
                self.getCoords_rec(bodypart.head, current_coords + self.orientation)
                self.getCoords_rec(bodypart.right, current_coords - rot90 @ self.orientation)
                self.getCoords_rec(bodypart.tail, current_coords - self.orientation)
                self.getCoords_rec(bodypart.left, current_coords + rot90 @ self.orientation)

    def rotate(self, newOrientation):
        self.orientation = newOrientation
        self.getCoords()

    def makeSprite(self):
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

        sprite = pygame.Surface((DEFAULT_TORSO_WIDTH + (rightmost - leftmost)*DEFAULT_TORSO_X_OFFSET, DEFAULT_TORSO_HEIGHT + (max_layer - min_layer)*DEFAULT_TORSO_Y_OFFSET))
        sprite.set_colorkey((255,0,255))
        sprite.fill((255,0,255))

        for cur_layer in range(min_layer, max_layer + 1):
            #print(cur_layer)
            #pygame.image.save(sprite, "testsprite" + str(cur_layer) + ".png")
            y_pos = 0 + (cur_layer - min_layer) * DEFAULT_TORSO_Y_OFFSET
            for i in range(0, self.num_bodyparts):
                if layers[i] == cur_layer:
                    x_pos = 0 + (self.coords[i][0][0] + self.coords[i][1][0] - leftmost) * DEFAULT_TORSO_X_OFFSET
                    sprite.blit(pygame.image.load(self.body_list[i].asset_type), (x_pos, y_pos))


        #pygame.image.save(sprite, "testsprite.png")
        return sprite
