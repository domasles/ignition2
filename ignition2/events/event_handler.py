from ignition2.events.window_event import _WindowEvent
from ignition2.events.input_event import _InputEvent

import pygame as pg

class EventHandler:
    def __init__(self) -> None:
        self.input = _InputEvent()
        self.window = _WindowEvent()

    def handle_events(self):
        events = self.__get_events()

        self.input.handle_events(events)
        self.window.handle_events(events)

    def __get_events(self):
        return pg.event.get()
