import sys
from time import sleep
import random

import pygame

from settings import Settings
from wizard import Wizard
from spell import Spell
from monster import Monster
from game_stats import GameStats
from scoreboard import Scoreboard
from attack import Attack

class WizardQuest:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Wizard Quest")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.wizard = Wizard(self)
        self.spells = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()       

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.wizard.update()
                self._update_monsters() 
                self._update_spells()
                self._update_attacks()                
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.wizard.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = True
        elif event.key == pygame.K_SPACE:        
            self._cast_spell()
        elif event.key == pygame.K_n:
            self.start_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.wizard.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = False

    def start_game(self):
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.monsters.empty()
        self.spells.empty()
        self.wizard.center_wizard()

    def _cast_spell(self):
        if len(self.spells) < self.settings.spells_allowed:
            new_spell = Spell(self)
            self.spells.add(new_spell)

    def _update_spells(self):
        self.spells.update()

        for spell in self.spells.copy():
            if spell.rect.left > self.settings.screen_width:
                self.spells.remove(spell)
        
        self._check_spell_monster_collisions()

    def _update_attacks(self):
        for monster in self.monsters:
            monster.attacks.update()
            for attack in monster.attacks.copy():
                if attack.rect.right < 0:
                    monster.attacks.remove(attack)

    def _check_spell_monster_collisions(self):
        collisions = pygame.sprite.groupcollide(self.spells, self.monsters, True, True)

        if collisions:
            for monsters in collisions.values():
                self.stats.score += self.settings.monster_points * len(monsters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.monsters and self.settings.monsters_total < 1:
            self.spells.empty()
            self.settings.next_level()
            self.stats.level += 1
            self.settings.monsters_total = self.settings.monsters_starting + self.stats.level - 1

    def _check_attack_wizard_collisions(self):
        for monster in self.monsters:            
            if pygame.sprite.spritecollideany(self.wizard, monster.attacks):
                if self.stats.lives_left > 0:
                    self.stats.lives_left -= 1
                    self.sb.prep_lives()
                    self.settings.monsters_total += len(self.monsters)
                    self.spells.empty()                    
                    self.monsters.empty()
                    self.wizard.center_wizard()
                    sleep(0.5)                
                else:
                    self.stats.game_active = False                    

    def _create_monster(self):
        monster = Monster(self)
        monster_width, monster_height = monster.rect.size
        monster.x = self.settings.screen_width - (random.randint(1,4) * monster_width)
        monster.y = random.randint(1,(self.settings.screen_height - monster_height))
        monster.rect.x = monster.x
        monster.rect.y = monster.y
        self.monsters.add(monster)

    def _update_monsters(self):
        if len(self.monsters) < self.settings.monsters_allowed and self.settings.monsters_total > 0:
            self._create_monster()
            self.settings.monsters_total -= 1
        for monster in self.monsters.sprites():
            if monster.check_edges():
                monster.change_direction()
            monster.fire_attack()
        self.monsters.update()
        self._check_attack_wizard_collisions()        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.wizard.blitme()
        for spell in self.spells.sprites():
            spell.draw_spell()        
        self.monsters.draw(self.screen)
        for monster in self.monsters:
            for attack in monster.attacks.sprites():
                attack.draw_attack()
        self.sb.show_score()

        pygame.display.flip()

if __name__ == '__main__':
    wq = WizardQuest()
    wq.run_game()