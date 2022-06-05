import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carman = CarManager()

screen.listen()
screen.onkeypress(player.hop, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carman.makeCar()
    carman.move_cars()
    
    
