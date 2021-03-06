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
scoreboard = Scoreboard(-175)

screen.listen()
screen.onkeypress(player.hop, "Up")

game_is_on = True
while game_is_on:
    nap = 0.1
    time.sleep(nap)
    screen.update()

    scoreboard.show_score()
    
    make_var = random.randint(0, 5)
    if make_var == 0:
        carman.makeCar()
    carman.move_cars()

    for car in carman.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 285:
        scoreboard.clear()
        scoreboard.plus_one()
        player.goto(0, -275)
        
    if player.is_finish():
        carman.level_up()
    
    
