from collections import deque



orientation = deque('nesw')


class Rover:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.orientation = orientation[0]


    def move_forward(self):
        if self.orientation == 'n':
            self.y += 1
        elif self.orientation == 'e':
            self.x += 1
        elif self.orientation == 's':
            self.y -= 1
        else:
            self.x -= 1


    def move_back(self):
        if self.orientation == 'n':
            self.y -= 1
        elif self.orientation == 'e':
            self.x -= 1
        elif self.orientation == 's':
            self.y += 1
        else:
            self.x += 1


    def rotate(self, direction):
        if direction == 'r':
            orientation.rotate(-1)
            self.orientation = orientation[0]
        elif direction == 'l':
            orientation.rotate()
            self.orientation = orientation[0]
        else:
            print("Rover can only rotate left or right")


    def commands(self, *args):
        for arg in args:
            if arg == 'mf':
                self.move_forward()
            elif arg == 'mb':
                self.move_back()
            elif arg == 'rr':
                self.rotate('r')
            elif arg == 'rl':
                self.rotate('l')
            else:
                print("Invalid command")

    def __str__(self):
        return (f"The rover's current position is ({self.x}, {self.y}) and it is facing {self.orientation}.")