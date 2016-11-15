import pygame
import random
from Node import *
from Common import *

class Boat:
    def __init__(self, position, canRemove, texture):
        self.position = position
        self.canRemove = canRemove
        self.texture = texture

    def update(self):
        # TODO

        return None

    def draw(self, screen):
        _width = int(30 / 3)
        screen.blit(pygame.transform.scale(self.texture, (_width, _width)),
                    (_width + self.position.X * 30,
                     _width + self.position.Y * 30))

#BOAT CODE HERE

#NOTE: TO DRAW USE THE CODE AS IN ASSIGNMENT 1