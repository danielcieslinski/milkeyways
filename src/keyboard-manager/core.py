# from keyboard import key_to_scan_codes

#TODO xmodmap bindings includding modifiers

from functools import partial
import subprocess
from os import system
from pyudev.wx import MonitorObserver

GLOBAL = 0
keyscanmap = {'a': 38, 'b': 56}

class KeyMapping:
    from_key: str
    target_key: str

    def __init__(self, a, b):
        self.from_key, self.target_key = a, b

    @classmethod
    def from_str(cls, e: str):
        return cls(*cls.parse(e))

    @staticmethod
    def parse(e: str):
        """
        :param e: 'a -> α'
        :return:
        """
        return e.replace(' ', '').split('->')

    def __repr__(self):
        return f'(from: {self.from_key}, to: {self.target_key})'

def cmd(command:str):
    return system(command)


def key_to_scan_code(k):
    return keyscanmap[k]

class XBinder:
    range: GLOBAL

    def _bind(self, mapping: KeyMapping):
        c = f'xmodmap -e "keycode {key_to_scan_code(mapping.from_key)} = {mapping.target_key}"'
        print(c)
        return cmd(c)

    def bind(self, mapping: KeyMapping):
        """
        :param mapping: Keymapping
        :return: unbind method if binding success
        """
        # if self._bind(mapping).returncode != 0:
        #     raise Exception('error binding')
        # -----------
        umapping = KeyMapping(mapping.from_key, mapping.from_key)
        return partial(self._bind, umapping)

handler = XBinder()

tmp = KeyMapping.from_str('a -> b')
ubound = handler.bind(tmp)
print(ubound)
ubound()
