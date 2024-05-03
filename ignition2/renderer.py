from includes import *

class Renderer:
    def __init__(self, window: Window, vert_shader: str=None, frag_shader: str=None) -> None:
        self.window = window
        self.ctx = window.ctx

        self.objs = []

        self.vert_shader = vert_shader
        self.frag_shader = frag_shader
        self.shaders = None

        self.vbo = None
        self.vao = None

    def render(self):
        for obj in self.objs:
            if obj.shaders == None:
                obj.shaders = self._get_shaders(self.vert_shader, self.frag_shader)
            if obj.vbo == None:
                obj.vbo = self._get_vbo(obj)
            if obj.vao == None:
                obj.vao = self._get_vao(obj.shaders, obj.vbo)

            obj.vao.render()

    def destroy(self):
        for obj in self.objs:
            obj.shaders.release()
            obj.vbo.release()
            obj.vao.release()

    def add_obj(self, obj):
        if obj not in self.objs:
            self.objs.append(obj)

    def remove_obj(self, obj):
        if obj in self.objs:
            self.objs.remove(obj)

    def _get_vert_data(self, obj):
        return np.array(obj.vert_data, "f4")
    
    def _get_vao(self, shaders, vbo):
        return self.ctx.vertex_array(shaders, [(vbo, "2f", "in_pos")])
    
    def _get_vbo(self, obj):
        return self.ctx.buffer(self._get_vert_data(obj))
    
    def _get_shaders(self, vert_shader, frag_shader):
        if vert_shader == None:
            with open("ignition2/shaders/default.vert") as f:
                vert_shader = f.read()
        else:
            with open(self.vert_shader) as f:
                vert_shader = f.read()

        if frag_shader == None:
            with open("ignition2/shaders/default.frag") as f:
                frag_shader = f.read()
        else:
            with open(self.vert_shader) as f:
                frag_shader = f.read()

        return self.ctx.program(vert_shader, frag_shader)
