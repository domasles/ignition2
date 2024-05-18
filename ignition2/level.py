from ignition2.window import Window

import numpy as np
import glm

class Level:
    def __init__(self, window: Window, vert_shader: str=None, frag_shader: str=None) -> None:
        self.ctx = window.ctx
        self.camera = window.camera

        self.vertices = [(-1, -1), ( 1, -1), (1, 1), (-1, 1)]
        self.indices = [(0, 2, 3), (0, 1, 2)]

        self.shaders = None
        self.vert_shader = vert_shader
        self.frag_shader = frag_shader

        self.vbo = None
        self.vao = None

        self.model_m = self.__get_model_m()

    def on_init(self):
        if self.shaders == None:
                self.shaders = self.__get_shaders(self.vert_shader, self.frag_shader)
                self.shaders["model_m"].write(self.model_m)
                self.shaders["proj_m"].write(self.camera.proj_m)
                self.shaders["view_m"].write(self.camera.view_m)

        if self.vbo == None:
            self.vbo = self.__get_vbo(self)

        if self.vao == None:
            self.vao = self.__get_vao(self.shaders, self.vbo)

    def __get_vert_data(self, obj):
        data = [obj.vertices[ind] for triangle in obj.indices for ind in triangle]
        return np.array(data, "f4")
    
    def __get_vao(self, shaders, vbo):
        return self.ctx.vertex_array(shaders, [(vbo, "2f", "in_pos")])
    
    def __get_vbo(self, obj):
        return self.ctx.buffer(self.__get_vert_data(obj))
    
    def __get_shaders(self, vert_shader, frag_shader):
        if vert_shader == None:
            with open("ignition2/shaders/default.vert") as f:
                vert_shader = f.read()
        else:
            with open(vert_shader) as f:
                vert_shader = f.read()

        if frag_shader == None:
            with open("ignition2/shaders/default.frag") as f:
                frag_shader = f.read()
        else:
            with open(vert_shader) as f:
                frag_shader = f.read()

        return self.ctx.program(vert_shader, frag_shader)

    def __get_model_m(self):
        return glm.mat4()
