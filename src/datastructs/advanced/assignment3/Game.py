import time
from threading import Thread
import os, pygame
import time
from Helper import *
from Tile import *
from Node import *
from Boat import *
pygame.init()
size = width, height = 768, 503
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10
entry_road, entry_rivers, bridges = build_scene(size, offset)

#faces to the right
boat_texture = pygame.image.load("Content/tanker.png").convert_alpha()
boats = [ Boat(entry_rivers.Value, False, boat_texture, offset) ]

#faces to the right
car_texture = pygame.image.load("Content/car.png").convert_alpha()
cars = [ Car(entry_road.Value, False, car_texture, offset) ]

def UpdateBoats(boat):
    if not boat.canRemove:
        boat.update()
        boat.draw(screen)

def UpdateCars(car):
    if not car.canRemove:
        car.update()
        car.draw(screen)

def Main():
  start = time.time()
  frameCounter = 0
  while True:    
    pygame.event.wait()
    screen.fill(green)

    #here we draw the board, do not move
    _board = entry_road
    while not _board.IsEmpty:
      _board.Value.Draw(screen, False)
      _board = _board.Tail

    #here we draw the bridges, do not move
    _board = bridges
    while not _board.IsEmpty:
      _board.Value.Draw(screen, True)
      _board = _board.Tail

    iterate(boats, lambda n: UpdateBoats(n))
    iterate(cars, lambda n: UpdateCars(n))

    if frameCounter == 5:
        selected = select_one_random(entry_rivers)
        if selected.River and not selected.Bridge:
            boats.append(Boat(selected, False, boat_texture, offset))
    elif frameCounter == 10:
        selected = select_one_random(entry_road)
        if selected.Traverseable and not selected.River:
            cars.append(Car(select_one_random(entry_road), False, car_texture, offset))
        frameCounter = 0

    frameCounter += 1
    pygame.display.flip()
    time.sleep(0.2)
    
Main()