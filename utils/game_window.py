import pygame
from utils.shader import DefaultScreenShader, Texture





class Window:
    def __init__(self, size=(840, 720), display_scale=1):
        pygame.init()
        self.screen = pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption("MyWindow")
        self.size = self.w, self.h = self.screen.get_size()
        self.display_scale = display_scale
        self.display = pygame.Surface((self.w*self.display_scale, self.h*self.display_scale), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()

        self.screen_shader = DefaultScreenShader(self.display)
        self.display_texture = Texture(self.display, self.screen_shader.ctx)


        self.clock = pygame.time.Clock()
        self.dt = 0


        self.mouse = {
            "press" : [False, False, False],
            "release" : [False, False, False],
            "hold" : [False, False, False],
            "pos" : (0., 0.),
            "rel" : (0., 0.),
            "scroll_up" : False,
            "scroll_down" : False,
        }


    def events(self, press = {}, release = {}):
        self.mouse["press"] = [False, False, False]
        self.mouse["release"] = [False, False, False]
        self.mouse["scroll_up"] = False
        self.mouse["scroll_down"] = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse["press"][0] = True
                    self.mouse["hold"][0] = True
                if event.button == 2:
                    self.mouse["press"][1] = True
                    self.mouse["hold"][1] = True
                if event.button == 3:
                    self.mouse["press"][2] = True
                    self.mouse["hold"][2] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse["release"][0] = True
                    self.mouse["hold"][0] = False
                if event.button == 2:
                    self.mouse["release"][1] = True
                    self.mouse["hold"][1] = False
                if event.button == 3:
                    self.mouse["release"][2] = True
                    self.mouse["hold"][2] = False
                if event.button == 4:
                    self.mouse["scroll_down"] = True
                if event.button == 5:
                    self.mouse["scroll_up"] = True
            if event.type == pygame.KEYDOWN:
                for e in press:
                    if event.key == e:
                        press[e]()
            if event.type == pygame.KEYUP:
                for e in release:
                    if event.key == e:
                        release[e]()

        mx, my = pygame.mouse.get_pos()
        self.mouse["pos"] = (mx / self.display_scale, my / self.display_scale)
        self.mouse["rel"] = pygame.mouse.get_rel()



    def run(self):
        while True:
            self.events()
            self.dt = self.clock.tick(120)/1000
            self.display.fill((100, 0, 0))

            self.screen_shader.render()
            pygame.display.flip()



