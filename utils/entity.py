import pygame
from utils import collide_rects


class Entity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size

        self.vel = [0., 0.]
        self.air_time = 0
        self.speed = 1

    def rect(self):
        return pygame.Rect(*self.pos, *self.size)


    def update(self, movement = [0, 0], layers = []):
        frame_movement = [self.vel[0] + movement[0] * self.speed, self.vel[1] + movement[1] * self.speed]
        self.collison_types = {"left" : False, "right" : False, "top" : False, "bottom" : False}


        self.vel[1] = min(self.vel[1] + 0.1, 5)

        #for layer in layers:
        self.pos[0] += frame_movement[0]
        rect = self.rect()
        for tile in collide_rects(rect, self.game.tile_map.get_collide_rects(self.pos, self.size, "layer1")):
            if frame_movement[0] > 0:
                rect.right = tile.left
                self.collison_types["right"] = True
            if frame_movement[0] < 0:
                rect.left = tile.right
                self.collison_types["left"] = True
            self.pos[0] = rect.x

        self.pos[1] += frame_movement[1]
        rect = self.rect()
        tiles = self.game.tile_map.get_collide_rects(self.pos, self.size, "layer1")
        for tile in collide_rects(rect.inflate(0, 1), tiles):
            if frame_movement[1] > 0:
                rect.bottom = tile.top
            if frame_movement[1] < 0:
                rect.top = tile.bottom
            self.pos[1] = rect.y

        for tile in collide_rects(rect.inflate(0, 1), tiles):
            if rect.bottom == tile.top:
                self.collison_types["bottom"] = True
            if rect.top == tile.bottom:
                self.collison_types["top"] = True

        if self.collison_types["bottom"] or self.collison_types["top"]:
            self.vel[1] = 0


