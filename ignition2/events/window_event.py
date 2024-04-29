from ignition2.events.event import Event

import pygame as pg
import sys

class _WindowEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self.types = [pg.QUIT]

    def _handle_event(self, event):
        pg.quit()
        sys.exit()