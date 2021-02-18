from abc import ABC, abstractmethod
from uuid import uuid4
import functools
import treelib
from typing import Any


# ------------
# Mappings
# ------------
class MetaMapping(ABC):
    trigger: Any
    target: Any
    description: str

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

class Context(MetaContext):
    pass

class RootContext(Context):
    name: 'root'

    def active(self) -> bool:
        return True

# ---------------

"""
1. Binder.range is not >  mapping.context

It means, that r
 If can't surpress, has to be consider the case if is input,
    then on the other hand comes up the problem, of what happens, when, the 
    handler of the binder is no longer active.
     
     To consider is:
        - conflicting_keys after removal
        - Will it still be on after the context comes back
            - Will same unbinder work?

2. Binder.range is >  mapping.context
"""
from typing import Callable, Iterable, Union, Tuple

class Action:
    target: Callable
    args: Iterable
    def __call__(self, *args, **kwargs):
        self.target()

class Binder:
    name: str
    range: Context
    _id: int

    @abstractmethod
    def bind(self, keys: str, action: [Callable, Iterable]):
        """
        :param keys:
        :param action: action[0]: Callable
        :return:
        """
        pass

    @abstractmethod
    def unbind(self):
        pass

import keyboard
class HotkeyBinder(Binder):
    name = "default hotkey binder"
    registered = []
    def bind(self, keys: str, action: [Callable, Iterable]):
        keyboard.register_hotkey(keys, *action)


# -----------------
# class AbstractApplication(MetaContext):

class KeyboardManager:
    contexts = [RootContext()]
    binders = {'global': HotkeyBinder()}
    def add_hotkey(self):
        pass

# ---------
class App:


# def run_checks(c: MetaContext):
#     # If is active there is no parent that is inactive
#     if len(c.walkup) == 1:
#         assert c.name == ROOT_STR
#
#     if self.active():
#         assert not any(list(map(self.parents, lambda x: not x.active())))
#
