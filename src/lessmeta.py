from abc import ABC, abstractmethod
from local.kmanag import MappingContext
import keyboard

ROOT_STR = ""

class Application:
    def __init__(self, name: str, active=lambda x, mappings):
        self.name = name
        self._active = active
        # ------
        self.mappings: Set[KeyboardMapping] = set()
        self.was_last_active = False
        # ------
        # Here will be stored registered mappings.

    def active(self) -> bool:
        return self._active()

    def add_mapping(self, mapping):
        self.mappings.add(mapping)

    def register_mappings(self):
       self.registered =  list(map(lambda x: x.bind, self.mappings))

    def unregister_mappings(self):
        map(lambda x: x(), self.registered)

    def check(self):
        active = self.active()
        if self.was_last_active and not active:
            # Unregister mappings
            self.unregister_mappings()

        if not self.was_last_active and active:
            # Register mappings
            self.register_mappings()

        self.was_last_a
        return active

    def __repr__(self):
        return f'Handler name: {self.name}, active: {self._is_active} priority: {self.priority}, mappings: {self.mappings}'
        # self.registered.append(k.call())

Application(name="root", lambda _: True, )

if __name__ == '__main__':
    [keyboard.add_hotkey, mapping.type == 'hotkey']
    local_handler = Handler(keyboard.add_hotkey, )