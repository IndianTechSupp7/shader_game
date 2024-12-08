import pygame
from utils import *


GRID_COLOR = (10, 10, 10)
AXIS_COLOR = (150, 150, 150)

class Grid:
    def __init__(self, app, pos, size):
        self.app = app
        self.pos = pos
        self.size = size

        self.show_grid = True
        self.show_axis = True

        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

        self.tile_map = self.app.tile_map
        self.offset = [0, 0]

        self.mousse_pos = self.app.mouse["pos"]

    def update_surf(self,  pos, size):
        self.size = size
        self.pos = pos
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def update(self):
        #self.surf = pygame.Surface(self.size, pygame.SRCALPHA)
        self.surf.fill((0, 0, 0))
        if self.app.mouse["hold"][1]:
            self.offset[0] -= self.app.mouse["rel"][0]
            self.offset[1] -= self.app.mouse["rel"][1]

        offset_x = self.offset[0] - self.surf.width / 2
        offset_y = self.offset[1] - self.surf.height / 2

        scroll = self.app.mouse["scroll_down"] - self.app.mouse["scroll_up"]
        self.tile_map.tile_size = round(clamp(10, 64, self.tile_map.tile_size * (1.0 + scroll * .1)))


        self.tile_map.render(self.surf, [offset_x, offset_y], sh_grid=self.show_grid)

        # render center
        if self.show_axis:
            pygame.draw.line(self.surf, AXIS_COLOR, (0, self.surf.height / 2 - self.offset[1]),
                             (self.surf.width, self.surf.height / 2 - self.offset[1]))
            pygame.draw.line(self.surf, AXIS_COLOR, (self.surf.width / 2 - self.offset[0], 0),
                             (self.surf.width / 2 - self.offset[0], self.surf.height))


    def render(self, surf, offset=[0, 0]):
        surf.blit(self.surf, (self.pos[0] - offset[0], self.pos[1] - offset[1]))



