import math
import pygame

class Ray():                # tile_map["layer"] => {"0;0" : "..."}
    def __init__(self, game, tile_map, lenght, base_dir=0, tile_size=16):
        self.game = game
        self.tile_map = tile_map
        self.lenght = lenght
        self.tile_size = tile_size
        self.base_dir = base_dir


        self.tile_found = False
        self.dis = 0
        self.max_dis = 20

    def update(self, raystart, raydir):
        self.raystart = [raystart.copy()[0] / self.tile_size, raystart.copy()[1] / self.tile_size]
        self.raydir = [math.cos(math.radians(raydir + self.base_dir)), math.sin(math.radians(raydir + self.base_dir))]


        self.rayUnitSetpsize = [math.sqrt(1 + (self.raydir[1] / (self.raydir[0]  + 1e-32)) ** 2),
                                    math.sqrt(1 + (self.raydir[0] / (self.raydir[1] + 1e-32)) ** 2)]
        self.mapCheck = [int(self.raystart.copy()[0]), int(self.raystart.copy()[1])]
        self.rayLenght1D = [float, float]
        self.Step = [int, int]

        if self.raydir[0] < 0:
            self.Step[0] = -1
            self.rayLenght1D[0] = (self.raystart[0] - float(self.mapCheck[0])) * self.rayUnitSetpsize[0]
        else:
            self.Step[0] = 1
            self.rayLenght1D[0] = (float(self.mapCheck[0] + 1) - self.raystart[0]) * self.rayUnitSetpsize[0]

        if self.raydir[1] < 0:
            self.Step[1] = -1
            self.rayLenght1D[1] = (self.raystart[1] - float(self.mapCheck[1])) * self.rayUnitSetpsize[1]
        else:
            self.Step[1] = 1
            self.rayLenght1D[1] = (float(self.mapCheck[1] + 1) - self.raystart[1]) * self.rayUnitSetpsize[1]
        self.loop()
        self.intersection = [float, float]
        if self.tile_found:
            return [self.raystart[0] + self.raydir[0] * self.dis, self.raystart[1] + self.raydir[1] * self.dis]

    def loop(self):
        self.tile_found = False
        self.dis = 0
        while not self.tile_found and self.dis < self.lenght:
            if self.rayLenght1D[0] < self.rayLenght1D[1]:
                self.mapCheck[0] += self.Step[0]
                self.dis = self.rayLenght1D.copy()[0]
                self.rayLenght1D[0] += self.rayUnitSetpsize[0]
            else:
                self.mapCheck[1] += self.Step[1]
                self.dis = self.rayLenght1D.copy()[1]
                self.rayLenght1D[1] += self.rayUnitSetpsize[1]
            #pygame.draw.circle(self.game.display, (255, 100, 100), [(self.mapCheck[0] + self.raydir[0] * self.dis) * self.tile_size, (self.mapCheck[1] + self.raydir[1] * self.dis) * self.tile_size], 4)
            #pygame.draw.circle(self.game.display, (255, 0, 0), [self.raystart[0] * self.tile_size, self.raystart[1] * self.tile_size], 4)
            if self.mapCheck[0] >= 0 and self.mapCheck[0] < self.game.w and self.mapCheck[1] >= 0 and self.mapCheck[1] < self.game.h:
                if f"{int(self.mapCheck[1])};{int(self.mapCheck[0])}" in self.tile_map["tiles"]:
                    self.tile_found = True