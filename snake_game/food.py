from random import randint
from snake_game.item import Item
from snake_game.snake import Snake
from snake_game.scenario import Scenario


class Food(Item):
    def __init__(self, points=10):
        super().__init__()
        self.points = points

    def is_alive(self):
        x, y = self.position[0]
        return Item.scenario.scenario[x, y] == 'F'

    def fill_scenario(self):
        x, y = self.position[0]
        if self.alive:
            Item.scenario.scenario[x, y] = 'F'

    def move(self):
        self.alive = self.is_alive()
        if not self.alive:
            while True:
                i = randint(0, Item.scenario.max_x - 1)
                j = randint(0, Item.scenario.max_y - 1)
                if Item.scenario.scenario[i, j] == 'E':
                    self.position = [(i, j)]
                    break
            self.alive = True

    def run(self):
        self.move()
        self.fill_scenario()


if __name__ == '__main__':
    scenario = Scenario(8, 8)
    game = Item(scenario=scenario)
    snake = Snake(position=[(1, 1), (1, 2), (1, 3)], scenario=scenario)
    food = Food()
    while True:
        snake.run()
        food.run()
