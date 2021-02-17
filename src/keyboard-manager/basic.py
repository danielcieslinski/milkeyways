from .metas import *
from os import system
import keyboard

# Mode is Context that we can switch

# ------------
# Custom Contexts

class Mode(MetaContext):
    def _set(self, state: bool):
        self.state = state
        return self.state

    def active(self) -> bool:
        return self.state


# =======================
class OSHandler():
    def bind(self, t):
        system('echo mapping')

    def unbind(self):
        system('echo unmapping')


def get_active_window():
    return system('xdotool getwindowfocus getwindowname')

# -----------

class Abbreviation(MetaMapping):
    trigger = Any
    target = Any

class Hotkey(MetaMapping):
    trigger = 'ctrl+o'
    target = (print, 'shit')

# --------

class Handler:
    name: "default"
    rules = True

    type_map = {
        Abbreviation: keyboard.add_abbreviation,
        Hotkey: keyboard.add_hotkey
    }

    def bind(self, mapping):
        k = self.add_hotkey(mapping)
        self.active_mappings.append(k)

# ---------

db = {}




