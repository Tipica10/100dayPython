from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_speed = 0.1

    def create_cars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(310, random.randrange(-250, 250, 15))
            self.cars.append(new_car)


    def move(self):
        for new_car in self.cars:
            new_car.backward(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        self.move_speed *= 0.95



