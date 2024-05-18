from ignition2.camera import Camera
from ignition2.window import Window

import numpy as np

class Renderer:
    def __init__(self, window: Window, vert_shader: str=None, frag_shader: str=None) -> None:
        self.window = window
        self.ctx = window.ctx

        self.camera = window.camera

        self.objs = []

        self.vert_shader = vert_shader
        self.frag_shader = frag_shader
        self.shaders = None

        self.vbo = None
        self.vao = None

    def render(self):
        for obj in self.objs:
            obj.on_init()
            obj.vao.render()

    def destroy(self):
        for obj in self.objs:
            obj.shaders.release()
            obj.vbo.release()
            obj.vao.release()

    def enable(self, obj):
        if obj not in self.objs:
            self.objs.append(obj)

    def disable(self, obj):
        if obj in self.objs:
            self.objs.remove(obj)
