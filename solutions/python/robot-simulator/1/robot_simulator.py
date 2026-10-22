# Globals for the directions
# Change the values as you see fit


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
transformations = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0)
}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
    def move(self, instruction):
        for letter in instruction:
            if letter == "R":
                self.direction = (self.direction + 1) % len(transformations)
            elif letter == "L":
                self.direction = (self.direction - 1) % len(transformations)
            elif letter == "A":
                x, y = self.coordinates
                dx, dy = transformations[self.direction]
                self.coordinates = (dx + x, dy + y)
                
                