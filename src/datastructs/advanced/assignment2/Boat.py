﻿import pygame
from random import randrange
from Node import *
from Common import *

class Boat:
    def __init__(self, curTile, canRemove, texture, offset):
        self.curTile = curTile
        self.canRemove = canRemove
        self.texture = texture
        self.offset = offset

    def update(self):
        direction = randrange(4)

        nextTile = None
        if direction == 0:
            nextTile = self.curTile.Up
        elif direction == 1:
            nextTile = self.curTile.Down
        elif direction == 2:
            nextTile = self.curTile.Left
        elif direction == 3:
            nextTile = self.curTile.Right

        if nextTile is not None:
            if nextTile.River and not nextTile.Harbor:
                self.curTile = nextTile
            elif nextTile.Harbor:
                self.canRemove = True

        return None

    def draw(self, screen):
        _width = int(self.offset / 3)
        screen.blit(pygame.transform.scale(self.texture, (_width, _width)),
                    (_width + self.curTile.Position.X * self.offset,
                     _width + self.curTile.Position.Y * self.offset))