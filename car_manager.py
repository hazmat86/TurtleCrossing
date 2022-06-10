from hashlib import new
from turtle import Turtle
import random

from pkg_resources import yield_lines

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def makeCar(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.up()
        new_car.color(random.choice(COLORS))
        ran_y = random.randint(-250, 250)
        new_car.goto(300, ran_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        


