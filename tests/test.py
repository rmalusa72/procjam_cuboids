# import pygame
# import time
# import pyganim
# import sys
# import os
# from ..cryptid.assets import *
#
# def rotate(surface, angle, pivot, offset):
#     """Rotate the surface around the pivot point.
#
#     Args:
#         surface (pygame.Surface): The surface that is to be rotated.
#         angle (float): Rotate by this angle.
#         pivot (tuple, list, pygame.math.Vector2): The pivot point.
#         offset (pygame.math.Vector2): This vector is added to the pivot.
#     """
#     rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
#     rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
#     # Add the offset vector to the center/pivot point to shift the rect.
#     rect = rotated_image.get_rect(center=pivot+rotated_offset)
#     return rotated_image, rect  # Return the rotated image and shifted rect.
#
# shoulder = [15,530]
# rect = (15, 530)
#
#
# class DisplayManager:
#     def __init__(self):
#         self.animations = []
#         self.screen = None
#         self.flcounter = 0
#         self.front_legs = []
#         self.back_leg = None
#         self.torso = None
#         self.hcounter = 0
#         self.heads = []
#
#     def initial_paint(self):
#         self.screen = pygame.display.set_mode((1000, 700), 0, 32)
#         head = pygame.image.load(HEAD1_F).convert_alpha()
#         head2, hrect2 = rotate(head, -3, (100,490), pygame.math.Vector2(55,65))
#         head3, hrect3 = rotate(head, -6, (100,490), pygame.math.Vector2(55,65))
#         head4, hrect4 = rotate(head, -9, (100,490), pygame.math.Vector2(55,65))
#         self.heads = [[head2, hrect2],[head3, hrect3],[head4, hrect4]]
#         self.heads = self.heads + list(reversed(self.heads))#
#         self.torso = pygame.image.load(BODY1).convert_alpha()
#         self.back_leg = pygame.image.load(LEG1_B_DOWN).convert_alpha()
#
#         front_leg = pygame.image.load(LEG1_F_DOWN).convert_alpha()
#         front_leg2, rect2 = rotate(front_leg, -2, shoulder, pygame.math.Vector2(45, 80))
#         front_leg3, rect3 = rotate(front_leg, -4, shoulder, pygame.math.Vector2(44, 81))
#         front_leg4, rect4 = rotate(front_leg, -6, shoulder, pygame.math.Vector2(43, 81))
#         front_leg5, rect5 = rotate(front_leg, -8, shoulder, pygame.math.Vector2(42, 82))
#         front_leg6, rect6 = rotate(front_leg, -10, shoulder, pygame.math.Vector2(41, 82))
#         self.front_legs = [[front_leg2, rect2],[front_leg3, rect3],[front_leg4, rect4],[front_leg5, rect5],[front_leg6, rect6]]
#         self.front_legs = self.front_legs + list(reversed(self.front_legs))
#         # front_leg3 = pygame.image.load('/Users/rowan/tina/procjam_cuboids/app/cryptid/assets/leg1_f_down10.png')
#         legs = [(front_leg, 100),(front_leg2, 100),(front_leg3, 100),(front_leg4, 100),(front_leg5, 100),(front_leg6, 200)]
#         leg_twitch = pyganim.PygAnimation(legs + list(reversed(legs)))
#         leg_twitch.play()
#
#         self.animations.append([leg_twitch, (15, 530)])
#         # pygame.draw.rect(self.screen, pygame.Color("#77AB59"), pygame.Rect(0, 600, 700, 100))
#
#     def update(self):
#         # TODO(@rowan) learn to update dirty rects https://www.pygame.org/docs/tut/newbieguide.html
#         self.screen.fill(NIGHT_BLUE)
#         # pygame.Color("#D2691E")
#         pygame.draw.rect(self.screen, CALM_BROWN, pygame.Rect(0, 600, 1000, 100))
#
#         self.screen.blit(self.back_leg, (100,490))
#         self.screen.blit(self.torso, (0,450))
#         # self.screen.blit(head, (100,490))
#         # self.screen.blit(head2, head_r)
#         self.screen.blit(*self.heads[int(self.hcounter)])
#         self.hcounter = (self.hcounter + 0.2) % (len(self.heads)-1)
#         # self.screen.blit(front_leg, rect)
#         self.screen.blit(*self.front_legs[int(self.flcounter)])
#         self.flcounter = (self.flcounter + 0.2) % (len(self.front_legs)-1)
#         # self.screen.blit(front_leg3, rect3)
#         # self.screen.blit(front_leg4, rect4)
#         # pygame.draw.circle(self.screen, (30, 250, 70), shoulder, 3)  # Pivot point.
#         # pygame.draw.rect(self.screen, (30, 250, 70), rect2, 1)  # The rect.
#         # self.screen.blit(front_leg, (15,530))
#
#         # for animation in self.animations:
#         #     animation[0].blit(self.screen, animation[1])
#         pygame.display.update()
