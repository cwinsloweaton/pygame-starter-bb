from typing import List

import pygame
from pygame import display, draw, event
from pygame.sprite import Group

from cell import Cell

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 16

def create_grid(w: int, h: int) -> List[List[Cell]]:
    grid = []
    for i in range(h):
        row = []
        for j in range(w):
            color = (255, 0, 0)
            row.append(Cell(color, j * 16 + j, i * 16 + i, CELL_SIZE))
        grid.append(row)
    return grid

pygame.init()

screen = display.set_mode([800, 600])

grid = create_grid(20, 20)
grid[10][10].color = (0, 255, 0)
grid_group = Group(grid)
running = True

while running:

    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    grid_group.draw(screen)

    display.flip()

pygame.quit()
