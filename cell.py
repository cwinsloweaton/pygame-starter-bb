import pygame
from pygame import Color, Surface
from pygame.sprite import Sprite


class Cell(Sprite):
    
    def __init__(self, color: Color, x, y, size) -> 'Cell':
        super().__init__()
        self._color = color
        self.image = Surface((size, size))
        self.image.fill(self._color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, color):
        self._color = color
        self.image.fill(self._color)