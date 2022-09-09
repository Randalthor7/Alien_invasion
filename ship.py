import pygame


class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):
        """ Initalize the ship and its starting postion."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ships horizontal postion.
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's postion based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
