import pygame
from pygame import Color, Surface
from pygame.sprite import Sprite


class Cell(Sprite):
    
    def __init__(self, color: Color, x, y, size) -> 'Cell':
        super().__init__()
        self.color = color
        self.image = Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        