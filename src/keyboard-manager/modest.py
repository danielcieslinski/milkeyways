from Xlib.display import Display
from Xlib import X

class KeyBinder(object):
    def __init__(self):
        self.cancel = False
        self.xdisp = Display()
        self.xroot = self.xdisp.screen().root
        self.key_code = 71 # F5

    def handle_event(self, event):
        keycode = event.detail
        print(keycode)
        if event.type == X.KeyPress:
            print(">>> event captured")
            # self.cancel = True

    def start(self):
        self.xroot.change_attributes(event_mask = X.KeyPressMask)
        self.xroot.grab_key(self.key_code, X.AnyModifier, 1, X.GrabModeAsync, X.GrabModeAsync)

        while not self.cancel:
            event = self.xroot.display.next_event()
            self.handle_event(event)

if __name__ == '__main__':
    keybinder = KeyBinder()
    keybinder.start()
    keybinder.cancel = True