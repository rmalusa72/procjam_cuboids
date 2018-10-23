import sys
import pygame
from mechanics.event_manager import EventManager
from app.cryptid import all

pygame.init()

if __name__ == '__main__':
    while True:
        EventManager(pygame).listen()
