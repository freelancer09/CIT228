import pygame
import random

from pygame.sprite import Sprite
from attack import Attack

class Monster(Sprite):

    def __init__(self, wq_game):
        super().__init__()
        self.screen = wq_game.screen
        self.settings = wq_game.settings

        self.image = pygame.image.load('images/monster.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        i = random.randint(1,2)
        if i == 1:
            self.direction = 1
        else:
            self.direction = -1  

        self.attacks = pygame.sprite.Group()    

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True

    def change_direction(self):
        if self.direction == 1:
            self.direction = -1
        else:
            self.direction = 1

    def update(self):
        self.y += (self.settings.monster_speed * self.direction)
        self.rect.y = self.y

    def fire_attack(self):        
        if len(self.attacks) < self.settings.attacks_allowed:
            i = random.randint(1,self.settings.attack_frequency)
            if i == 1:
                new_attack = Attack(self)
                new_attack.move(self.rect.midleft)
                self.attacks.add(new_attack)