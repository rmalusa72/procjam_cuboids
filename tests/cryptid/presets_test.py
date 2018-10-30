import pytest
import pygame

from app.cryptid.presets import *

def test_dog():
    dog = Dog(1)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/dog.png")

def test_weird_dog():
    dog = WeirdDog(1)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/weird_dog.png")

def test_left_dog():
    dog = LeftwardDog(1)
    pygame.image.save(dog.makeSprite(), "tests/cryptid/leftward_dog.png")

def test_frog():
    frog = Frog(1)
    pygame.image.save(frog.makeSprite(), "tests/cryptid/frog.png")

def test_spider():
    spider = EyeSpider(1)
    pygame.image.save(spider.makeSprite(), "tests/cryptid/spider.png")
