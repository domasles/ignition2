class Event:
    def __init__(self) -> None:
        self.types: list = None

    def _handle_events(self, events):
        for event in events:
            if event.type in self.types:
                self._handle_event(event)

    def _handle_event(self, event): ...
