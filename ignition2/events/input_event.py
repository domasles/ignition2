from ignition2.events.event import _Event

import pygame as pg
import json
import os

class _InputEvent(_Event):
    def __init__(self) -> None:
        super().__init__()
        self.types = [pg.KEYDOWN, pg.KEYUP]
        self.keymap = os.path.abspath("ignition2/events/keymap.json")

    def _handle_event(self, event):
        if event.type == self.types[1]: return

    def _get_key(self, key):
        with open(self.keymap) as f:
            keymap = json.load(f)

        if key in keymap: return pg.key.get_pressed()[keymap[key]]
        else: return pg.key.get_pressed()[ord(key)]
