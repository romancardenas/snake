import numpy as np
from random import randint
from snake import Snake
from time import sleep
from sense_hat import SenseHat


def display_scenario(sense, scenario):
    for i in range(scenario.shape[0]):
        for j in range(scenario.shape[1]):
            red, green, blue = (0, 0, 0)
            dot = scenario[i, j]
            if dot == 'A':
                red, green, blue = (255, 255, 255)
            elif dot == 'D':
                red = 255
            elif dot == 'F':
                green = 255
            sense.set_pixel(i, j, red, green, blue)


def add_food(scenario):
    if np.sum(np.sum(scenario == 'F', axis=1), axis=0) == 0:
        x, y = scenario.shape
        while True:
            i = randint(0, x - 1)
            j = randint(0, y - 1)
            if scenario[i, j] == 'E':
                scenario[i, j] = 'F'
                break
    return scenario


if __name__ == '__main__':
    snake = Snake()
    sense = SenseHat()
    scenario = np.full((8, 8), 'E', dtype=str)
    while True:
        for event in sense.stick.get_events():
            if event.action in ('pressed', 'held'):
                if event.direction in ('right', 'left', 'up', 'down'):
                    snake.change_direction(event.direction)
        scenario = snake.move(scenario)
        scenario = add_food(scenario)
        display_scenario(sense, scenario)
        sleep(1)
