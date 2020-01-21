import pygame
import numpy


class Graph:
    """ Draws given function """
    SIZE = (720, 720)
    BACKGROUND_COLOR = (36, 34, 52)
    LINE_COLOR = (255, 255, 255)
    LINE_SPACING = 16
    GRID_COLOR = (89, 193, 53)
    ZOOM_RATE = 0.05

    def __init__(self):
        """ Create a new graph """
        self.image = pygame.Surface(self.SIZE)
        self.x_bounds = [-10, 10]
        self.y_bounds = [-10, 10]

    def update(self, func):
        """ Update image """
        self.image.fill(self.BACKGROUND_COLOR)
        self.draw_grid()
        self.draw_func(func)

    def draw_grid(self):
        """ Draw axi """
        x = 0
        while x < self.SIZE[0]:
            pygame.draw.line(self.image, self.GRID_COLOR, (x, self.SIZE[1]//2), (x + self.LINE_SPACING, self.SIZE[1]//2))
            x += self.LINE_SPACING * 2
        y = 0
        while y < self.SIZE[1]:
            pygame.draw.line(self.image, self.GRID_COLOR, (self.SIZE[0]//2, y), (self.SIZE[0]//2, y + self.LINE_SPACING))
            y += self.LINE_SPACING * 2

    def draw_line(self, start_x, start_y, end_x, end_y):
        """ Attempt to draw a line from start point to end """
        start = [start_x + self.SIZE[0] // 2, -start_y + self.SIZE[1] // 2]
        end = [end_x + self.SIZE[0] // 2, -end_y + self.SIZE[1] // 2]
        try:
            pygame.draw.line(self.image, self.LINE_COLOR, start, end)
        except TypeError:
            return

    def draw_func(self, func):
        """ Draw function """
        last_x, last_y = None, None
        for x in numpy.linspace(self.x_bounds[0], self.x_bounds[1], self.SIZE[0]):
            x_coord = x * self.SIZE[0] / (abs(self.x_bounds[0]) + self.x_bounds[1])
            try:
                y = func(x) * self.SIZE[1] / (abs(self.y_bounds[0]) + self.y_bounds[1])
                if last_x is not None and last_y is not None:
                    self.draw_line(last_x, last_y, x_coord, y)
                last_x, last_y = x_coord, y
            except TypeError:
                continue

    def zoom_in(self):
        """ Zoom in view of function """
        self.x_bounds[0] *= 1 - self.ZOOM_RATE
        self.x_bounds[1] *= 1 - self.ZOOM_RATE
        self.y_bounds[0] *= 1 - self.ZOOM_RATE
        self.y_bounds[1] *= 1 - self.ZOOM_RATE

    def zoom_out(self):
        """ Zoom out view of function """
        self.x_bounds[0] *= 1 + self.ZOOM_RATE
        self.x_bounds[1] *= 1 + self.ZOOM_RATE
        self.y_bounds[0] *= 1 + self.ZOOM_RATE
        self.y_bounds[1] *= 1 + self.ZOOM_RATE
        
