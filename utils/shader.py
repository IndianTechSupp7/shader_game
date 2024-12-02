import pygame
from pygame_shaders_setup import Shader as BSahder
from pygame_shaders_setup import Texture, DEFAULT_VERTEX_SHADER, DEFAULT_FRAGMENT_SHADER

class Shader(BSahder):
    def __init__(self, vert_path = "", frag_path = ""):
        self.vert_path = vert_path or DEFAULT_VERTEX_SHADER
        self.frag_path = frag_path or DEFAULT_FRAGMENT_SHADER

    def construct(self, surf):
        super().__init__(self.vert_path, self.frag_path, surf)
