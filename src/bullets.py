import pygame


class Bullets(list):
    def __init__(self, *args):
        list.__init__(self, args)

    def update(self, dt, screen):
        for bullet in self:
            remove = bullet.update(dt, screen)
            if remove:
                self.bullets.remove(bullet)
