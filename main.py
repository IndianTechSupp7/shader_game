import pygame.key

from utils import Window
from level import TileMap
from entities import Player

class Game(Window):
    def __init__(self):
        super().__init__()

        self.tile_map = TileMap(self, "")
        self.player = Player(self)

        self.offset = [0, 0]
        self.camera_target = self.player

    def run(self):
        while True:
            self.events(press={
                pygame.K_w : lambda : self.player.jump()
            })
            self.display.fill((0, 0, 0))

            self.offset[0] += ((self.camera_target.pos[0] - self.display.width/2) - self.offset[0])/20
            self.offset[1] += ((self.camera_target.pos[1] - self.display.height/2) - self.offset[1])/20
            offset = [int(self.offset[0]), int(self.offset[1])]


            keys = pygame.key.get_pressed()
            self.player.update([keys[pygame.K_d] - keys[pygame.K_a], 0],
                               layers=["layer1"])

            self.tile_map.render(self.display, offset)
            self.player.render(self.display, offset)

            #self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            super().run()

if __name__ == '__main__':
    Game().run()
