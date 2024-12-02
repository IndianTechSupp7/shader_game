import pygame

class Animation:
    def __init__(self, animation):
        self.frames = animation["frames"] or []
        self.type = animation["type"] or ""
        self.speed = animation["speed"] or 0.1
        self.frame = 0 if self.type != "reverse" else len(self.frames)


    def render(self):
        if self.type == "loop":
            self.frame += self.speed
            self.frame %= len(self.frames)
        elif self.type == "reverse":
            self.frame = max(self.frames - self.speed, 0)
        else:
            self.frame = min(self.frames + self.speed, len(self.frames))

        return self.frames[int(self.frame)]