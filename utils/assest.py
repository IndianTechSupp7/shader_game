import pygame
import os
from utils import generate_dict_tree

MAIN_ROOT = "data/"


class Assets:
    def __init__(self):
        self.images = self.generate_image_tree(MAIN_ROOT + "/images", key=self._image_filter)
        self._shader_filter = lambda path: os.path.join(MAIN_ROOT + "/shaders", path)
        self.maps_filter = lambda path: os.path.join(MAIN_ROOT + "/maps", path)
        self.shaders = self.generate_image_tree(MAIN_ROOT + "/shaders", key=self._shader_filter)
        self.maps = self.generate_image_tree(MAIN_ROOT + "/maps", key=self.maps_filter)



    def _image_filter(self, path):
        return pygame.image.load(os.path.join(MAIN_ROOT + "/images", path)).convert_alpha()

    @staticmethod
    def get_images():
        return [pygame.image.load(MAIN_ROOT+"images/"+i).convert_alpha() for i in os.listdir(MAIN_ROOT+"images/")]

    @staticmethod
    def get_shader(name):
        return MAIN_ROOT+"shaders/" + name

    @staticmethod
    def generate_image_tree(bpath, key=lambda x: x):
        tree = []
        for root, dirs, files in os.walk(bpath):
            #image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            for img in files:
                # Create the attribute path by replacing base folder and slashes
                relative_path = os.path.relpath(os.path.join(root, img), bpath)
                path_parts = relative_path.replace(os.sep, '-')
                #image = pygame.image.load(os.path.join(bpath, relative_path)).convert_alpha()
                tree.append([path_parts, key(relative_path)])
        return  generate_dict_tree(tree, sep="-") if tree else {}
