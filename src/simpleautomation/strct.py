class SESSION(object):
    def __init__(self):
        self.actions = []
        self.randomize_sleep = 0
        self.timer_start = 5
    def to_dict(self):
        return {
            "randomize_sleep" : self.randomize_sleep,
            "timer_start" : self.timer_start
        }
    def from_dict(self, dict):
        self.randomize_sleep = dict["randomize_sleep"]
        self.timer_start = dict["timer_start"]

class ACTION_KBRD(object):
    def __init__(self, event, delay, pressed):
        self.event = event
        self.delay = delay 
        self.pressed = pressed
    def __str__(self): return "[EVENT CLAVIER " + str(self.event) + " PRESSÉ=" + str(self.pressed) +  " AVEC DÉLAI " + str(self.delay) + " sec]"
    def to_dict(self): return {
        "event" : str(self.event),
        "delay" : self.delay,
        "pressed" : self.pressed
    }

class ACTION_MOUSE(object):
    def __init__(self, x, y, _type, pressed, delay):
        self.x = x 
        self.y = y 
        self._type = _type 
        self.pressed = pressed
        self.delay = delay
    def __str__(self): return "[EVENT SOURIS " + str((self.x, self.y)) + " " + str(self._type) + " " + str(self.pressed) + " AVEC DÉLAI " + str(self.delay) + "sec]"
    def to_dict(self): return {
        "x" : self.x,
        "y" : self.y,
        "_type" : str(self._type),
        "pressed" : str(self.pressed),
        "delay" : self.delay
    }