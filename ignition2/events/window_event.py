from includes import *

class WindowEvent(Event):
    def __init__(self, window) -> None:
        super().__init__()
        self.types = [pg.QUIT]
        self.renderer = Renderer(window)

    def _handle_event(self, event):
        self.renderer.destroy()
        pg.quit()
        sys.exit()