import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        self.game = game

        #Define Layer
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        #Define x and y position
        self.x = PLAYER_X
        self.y = PLAYER_Y

        #Define image
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLACK)

        #Define rect and set position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass
