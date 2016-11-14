import time
from threading import Thread
import os, pygame
import time
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

def Update(cars):
  #TODO: add the logic of your cars here
  #HINT For filtering reasons we return a list (of cars?)
  return cars

def Draw(cars):
  for car in cars:
    _width = int(offset / 3)
    screen.blit(pygame.transform.scale(car_texture, (_width, _width)),
                     (_width + car.position.X * offset,
                      _width + car.position.Y * offset))

def Main():
  start = time.time()
  cars = [ Car(Point(0, 0)), Car(Point(2, 2)) ]
  while True:
    pygame.event.wait()
    screen.fill(green)

    entry_tile.Reset()
    entry_tile.Draw(screen)

    cars = Update(cars)
    Draw(cars)

    pygame.display.flip()
    time.sleep(1)
    
Main()