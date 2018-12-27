from sense_hat import SenseHat

class Snake:
    def __init__(self, direction='right', position=None, max_x=8, max_y=8):
        self.alive = True
        self.direction = direction
        self.position = position
        if self.position is None:
            self.position = [max_x // 2, max_y // 2]
    
    def change_direction(self, new_direction):
        print('New direction: {}'.format(new_direction))
        self.direction = new_direction
    
    def move(self, scenario):
        pass

if __name__ == '__main__':
    snake = Snake()
    sense = SenseHat()
    while True:
        for event in sense.stick.get_events():
            if event.action in ('pressed', 'held'):
                if event.direction in ('right', 'left', 'up', 'down'):
                    snake.change_direction(event.direction)

