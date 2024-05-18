import glm

class Camera:
    def __init__(self) -> None:
        self.fov = 90
        self.ratio = None

        self.near = 0.01
        self.far = 1000

        self.pos = glm.vec3(0, 0, 1)
        self.up = glm.vec3(0, 1, 0)

        self.view_m = None
        self.proj_m = None

    def get_view_m(self):
        return glm.lookAt(self.pos, glm.vec3(0), self.up)

    def get_proj_m(self):
        return glm.perspective(glm.radians(self.fov), self.ratio, self.near, self.far)
