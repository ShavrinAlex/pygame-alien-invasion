import pygame as pg


class Player:
    """Class player."""


    def __init__(self, window: object):
        """Initializing all settings.

        Args:
            window (object): Root window.
        """

        self.window = window

        # Settings player.
        self.spaceship = pg.image.load('./images/Player/Spaceship.png')
        self.rect_pos = self.spaceship.get_rect(midbottom=(pg.display.get_window_size()[0]//2, pg.display.get_window_size()[1] - 10))
        self.health = 3
        self.count_shell = 5
        self.speed = 3


    def draw(self):
        """Draw player spaceship."""

        self.window.blit(self.spaceship, self.rect_pos)


    def movement(self, keys, mouse_pos, mouse_button, control_type):
        """Move player spaceship."""

        if control_type == 'keyboard':
            if keys[pg.K_a] and self.rect_pos.bottomleft[0] > 0 :
                self.rect_pos.x -= self.speed
            if keys[pg.K_d] and self.rect_pos.bottomright[0] < pg.display.get_window_size()[0]:
                self.rect_pos.x += self.speed
            if keys[pg.K_SPACE]:
                print(1)

        if control_type == 'mouse' and pg.mouse.get_focused():
            if mouse_pos[0] < self.rect_pos.centerx and self.rect_pos.bottomleft[0] > 0: 
                self.rect_pos.x -= self.speed
            if mouse_pos[0] > self.rect_pos.centerx and self.rect_pos.bottomright[0] < pg.display.get_window_size()[0]:
                self.rect_pos.x += self.speed
            if mouse_button[0]:
                print(1)
