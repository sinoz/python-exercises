import time
from threading import Thread
import os, pygame
import time
from random import randrange
from Tile import *
from Node import *

pygame.init()
size = width, height = 768, 503
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 30
board_size = 10
car_texture = pygame.image.load("Content\car.png").convert()
entry_tile = build_square_matrix(board_size, offset)

def Update(carList):
  for car in carList:
    n = randrange(4)

    direction = None
    if n == 0:
      direction = car.curTile.Up
    elif n == 1:
      direction = car.curTile.Down
    elif n == 2:
      direction = car.curTile.Right
    elif n == 3:
      direction = car.curTile.Left

    if not direction == None:
      if direction.Traverseable:
        car.curTile = direction

    if car.curTile.Park:
      carList.remove(car)
  return carList

def Draw(cars):
  for car in cars:
    _width = int(offset / 3)
    screen.blit(pygame.transform.scale(car_texture, (_width, _width)),
                     (_width + car.curTile.Position.X * offset,
                      _width + car.curTile.Position.Y * offset))

def Main():
  start = time.time()
  cars = [ Car(entry_tile) ]
  secondCounter = 0
  while True:
    pygame.event.wait()
    screen.fill(green)

    entry_tile.Reset()
    entry_tile.Draw(screen)

    cars = Update(cars)
    if secondCounter > 5: #TODO: compute using `start` instead?
      cars.append(Car(entry_tile))
      secondCounter = 0
    Draw(cars)

    pygame.display.flip()
    time.sleep(1)

    secondCounter += 1
    
Main()