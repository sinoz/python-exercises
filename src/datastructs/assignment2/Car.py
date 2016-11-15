import pygame
import random
from Node import *
from Common import *

class Car:
    def __init__(self, curTile, canRemove, texture):
        self.curTile = curTile
        self.canRemove = canRemove
        self.texture = texture

    def update(self):
        # TODO
        return None

    def draw(self, screen):
        _width = int(30 / 3)
        screen.blit(pygame.transform.scale(self.texture, (_width, _width)),
                    (_width + self.curTile.Position.X * 30,
                     _width + self.curTile.Position.Y * 30))

#NOTE: TO DRAW USE THE CODE AS IN ASSIGNMENT 1