from ignition2.camera import Camera

import moderngl as mgl
import pygame as pg

class Window:
    def __init__(self, width: int, height: int, camera: Camera, title: str=None, fullscreen: bool=False, target_fps: int=60, clear_col: tuple=(0, 0, 0)) -> None:
        self.width = width
        self.height = height
        self.title = title

        camera.ratio = width / height
        camera.view_m = camera.get_view_m()
        camera.proj_m = camera.get_proj_m()
        self.camera = camera

        self.fullscreen = fullscreen
        self.target_fps = target_fps

        self.clear_col = clear_col

        self.clock = pg.time.Clock()
        self.create()

    def create(self):
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 6)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        flags = pg.DOUBLEBUF | pg.OPENGL | (pg.FULLSCREEN if self.fullscreen else pg.SHOWN)

        pg.display.set_mode((self.width, self.height), flags)

        self.ctx = mgl.create_context()

    def update(self):
        pg.display.set_caption((self.title if self.title != None else str(self.get_fps())))

        pg.display.flip()

        self.ctx.viewport = (0, 0, self.width, self.height)
        self.ctx.clear(color=self.clear_col)

        self.clock.tick(self.target_fps)

    def get_fps(self):
        self.fps = round(self.clock.get_fps(), 1)
        return self.fps
