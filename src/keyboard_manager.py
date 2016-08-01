# python native module
import time

# PyUserInput module
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent

#KeyboardManager module
import util

class KeyboardManager:

    def __init__(self):
        self.keyboard_type = 'normal'

    @property
    def keyboard_type(self):
        return self._keyboard_type
    
    @keyboard_type.setter
    def keyboard_type(self, keyboard_type):
        if keyboard_type == 'special':
            self._keyboard_type = keyboard_type
        else:
            print 'keyboard_type should be normal or special'

    def generate_event(self):
        keyboard_generator = KeyboardGenerator(self.keyboard_type, 'config.json')
        keyboard_generator.generate_event()

    def listen_event(self):
        keyboard_listener = KeyboardListener(self.keyboard_type, 'config.json')
        keyboard_listener.run()


class KeyboardListener(PyKeyboardEvent):
    def __init__(self, keyboard_type, path_config):
        PyKeyboardEvent.__init__(self)
        self.keyboard_type = keyboard_type
        self.config = util.load_json(path_config)
        self.now_keyboard_event = ''

    @property
    def now_keyboard_event(self):
        return self._now_keyboard_event
    
    @now_keyboard_event.setter
    def now_keyboard_event(self, keyboard_event):
        self._now_keyboard_event = keyboard_event

    def _tap(self, event):
        k = PyKeyboard()
        #print self.config['step1']
        self.now_keyboard_event = event.Key
        now_keyboard_event = self.now_keyboard_event
        print 'hi x'
        if now_keyboard_event == 'F1':
            print len(self.config)
            #k.press_key(self.config['step1'])
            

class KeyboardGenerator():
    def __init__(self, keyboard_type, path_config):
        self.keyboard_type = keyboard_type
        self.path_config = path_config

    def generate_event(self):
        config = util.load_json(self.path_config)
        print config['step1']

def main():
    keyboard_manager = KeyboardManager()
    keyboard_manager.listen_event()
    #keyboard_manager.generate_event()

if __name__ == '__main__':
    main()