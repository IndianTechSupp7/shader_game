import pygame.key

from utils import TimerManager, Timer
from utils.game_window import Window
from level import TileMap
from entities import Player

class Game(Window):
    def __init__(self):
        super().__init__(display_scale=.5)

        self.timer_manager = TimerManager(self)
        Timer.TIMER_MANAGER = self.timer_manager

        self.tile_map = TileMap(self, "test_level")
        self.player = Player(self)

        self.offset = [0, 0]
        self.camera_target = self.player


    def run(self):
        while True:
            self.dt = self.clock.tick(120) / 1000
            self.display.fill((100, 0, 0))

            self.events(
                press={
                    pygame.K_w : lambda : self.player.jump()
                },
                release={
                    pygame.K_w : lambda : self.player.release_jump()
                }
            )

            self.display.fill((0, 0, 0))

            self.offset[0] += ((self.camera_target.pos[0] - self.display.width/2) - self.offset[0])/20
            self.offset[1] += ((self.camera_target.pos[1] - self.display.height/2) - self.offset[1])/20
            offset = [int(self.offset[0]), int(self.offset[1])]


            keys = pygame.key.get_pressed()
            self.player.update([keys[pygame.K_d] - keys[pygame.K_a], 0],
                               layers=["layer1"], dt=self.dt)

            self.tile_map.render(self.display, offset)
            self.player.render(self.display, offset)


            self.timer_manager.update(self.dt)
            self.screen_shader.render()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
