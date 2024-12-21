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


    def update(self, movement = [0, 0], layers = [], dt=1):
        frame_movement = [self.vel[0] + movement[0] * self.speed * dt, self.vel[1] + movement[1] * self.speed * dt]
        self.collison_types = {"left" : None, "right" : None, "top" : None, "bottom" : None}


        self.vel[1] = min(self.vel[1] + 0.1, 5)

        #for layer in layers:
        self.pos[0] += frame_movement[0]
        rect = self.rect()
        tiles = self.game.tile_map.get_collide_rects(self.pos, self.size, "layer1")
        collide_tiles = collide_rects(rect.inflate(0, 0), tiles)
        for tile in collide_rects(rect, self.game.tile_map.get_collide_rects(self.pos, self.size, "layer1")):
            if frame_movement[0] > 0:
                rect.right = tile.left
                #self.collison_types["right"] = rect.right
            if frame_movement[0] < 0:
                rect.left = tile.right
                #self.collison_types["left"] = rect.left
            self.pos[0] = rect.x

        for tile in collide_tiles:
            if rect.right == tile.left:
                self.collison_types["right"] = rect.right
            if rect.left == tile.right:
                self.collison_types["left"] = rect.left

        self.pos[1] += frame_movement[1]
        rect = self.rect()
        tiles = self.game.tile_map.get_collide_rects(self.pos, self.size, "layer1")
        collide_tiles = collide_rects(rect.inflate(0, 0), tiles)
        for tile in collide_tiles:
            if frame_movement[1] > 0:
                rect.bottom = tile.top
            if frame_movement[1] < 0:
                rect.top = tile.bottom
            self.pos[1] = rect.y

        for tile in collide_tiles:
            if rect.bottom == tile.top:
                self.collison_types["bottom"] = rect.bottom
            if rect.top == tile.bottom:
                self.collison_types["top"] = rect.top

        if self.collison_types["bottom"] is not None or self.collison_types["top"] is not None:
            self.vel[1] = 0


