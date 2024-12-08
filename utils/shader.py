import pygame
from pygame_shaders_setup import Shader as BSahder
from pygame_shaders_setup import Texture, DEFAULT_VERTEX_SHADER, DEFAULT_FRAGMENT_SHADER, DefaultScreenShader
import moderngl

class Shader(BSahder):
    def __init__(self, vert_path = "", frag_path = ""):
        self.vert_path = vert_path or DEFAULT_VERTEX_SHADER
        self.frag_path = frag_path or DEFAULT_FRAGMENT_SHADER
        self.const_vars = {}


    def _change_notifier(self, var):
        pass

    def __setitem__(self, key, value):
        self.const_vars[key] = value
        return value


    def render(self, t=True):
        active_uniforms = {name: self.shader[name] for name in self.shader if isinstance(self.shader[name], moderngl.Uniform)}
        for var in self.const_vars:
            if var in active_uniforms:
                self.send(var, self.const_vars[var])
        return super().render(t)

    def construct(self, surf):
        super().__init__(self.vert_path, self.frag_path, surf)






class ConstUniforms:
    def __init__(self, **uniforms):
        #self._uniforms = uniforms
        for name, value in uniforms.items():
            setattr(self, name, value)
        print(self.uniforms)

    def _change_notifier(self, x):
        pass

    def update_shaders(self, shaders):
        for var in self.uniforms:
            for shader in shaders:
                shader.const_vars[var] = self.uniforms[var]
        return self
    @property
    def uniforms(self):
        return vars(self)
