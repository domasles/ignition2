from ignition2.events.input_event import _InputEvent

import json
import os

class InputSystem:
    def __init__(self, binds_file: str=None) -> None:
        self.input_event = _InputEvent()
        self.binds = binds_file

    def get_key(self, key: str):
        return self.input_event._get_key(key)
    
    def get_action(self, action: str):
        if self.binds == None: binds = os.path.abspath(f"ignition2/systems/default_binds.json")
        else: binds = self.binds

        with open(binds) as f:
            binds_data = json.load(f)

        if action in binds_data: return self.input_event._get_key(binds_data[action])
