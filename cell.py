import pygame
from pygame import Color, Surface
from pygame.sprite import Sprite

class Cell(Sprite):
    
    def __init__(self, color: Color, x, y, size) -> None:
        super().__init__()
        self.color = color
        self.image = Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        print(y)
        self.rect.y = y
        