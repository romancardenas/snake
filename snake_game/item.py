import numpy as np


class Item:
    scenario = None

    def __init__(self, position=None, scenario=None):
        if scenario is not None:
            Item.scenario = scenario
        self.position = [(Item.scenario.max_x // 2, Item.scenario.max_y // 2)] if position is None else position.copy()
        self.alive = True

    def is_alive(self):
        return self.alive

    def run(self):
        pass
