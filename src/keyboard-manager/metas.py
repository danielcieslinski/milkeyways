import keyboard
from typing import List
from abc import ABC


"""
We assume always surpressing for listening, so if insert after dispatch will have to emulate
Modes: one of [insert, not insert] xd
"""




class KeyboardManager(ABC):
    def from_api(self):
        self.buffer = frozenset({})

    def check_buff(self):
        return 

    def on_key_press(self, parameter_list):

        self.buffer(parameter_list)
        """
        Activate on keyboard press
        """
        raise NotImplementedError

    def on_key_release(self, parameter_list):

        """
        Activate on keyboard release key
        """
        raise NotImplementedError


KeyboardManager.register(keyboard)

