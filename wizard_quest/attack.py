import pygame
from pygame.sprite import Sprite

class Attack(Sprite):

    def __init__(self, wq_game):
        super().__init__()
        self.screen = wq_game.screen
        self.settings = wq_game.settings
        self.color = self.settings.attack_color

        self.rect = pygame.Rect(0, 0, self.settings.attack_width, self.settings.attack_height)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x -= self.settings.attack_speed
        self.rect.x = self.x

    def move(self, pos):
        self.rect.midright = pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_attack(self):
        pygame.draw.rect(self.screen, self.color, self.rect)