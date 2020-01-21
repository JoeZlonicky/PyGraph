import pygame
from graph import Graph


class InputBox:
    """ Handles input from user and displays it as text """
    SIZE = (Graph.SIZE[0], 100)
    FONT_SIZE = 32
    BORDER_WIDTH = 2 
    BORDER_COLOR = (89, 193, 53)
    BACKGROUND_COLOR = (36, 34, 52)

    def __init__(self):
        """ Create an input box """
        self.font = pygame.font.SysFont("Arial", 32)
        self.input = "x"
        self.image = pygame.Surface(self.SIZE)
        self.update_image()

    def handle_events(self, events):
        """ Handle keyboard input """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                    self.update_image()
                else:
                    self.input += event.unicode
                    self.update_image()

    def update_image(self):
        """ Render text """
        self.image.fill(self.BACKGROUND_COLOR)
        pygame.draw.line(self.image, self.BORDER_COLOR, (0, 0), (self.SIZE[0],0),
                self.BORDER_WIDTH)
        label = self.font.render(self.input, True, (255, 255, 255))
        label_rect = label.get_rect(centerx=self.SIZE[0] // 2, centery=self.SIZE[1] // 2)
        self.image.blit(label, label_rect)
