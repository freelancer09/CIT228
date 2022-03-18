class Settings:

    def __init__(self):
        
        # Screen settings
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Spell settings
        self.spell_diameter = 30
        self.spell_color = (255, 0, 0)
        self.spells_allowed = 4

        # Monster settings
        self.attack_color = (0, 255, 0)
        self.attack_width = 15
        self.attack_height = 6
        self.attacks_allowed = 1 
        self.monsters_allowed = 3
        self.monsters_starting = 5        
        # Positive integer; higher is less frequent   
        self.attack_frequency = 4 

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.wizard_speed = 1.5
        self.spell_speed = 3.0
        self.monster_speed = 0.75
        self.monsters_total = self.monsters_starting
        self.attack_speed = 0.75

        self.monster_points = 50

    def next_level(self):
        self.monster_speed *= self.speedup_scale
        self.attack_speed *= self.speedup_scale
        self.monster_points = int(self.monster_points * self.score_scale)
