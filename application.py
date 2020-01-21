import pygame
from math import *
from graph import Graph
from input_box import InputBox


class Application:
    """ Graphing application that draws given input """
    SCREEN_SIZE = (Graph.SIZE[0], Graph.SIZE[1] + InputBox.SIZE[1])

    def __init__(self):
        """ Creating a new application """
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("PyGraph")
        pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
        self.graph = Graph()
        self.input_box = InputBox()
        self.loop()

    def loop(self):
        """ Event and draw loop """
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.graph.zoom_in()
                    elif event.button == 5:
                        self.graph.zoom_out()
            self.input_box.handle_events(events)
            self.graph.update(self.function)
            self.screen.blit(self.graph.image, (0, 0))
            self.screen.blit(self.input_box.image, (0, self.graph.SIZE[1]))
            pygame.display.flip()

    def function(self, x):
        """ To be passed to the graph """
        try:
            return eval(self.input_box.input)
        except (NameError, SyntaxError, ValueError):
            return None


if __name__ == "__main__":
    Application()
