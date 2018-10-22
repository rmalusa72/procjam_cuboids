import sys
import pygame
from mechanics.event_manager import EventManager

pygame.init()

if __name__ == '__main__':
    while True:
        EventManager(pygame).listen()
