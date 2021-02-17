from typing import Callable, Set
from typing import List
import keyboard
from os import system

DEBUG = True

class KeyboardMapping:
    def __init__(self, f, args):
        self.f = f
        self.args = args
        self._unbinder: Callable

    def bind(self):
        if DEBUG:
            print('Registering mapping: ', self.f, self.args)
        self._unbinder = self.f(*self.args)

    def unbind(self):
        self._unbinder()


class Scope:
    def __init__(self, name='root'):
        self.name = name
        self.mappings: Set[KeyboardMapping] = set()
        self.was_last_active = False

        # For testing only
        self._is_active = True

    def is_active(self) -> bool:
        return self._is_active

    def set_active(self, state):
        self._is_active = state

    def add(self, mapping: KeyboardMapping):
        self.mappings.add(mapping)

    def map_keys(self):
        for k in self.mappings:
            k.bind()

    def unmap_keys(self):
        for k in self.mappings:
            k.unbind()

    def check(self):
        active = self.is_active()
        if self.was_last_active and not active:
            # Unregister mappings
            self.unmap_keys()

        if not self.was_last_active and active:
            # Register mappings
            self.map_keys()

        self.was_last_active = active
        return active

    def __repr__(self):
        return f'<Scope> name: {self.name},active: {self._is_active}, mappings: {self.mappings}'
        # self.registered.append(k.call())


class KeyboardManager:
    def __init__(self):
        self.scopes: List[Scope] = [Scope()]

    def _run_checks(self):
        for scope in self.scopes:
            scope.check()

    def callback(self, x):
        checks = list(map(lambda x: (x, x.check(),), self.scopes))
        print(x)

        for c in checks:
            print(c)

    def _hook(self):
        keyboard.hook(self.callback)

    def start(self):
        # self.scopes[0].map_keys()
        self._hook()
        keyboard.wait('esc')

    def add(self, mapping):
        self.scopes[0].add(mapping)

    def add_scope(self, scope):
        self.scopes.append(scope)

import subprocess

def cmd(command):
    out = subprocess.run([command], capture_output=True).stdout.decode()
    return out

def get_active_window():
    return cmd('xdotool getwindowfocus getwindowname')


actions = [['Active window', get_active_window]]
db = {'recorded': []}

def record():
    global DEBUG
    DEBUG = False
    keyboard.unhook_all()
    keys = keyboard.record()
    print('finifhes')
    print('keys:', keys)
    try:
        action = int(input(list(map(lambda x: x[0], actions))))
        db['recorded'].append([keys, actions[action]])
    except IndexError:
        print('Wrong index genius')

keyboard.remap_key('a', 'shift+')

km = KeyboardManager()
km.add(KeyboardMapping(keyboard.register_hotkey, ('windows+shift+=', record)))

# switchy_scope = Scope("Switchy")
# switchy_mapping = KeyboardMapping(keyboard.register_hotkey,
#                                   ('ctrl+p', (switchy_scope.set_active, not switchy_scope.is_active())))


# km.add_scope(switchy_scope)
km.start()

# https://usefulwebtool.com/math-keyboard
