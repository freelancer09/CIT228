import pygame
from pygame.sprite import Sprite

class Spell(Sprite):

    def __init__(self, wq_game):
        super().__init__()
        self.screen = wq_game.screen
        self.settings = wq_game.settings
        self.color = self.settings.spell_color

        self.rect = pygame.Rect(0, 0, self.settings.spell_diameter, self.settings.spell_diameter)
        self.rect.midleft = wq_game.wizard.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.spell_speed
        self.rect.x = self.x

    def draw_spell(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx , self.rect.centery), (self.rect.width / 2))