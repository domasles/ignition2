from ignition2.events.event import Event
from ignition2.renderer import Renderer

import pygame as pg
import sys

class WindowEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self.types = [pg.QUIT]

    def _handle_event(self, event):
        pg.quit()
        sys.exit()
