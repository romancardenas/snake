import numpy as np


class Scenario:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.scenario = np.full((self.max_x, self.max_y), 'E', dtype=str)
