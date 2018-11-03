import pytest
import pygame

from app.assets import *
from app.cryptid.presets import *
from app.cryptid.cryptid import Cryptid

def test_randomize():
    for i in range(0, 10):
        pygame.image.save(Cryptid().randomize(5).makeSprite(), F"tests/cryptid/sprite{i}.png")

def test_reproduce():
    dog = LeftwardDog()
    spider = EyeSpider()
    baby = dog.reproduce(spider)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby.png")

def test_mate():
    dog = LeftwardDog()
    spider = EyeSpider()
    baby = dog.mate(spider)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby2.png")

def test_random_mate():
    dog = Cryptid().randomize(25)
    spider = Cryptid().randomize(15)
    baby = dog.mate(spider)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby_random.png")

def test_random_mate_rotated():
    dog = Cryptid(orientation=NORTH).randomize(25)
    spider = Cryptid().randomize(15)
    baby = dog.mate(spider)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby_random_north.png")
    baby.rotate(EAST)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby_random_east.png")
    baby.rotate(SOUTH)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby_random_south.png")
    baby.rotate(WEST)
    pygame.image.save(baby.makeSprite(), "tests/cryptid/baby_random_west.png")

def test_rotate():
    dog = Dog(orientation=NORTH)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_north.png")
    dog.rotate(EAST)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_east.png")
    dog.rotate(SOUTH)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_south.png")
    dog.rotate(WEST)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/rotate_west.png")
