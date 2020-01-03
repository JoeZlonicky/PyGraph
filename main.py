import pygame
from math import *
from graph import Graph
from input_box import InputBox


class GraphingApplication:
    screen_size = (Graph.screen_size[0], Graph.screen_size[1] + InputBox.size[1])

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PyGraph")
        pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
        self.graph = Graph()
        self.input_box = InputBox()

    def loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.graph.decrease_y_bounds()
                        self.graph.decrease_x_bounds()
                    elif event.button == 5:
                        self.graph.increase_y_bounds()
                        self.graph.increase_x_bounds()
            self.input_box.handle_events(events)
            self.screen.fill(self.graph.background_color)
            self.graph.update(self.function)
            self.screen.blit(self.graph.screen, (0, 0))
            self.screen.blit(self.input_box.image, (0, self.graph.screen_size[1]))
            pygame.display.flip()

    def function(self, x):
        try:
            return eval(self.input_box.input)
        except (NameError, SyntaxError, ValueError):
            return None


if __name__ == "__main__":
    GraphingApplication().loop()
