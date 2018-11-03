import pytest
import pygame

from app.cryptid.presets import *

def test_dog():
    dog = Dog()
    pygame.image.save(dog.makeSprite(), "tests/cryptid/dog.png")

def test_weird_dog():
    dog = WeirdDog()
    pygame.image.save(dog.makeSprite(), "tests/cryptid/weird_dog.png")

def test_left_dog():
    dog = LeftwardDog()
    pygame.image.save(dog.makeSprite(), "tests/cryptid/leftward_dog.png")

def test_frog():
    frog = Frog()
    pygame.image.save(frog.makeSprite(), "tests/cryptid/frog.png")

def test_spider():
    spider = EyeSpider()
    pygame.image.save(spider.makeSprite(), "tests/cryptid/spider.png")

def test_longboy():
    lb = LongBoy()
    pygame.image.save(lb.makeSprite(), "tests/cryptid/long_boy.png")
