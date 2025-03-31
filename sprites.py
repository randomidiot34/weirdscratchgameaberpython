import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        self.game = game

        #Define Layer
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        #Define y velocity
        self.velocity_y = 0

        #Define image
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLACK)

        #Define rect and set position
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_X
        self.rect.bottom = GROUND_LEVEL

    def update(self):

        self.jump()
        #Grounded check
        if self.rect.bottom < GROUND_LEVEL:
           #Update y velocity
           self.velocity_y -= GRAVITY
           #Update position if not grounded
           self.rect.y -= self.velocity_y
        else:
            #Set player height to ground level
            self.rect.bottom = GROUND_LEVEL
            self.velocity_y = 0
            self.grounded = True

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.grounded:
            self.grounded = False
            self.velocity_y = PLAYER_JUMPFORCE
            self.rect.y -= 10
