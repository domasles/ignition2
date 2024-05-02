from ignition2.events.window_event import _WindowEvent
from ignition2.events.input_event import _InputEvent
from ignition2.window import Window

import pygame as pg

class EventHandler:
    def __init__(self, window: Window) -> None:
        self.input_event = _InputEvent()
        self.window_event = _WindowEvent(window)

    def handle_events(self):
        events = self._get_events()

        self.input_event._handle_events(events)
        self.window_event._handle_events(events)

    def _get_events(self):
        return pg.event.get()
