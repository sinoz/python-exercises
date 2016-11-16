﻿import pygame
import random
from Node import *
from Common import *

class Car:
    def __init__(self, curTile, canRemove, texture, offset):
        self.curTile = curTile
        self.canRemove = canRemove
        self.texture = texture
        self.offset = offset

    def update(self):
        # TODO
        return None

    def draw(self, screen):
        _width = int(self.offset / 3)
        screen.blit(pygame.transform.scale(self.texture, (_width, _width)),
                    (_width + self.curTile.Position.X * self.offset,
                     _width + self.curTile.Position.Y * self.offset))