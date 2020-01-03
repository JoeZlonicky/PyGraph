import pygame
from graph import Graph


class InputBox:
    size = (Graph.screen_size[0], 100)
    border_width = 2

    def __init__(self):
        self.font = pygame.font.SysFont("Consolas", 32)
        self.input = ""
        self.background = pygame.Surface(self.size)
        pygame.draw.rect(self.background, (255, 255, 255), self.background.get_rect(), self.border_width)
        self.image = self.background.copy()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                    self.update_image()
                else:
                    self.input += event.unicode
                    self.update_image()

    def update_image(self):
        self.image = self.background.copy()
        label = self.font.render(self.input, True, (255, 255, 255))
        label_rect = label.get_rect(centerx=self.size[0] // 2, centery=self.size[1] // 2)
        self.image.blit(label, label_rect)
