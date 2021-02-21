from typing import Callable, Union, Tuple, Set, List
from abc import ABC, abstractmethod
import keyboard
import functools
from uuid import uuid4

ROOT_STR = 'root'


class KeyboardMapping:
    def __init__(self, f, args):
        self.f = f
        self.args = args
        self.res = None
        self.registered = False

    def bind(self):
        self.res = self.f(*self.args)
        self.registered = True

    def unbind(self):
        self.res()
        self.registered = False


class MetaContext(ABC):
    name: str
    parent: None
    children: []
    _id = uuid4()

    @abstractmethod
    def active(self) -> bool:
        pass

    def add_child(self, context):
        self.children.append(context)

    @functools.cache
    @property
    def abspath(self):
        # is it property for sure?
        # we could possibly create
        return ':'.join(self.walkup[::-1])

    @property
    def parents(self):
        """
        list of parents, or none if is root
        """
        try:
            return self.walkup[1:]
        except IndexError:
            return None

    @property
    def walkup(self):
        """
        :return: returns path, from self to root. Including each
        out[0] is self
        out[-1] is root
        """
        out, n = [], self
        while n.parent is not None:
            out.append(n)
            n = n.parent
        return out

    # ---------
    def asserts(self):
        # If is active there is no parent that is inactive
        if len(self.walkup) == 1:
            assert self.name == ROOT_STR

        if self.active():
            assert not any(list(map(self.parents, lambda x: not x.active())))


class MappingContext(MetaContext):
    def __init__(self, name: str, active: Callable, handler=None):
        self.name = name
        self.active = active
        self.handler = handler
        # -------
        self.handler = handler if handler is not None else self.resolve_handler()

    def resolve_handler(self):
        for n in self.parents:
            if n.bind is not None:
                return n.handler


class Context(MappingContext):
    def __init__(self, name, rule: Callable):
        self.name = name
        self.active = rule

    def handle(self, handler: Callable, args: tuple):
        """maps args """
        return handler(*args)

    def _hook(self):
        keyboard.hook(self.callback)


class KeyboardManager:
    def _run_checks(self):
        crp = lambda x: {'name': x.name, "active": x.active()}
        # list(map(crp, self.contexts))

    def start(self):
        self.contexts[0]
        self._hook()
        keyboard.wait('esc')

    def mappinh(self, mapping):
        self.scopes[0].add(mapping)

    def add_scope(self, scope):
        self.scopes.append(scope)


# --------
km = KeyboardManager()
km.binders = []

from os import system


def get_active_window():
    return system('xdotool getwindowfocus getwindowname')


class Handler:
    mappings: List[KeyboardMapping]

    def bind(self):
        pass

    def unbind(self):
        pass


class Manager:
    apps: []


class App:
    mappings =

    def map_ket(self):
        pass

    @abstractmethod
    def _is_active(self) -> bool:
        pass

    def active(self) -> bool:
        return self._is_active()



class HandledApp(App):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.state = bool

    def is_active(self):
        state = self.app.


db = {
    # 'rules': List[Union[Callable, bool]],
    'ruleset': [
        {'name': 'global',
         'active': True,
         }
    ]
}

# scope = [Keyboard.register_hotkey, ('ctrl+o', print, 'ctrl pressed')
#         KeyboardMapping(keyboard.register_hotkey, ('ctrl+o', print, 'ctrl pressed')]


# switchy_scope.add(switchy_mapping)
# km.add_scope(switchy_scope)
km.start()

#
# for _ in range(3):
#     km.check()
#     sleep(1)

# class Scope(metaclass=ABC):
#     keys: Set[KeyboardMapping]
#
#     @abstractmethod
#     def registered(self) -> bool:
#         pass
#
#     @property
#     @abstractmethod
#     def is_active(self) -> bool:
#         pass


# https://usefulwebtool.com/math-keyboard
