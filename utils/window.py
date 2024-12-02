import pygame
from pygame_shaders_setup import DefaultScreenShader


class Window:
    def __init__(self):
        pygame.init()
        self.size = self.w, self.h = (840, 720)
        self.screen = pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)
        self.display = pygame.Surface((self.w/2, self.h/2))

        self.screen_shader = DefaultScreenShader(self.display)

        self.clock = pygame.time.Clock()

        self.mouse = {
            "press" : [False, False, False],
            "release" : [False, False, False],
            "pos" : (0, 0),
        }



    def events(self, press = {}, release = {}):
        self.mouse["press"] = [False, False, False]
        self.mouse["release"] = [False, False, False]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse["press"][0] = True
                if event.button == 2:
                    self.mouse["press"][1] = True
                if event.button == 3:
                    self.mouse["press"][2] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse["release"][0] = True
                if event.button == 2:
                    self.mouse["release"][1] = True
                if event.button == 3:
                    self.mouse["release"][2] = True
            if event.type == pygame.KEYDOWN:
                for e in press:
                    if event.key == e:
                        press[e]()
            if event.type == pygame.KEYUP:
                for e in release:
                    if event.key == e:
                        release[e]()
        self.mouse["pos"] = pygame.mouse.get_pos()

    def run(self):
        self.clock.tick(120)
        self.screen_shader.render()
        pygame.display.flip()

if __name__ == '__main__':
    w = Window()
    while True:
        w.events()
        w.display.fill((0, 0, 0))
        w.run()