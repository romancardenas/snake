import numpy as np
from time import sleep
from sense_hat import SenseHat


class Snake:
    def __init__(self, direction='right', position=None, max_x=8, max_y=8):
        self.alive = True
        self.direction = direction
        self.position = position
        if self.position is None:
            self.position = [(max_x // 2, max_y // 2)]
    
    def change_direction(self, new_direction):
        print('New direction: {}'.format(new_direction))
        self.direction = new_direction

    def fill_scenario(self, scenario):
        scenario[scenario == 'AS'] = 'E'
        scenario[scenario == 'DS'] = 'E'
        state = 'AS' if self.alive else 'DS'
        for x, y in self.position:
            scenario[x, y] = state
        return scenario
    
    def move(self, scenario):
        if self.alive:
            x, y = self.position[len(self.position) - 1]
            x = (x + {'left': -1, 'right': 1}.get(self.direction, 0)) % scenario.shape[0]
            y = (y + {'up': -1, 'down': 1}.get(self.direction, 0)) % scenario.shape[1]
            if (x, y) in self.position:
                self.alive = False
            else:
                self.position.append((x, y))
                if scenario[x, y] != 'F':
                    self.position.pop(0)
        return self.fill_scenario(scenario)


if __name__ == '__main__':
    snake = Snake()
    sense = SenseHat()
    scenario = np.full((8, 8), 'E', type=str)
    while True:
        for event in sense.stick.get_events():
            if event.action in ('pressed', 'held'):
                if event.direction in ('right', 'left', 'up', 'down'):
                    snake.change_direction(event.direction)
        scenario = snake.move(scenario)
        sense.clear()
        for i in scenario.shape[0]:
            for j in scenario.shape[1]:
                red, green, blue = (0, 0, 0)
                dot = scenario[i, j]
                if dot == 'AS':
                    red, green, blue = (255, 255, 255)
                elif dot == 'DS':
                    red = 255
                sense.set_pixel(i, j, red, green, blue)
        sleep(1)
