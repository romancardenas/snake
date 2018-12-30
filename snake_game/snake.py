from snake_game.item import Item
from snake_game.scenario import Scenario


class Snake(Item):
    def __init__(self, direction='right', position=None, scenario=None):
        super().__init__(position, scenario)
        self.direction = direction

    def is_alive(self):
        return len(self.position) == len(set(self.position))
    
    def change_direction(self, new_direction):
        self.direction = new_direction

    def empty_scenario(self):
        for x, y in self.position:
            Item.scenario.scenario[x, y] = 'E'

    def fill_scenario(self):
        state = 'A' if self.alive else 'D'
        for x, y in self.position:
            Item.scenario.scenario[x, y] = state
        x, y = self.position[0]
        Item.scenario.scenario[x, y] = 'T'
        x, y = self.position[-1]
        Item.scenario.scenario[x, y] = 'H'
    
    def move(self):
        if self.alive:
            x, y = self.position[len(self.position) - 1]
            x = (x + {'left': -1, 'right': 1}.get(self.direction, 0)) % Item.scenario.max_x
            y = (y + {'up': -1, 'down': 1}.get(self.direction, 0)) % Item.scenario.max_y
            self.position.append((x, y))
            if self.scenario.scenario[x, y] != 'F':
                self.position.pop(0)
            self.alive = self.is_alive()

    def run(self):
        self.empty_scenario()
        self.move()
        self.fill_scenario()
        return len(self.position)


if __name__ == '__main__':
    scenario = Scenario(8, 8)
    snake1 = Snake(position=[(1, 1), (1, 2), (1, 3)], scenario=scenario)
    while True:
        snake1.run()
