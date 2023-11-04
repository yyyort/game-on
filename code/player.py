import pygame as pg 
from settings import *

# Import Classes
from entity import Entity
from support import import_folder

class Player(Entity):
    def __init__(self, pos, group, obstacle_sprites):
        super().__init__(group)
        self.image = pg.image.load('../graphics/test/player_1.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-4, -24)
        
        self.stats = {
            'health' : 100,
            'stamina' : 50,
            'speed' : 5,
            'exp' : 0,
            'damage' : 5,
            'range' : 3,
        }
        
        self.max_stats = {
            'health' : 100,
            'stamina' : 50,
            'speed' : 7,
            'exp' : 0,
            'damage' : 10,
            'range' : 5,
        }
        
        self.gender = ''
        self.status = 'down'
        self.character_path = '../graphics/player_alt/'
        self.attacking = False
    
        self.obstacle_sprites = obstacle_sprites
    
    def import_player_assets(self):
        self.animations = { 
                        'up': [],
                        'down': [],
                        'left': [],
                        'right': [],
                        'up_idle':[],
                        'down_idle':[],
                        'left_idle':[],
                        'right_idle':[],
                        'right_attack':[],
                        'left_attack':[],
                        'down_attack':[],
                        'up_attack':[],
                        }

        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def input(self):
        keys = pg.key.get_pressed()
        if not self.attacking:
            
            # Y axis input
            if keys[pg.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pg.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
                
            # X axis input
            if keys[pg.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pg.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
    
    def get_character(self):
        if self.gender == 'female':
            self.character_path = '../graphics/player/'

            self.stats = {
            'health' : 75,
            'stamina' : 75,
            'speed' : 7,
            'exp' : 0,
            'damage' : 3,
            'range' : 5,
        }
            
            self.max_stats = {
            'health' : 75,
            'stamina' : 100,
            'speed' : 10,
            'exp' : 0,
            'damage' : 5,
            'range' : 10,
        }
            
    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.image = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.import_player_assets()
        self.input()
        self.get_status()
        self.get_character()
        self.animate()
        self.move(self.stats['speed'])      