import pygame.font
from pygame.sprite import Group

from wizard import Wizard

class Scoreboard:

    def __init__(self, wq_game):
        self.wq_game = wq_game
        self.screen = wq_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = wq_game.settings
        self.stats = wq_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_directions()
        self.prep_lives()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 50

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 10

    def prep_directions(self):
        self.directions_image = self.font.render("N - New Game | Q - Quit Game", True, self.text_color, self.settings.bg_color)
        self.directions_rect = self.directions_image.get_rect()
        self.directions_rect.centerx = self.screen_rect.centerx
        self.directions_rect.bottom = self.screen_rect.bottom - 10

    def prep_lives(self):
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Wizard(self.wq_game)
            life.image = pygame.transform.scale(life.image, (49, 64))
            life.rect.width = 49
            life.rect.height = 64
            life.rect.x = self.screen_rect.centerx + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.directions_image, self.directions_rect)
        self.lives.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()