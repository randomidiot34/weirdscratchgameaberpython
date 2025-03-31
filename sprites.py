import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        self.game = game

        #Define render Layer
        self._layer = PLAYER_LAYER

        #Define group
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

        self.collide_balls()

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.grounded:
            self.grounded = False
            self.velocity_y = PLAYER_JUMPFORCE
            self.rect.y -= 10

    def collide_balls(self):
        hits = pygame.sprite.spritecollide(self, self.game.balls, False, pygame.sprite.collide_circle)
        if hits:
            self.game.running = False

class Ground(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        #Define render layer
        self._layer = GROUND_LAYER

        #Define groups
        self.groups = self.game.all_sprites, self.game.ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        #Define image
        self.image = pygame.Surface([GROUND_WIDTH, GROUND_HEIGHT])
        self.image.fill(GREEN)

        #Define rect and position
        self.rect = self.image.get_rect()
        self.rect.y = GROUND_LEVEL

class Baseball(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        #Define render layer
        self._layer = BASEBALL_LAYER
        
        #Define groups
        self.groups = self.game.all_sprites, self.game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)

        #Define image
        self.image = pygame.Surface([BASEBALL_DIAMETER, BASEBALL_DIAMETER], pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        #Define rect and circle
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, BLUE, (BASEBALL_DIAMETER/2, BASEBALL_DIAMETER/2), BASEBALL_DIAMETER/2)
        self.rect.y = BASEBALL_Y
        self.rect.x = BASEBALL_X

    def update(self):
        self.rect.x -= BASEBALL_SPEED

        if self.rect.right < 0:
            self.rect.x = WIN_WIDTH
            self.game.score += 1

class Score(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        #Define render layer
        self._layer = TEXT_LAYER

        #Define groups
        self.groups = self.game.all_sprites, self.game.text
        pygame.sprite.Sprite.__init__(self, self.groups)

        #Define initial text
        self.text = self.game.font.render(f"Score: {self.game.score}", False, BLACK)
        self.image = self.text.convert_alpha()

        #Define rect
        self.rect = self.text.get_rect()

    def update(self):
        self.text = self.game.font.render(f"Score: {self.game.score}", False, BLACK)
        self.image = self.text.convert_alpha()
