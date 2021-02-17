from abc import ABC, abstractmethod
import functools
from uuid import uuid4
from typing import Set, List
from treelib import Tree
from typing import Any

# ------------
# Context
# ------------
ROOT_STR = ""

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

# ------------------------
# Mapping
# -----------------------
class MetaMapping(ABC):
    trigger: Any
    target: Any
    description: str
# -----------
# | Handler |
# ----------

# def add_mapping(self, mapping: KeyboardMapping):
#     pass
# ----------
# (can assign?), (can user add there own mappings?)
# (does send data?)
# (does need an event to be passed?)
# (can there other hotkeys come up)

# ------
# type 1: has to be called
# type 2: will know himself how to remap

# ---------
from logging import log
from time import time as now
from dataclasses import dataclass

class Handler:
    """
    A context with it's own handler.

    Range of that handler is assumed to work for all children of
    All the mappings belonging to that context will be mapped
    using this handler
    """
    mappings = []
    unbind_on_disactivation: bool

    # It's necessary to unbind all mappings, which are being mapped with the handler that has range exceeding the scope
    #

    def disactivated(self):
        if self.unbind_on_disactivation:
            for b in self.mappings:
                self.unbind(b)

    def add(self, mapping):
        self.mappings.append(mapping)

    @abstractmethod
    def bind(self, mapping: KeyboardMapping):
        return self.binder.bind(mapping)

    @abstractmethod
    def unbind(self, mapping: KeyboardMapping):
        return self.unbind(mapping)

class Context(MetaContext, Handler):
    active=[False]
    def disactivated(self):

class MetaKeyboardManager(ABC):
    handlers: List[Handler]
    contexts: Tree[Context]
    mappings: [Context, Handler, List[KeyboardMapping]]

    def contexts(self):
        return self.contexts.to_json()

    @abstractmethod
    def add_handler(self):
        self.handlers.append(Handler())

    # mapping: (context, handler, [trigger -> actions])
    def add_context(self, ctx, parent='root'):
        self.contexts.append(ctx)

    @abstractmethod
    def hook(self, event):
        """Function to be called on every keypress"""
        pass

class AbstractManager(MetaContext):
    @classmethod
    @abstractmethod
    def with_handler(cls, handler):
        # cls.bind = keyboard.add_hotkey
        cls.bind = handler(cls.trigger)

    def __init__(self):
        self.bind = self.f(*self.argas)
