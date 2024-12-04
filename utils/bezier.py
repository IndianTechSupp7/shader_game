import pygame
from pygame.gfxdraw import aacircle, filled_circle
import math


def bezier(a: float, b: float, c: float, d: float, t: float):
    # return a * (1 - t)**3 + 3*b * (1 - t)**2*t + 3*c * (1-t)*t**2 + d*t**3
    x = (1 - t)**3 * 0 + t*a*(3*(1-t)**2) + c*(3*(1-t)*t**2) + 1*t**3
    y = (1 - t)**3 * 0 + t*b*(3*(1-t)**2) + d*(3*(1-t)*t**2) + 1*t**3
    return x, y


def draw_aacircle(surf, color, center, r):
    aacircle(surf, int(center[0]), int(center[1]), r, color)
    filled_circle(surf, int(center[0]), int(center[1]), r, color)


class Game:
    def __init__(self):
        pygame.init()
        self.size = self.w, self.h = (800, 800)
        self.screen = pygame.display.set_mode(self.size)
        self.display = pygame.Surface(self.size)
        self.clock = pygame.time.Clock()

        self.t = 0

        self.radius = 10

        self.size = 450
        self.offset = [175, 175]
        self.points = [0.25,0.1,0.25,1]

        self.mouse = {
            "press" : [False, False, False],
            "release" : [False, False, False],
            "pos" : (0, 0)
        }
        self.p = []

        self.g1 = False
        self.g2 = False


    def events(self):
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse["release"][0] = True
                if event.button == 2:
                    self.mouse["release"][1] = True
                if event.button == 3:
                    self.mouse["release"][2] = True
        self.mouse["pos"] = pygame.mouse.get_pos()

    def draw(self):
        pygame.draw.aaline(self.display, (100, 100, 100), self.p0, self.p1)
        pygame.draw.aaline(self.display, (100, 100, 100), self.p1, self.p2)
        pygame.draw.aaline(self.display, (100, 100, 100), self.p2, self.p3)


        draw_aacircle(self.display, (255, 0, 0), self.p1, self.radius)
        draw_aacircle(self.display, (0, 0, 255), self.p2, self.radius)
        # aacircle(self.display, int(self.p1[0]), int(self.p1[1]), self.radius, (255, 0, 0))

        draw_aacircle(self.display, (100, 100, 100), self.p0, 5)
        draw_aacircle(self.display, (100, 100, 100), self.p3, 5)

        self.p = []
        for i in range(100):
            x, y = bezier(*self.points, i/100)
            self.p.append([x * self.size + self.offset[0], y * self.size + self.offset[1]])
        pygame.draw.aalines(self.display, (255, 255, 255), False, self.p)


    def run(self):
        p = self.points.copy()

        while True:
            dt = self.clock.tick(120)/1000
            self.events()
            self.display.fill((0, 0, 0))

            self.t += 1/120 ;self.t %= 1
            self.b = bezier(*self.points, self.t)

            self.p0 = (self.offset[0], self.offset[1])
            self.p1 = (self.points[0] * self.size + self.offset[0], self.points[1] * self.size + self.offset[1])
            self.p2 = (self.points[2] * self.size + self.offset[0], self.points[3] * self.size + self.offset[1])
            self.p3 = (self.size + self.offset[0], self.size + self.offset[1])
            if pygame.mouse.get_pressed()[0]:
                if pygame.Rect(self.p1[0] - self.radius, self.p1[1] - self.radius, self.radius*2, self.radius*2).collidepoint(self.mouse["pos"]) or self.g1:
                    self.g1 = True
                    self.points[0] = (self.mouse["pos"][0] - self.offset[0]) / self.size
                    self.points[1] = (self.mouse["pos"][1] - self.offset[1]) / self.size
                elif pygame.Rect(self.p2[0] - self.radius, self.p2[1] - self.radius, self.radius*2, self.radius*2).collidepoint(self.mouse["pos"]) or self.g2:
                    self.g2 = True
                    self.points[2] = (self.mouse["pos"][0] - self.offset[0]) / self.size
                    self.points[3] = (self.mouse["pos"][1] - self.offset[1]) / self.size
            elif not pygame.mouse.get_pressed()[0]:
                self.g1 = False
                self.g2 = False
            if self.points != p:
                print(*[f"{round(i, 3)}, " for i in self.points])
            p = self.points.copy()
            self.draw()
            # pygame.draw.circle(self.display, (255, 255, 255), self.b, 10)
            pygame.draw.line(self.display, (50, 50, 50), [25, 0], [25, 50], width=2)
            pygame.draw.line(self.display, (50, 50, 50), [775, 0], [775, 50], width=2)
            draw_aacircle(self.display, (255, 255, 255), (self.b[1] * 750 + 25, 25), 10)

            # draw_aacircle(self.display, (255, 0, 0), self.mouse["pos"], 10)

            # print(self.mouse["pos"])
            # print(self.screen.get_size())

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
