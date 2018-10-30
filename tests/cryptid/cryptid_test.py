import pytest
import pygame

from app.assets import *
from app.cryptid.presets import *
from app.cryptid.cryptid import Cryptid

def test_randomize():
    for i in range(0, 10):
        pygame.image.save(Cryptid(1).randomize(5).makeSprite(), F"tests/cryptid/sprite{i}.png")

def test_reproduce():
    dog = LeftwardDog(1)
    spider = EyeSpider(1)
    dog.reproduce(spider)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/baby.png")

def test_reproduce():
    dog = Dog(NORTH)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_north.png")
    dog.rotate(EAST)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_east.png")
    dog.rotate(SOUTH)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_south.png")
    dog.rotate(WEST)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_west.png")
