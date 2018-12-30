import numpy as np
from random import randint
from scenario import Scenario
from item import Item
from food import Food
from snake import Snake
from time import sleep
from sense_hat import SenseHat


def display_scenario(sense, scenario):
    for i in range(scenario.shape[0]):
        for j in range(scenario.shape[1]):
            red, green, blue = (0, 0, 0)
            dot = scenario[i, j]
            if dot == 'H':
                blue = 255
            elif dot == 'A':
                red, green, blue = (255, 255, 255)
            elif dot == 'D':
                red = 255
            elif dot == 'T':
                red, green, blue = (255, 255, 255)
            elif dot == 'F':
                green = 255
            sense.set_pixel(i, j, red, green, blue)


if __name__ == '__main__':
    sense = SenseHat()
    time_to_wait = np.linspace(1000, 0, 64).astype(int).tolist()

    scenario = Scenario(8, 8)
    game = Item(scenario=scenario)
    snake = Snake(position=[(1, 1), (1, 2), (1, 3)], scenario=scenario)
    food = Food()
    i = 0
    while True:
        for event in sense.stick.get_events():
            if event.action in ('pressed', 'held'):
                if event.direction in ('right', 'left', 'up', 'down'):
                    snake.change_direction(event.direction)
        display_scenario(sense, scenario.scenario)
        sleep(time_to_wait[i] / 1000.0)
        i = snake.run() - 1
        food.run()
