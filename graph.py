import pygame
import numpy


class Graph:
    screen_size = (720, 720)
    background_color = (0, 0, 0)
    color = (255, 255, 255)
    zoom_rate = 0.05

    def __init__(self):
        self.screen = pygame.Surface(self.screen_size)
        self.x_bounds = [-10, 10]
        self.y_bounds = [-10, 10]

    def update(self, func):
        self.screen.fill(self.background_color)
        self.draw_grid()
        self.draw_func(func)

    def draw_grid(self):
        self.draw_line(-self.screen_size[0] // 2, 0, self.screen_size[0] // 2, 0)
        self.draw_line(0, self.screen_size[1] // 2, 0, -self.screen_size[1] // 2)

    def draw_line(self, start_x, start_y, end_x, end_y):
        start = [start_x + self.screen_size[0] // 2, -start_y + self.screen_size[1] // 2]
        end = [end_x + self.screen_size[0] // 2, -end_y + self.screen_size[1] // 2]
        try:
            pygame.draw.line(self.screen, self.color, start, end)
        except TypeError:
            return

    def draw_func(self, func):
        last_x, last_y = None, None
        for x in numpy.linspace(self.x_bounds[0], self.x_bounds[1], self.screen_size[0]):
            x_coord = x * self.screen_size[0] / (abs(self.x_bounds[0]) + self.x_bounds[1])
            try:
                y = func(x) * self.screen_size[1] / (abs(self.y_bounds[0]) + self.y_bounds[1])
                if last_x is not None and last_y is not None:
                    self.draw_line(last_x, last_y, x_coord, y)
                last_x, last_y = x_coord, y
            except TypeError:
                continue

    def increase_x_bounds(self):
        self.x_bounds[0] *= 1 + self.zoom_rate
        self.x_bounds[1] *= 1 + self.zoom_rate

    def decrease_x_bounds(self):
        self.x_bounds[0] *= 1 - self.zoom_rate
        self.x_bounds[1] *= 1 - self.zoom_rate

    def increase_y_bounds(self):
        self.y_bounds[0] *= 1 + self.zoom_rate
        self.y_bounds[1] *= 1 + self.zoom_rate

    def decrease_y_bounds(self):
        self.y_bounds[0] *= 1 - self.zoom_rate
        self.y_bounds[1] *= 1 - self.zoom_rate
