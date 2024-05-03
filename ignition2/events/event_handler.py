from includes import *

class EventHandler:
    def __init__(self, window: Window) -> None:
        self.input_event = InputEvent()
        self.window_event = WindowEvent(window)

    def handle_events(self):
        events = self._get_events()

        self.input_event._handle_events(events)
        self.window_event._handle_events(events)

    def _get_events(self):
        return pg.event.get()
