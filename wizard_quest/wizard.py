import pygame
from pygame.sprite import Sprite

class Wizard(Sprite):

    def __init__(self, wq_game):

        super().__init__()
        self.screen = wq_game.screen
        self.settings = wq_game.settings
        self.screen_rect = wq_game.screen.get_rect()

        self.image = pygame.image.load('images/wizard.png')
        self.image = pygame.transform.scale(self.image, (98, 128))
        self.rect = self.image.get_rect()

        self.center_wizard()

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.wizard_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.wizard_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_wizard(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)