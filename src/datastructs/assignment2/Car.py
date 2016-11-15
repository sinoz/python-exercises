import pygame
import random
from Node import *
from Common import *

class Car:
    def __init__(self, curTile, canRemove):
        self.curTile = curTile
        self.canRemove = canRemove

#NOTE: TO DRAW USE THE CODE AS IN ASSIGNMENT 1