from ignition2.events.renderer_event import RendererEvent
from ignition2.events.window_event import WindowEvent
from ignition2.events.input_event import InputEvent
from ignition2.window import Window

import pygame as pg

class EventHandler:
    def __init__(self, window: Window) -> None:
        self.input_event = InputEvent()
        self.window_event = WindowEvent()
        self.renderer_event = RendererEvent(window)

    def handle_events(self):
        events = self._get_events()

        self.input_event.handle_events(events)
        self.window_event.handle_events(events)
        self.renderer_event.handle_events(events)

    def _get_events(self):
        return pg.event.get()
