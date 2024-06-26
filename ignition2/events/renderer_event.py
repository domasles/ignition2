from ignition2.events.event import Event
from ignition2.renderer import Renderer

import pygame as pg

class RendererEvent(Event):
    def __init__(self, window) -> None:
        super().__init__()
        self.types = [pg.QUIT]
        self.renderer = Renderer(window)

    def _handle_event(self, event):
        self.renderer.destroy()
