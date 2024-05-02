class Level:
    def __init__(self, vert_data: list) -> None:
        self.vert_data = vert_data
        self.vao = None
        self.vbo = None
        self.shaders = None
