from utils import bezier
class Timer:
    TIMER_MANAGER = None
    def __init__(self, duration = 1):
        self.id = id(self)
        self.duration = duration
        self._timer = 0

        self._counting = False

        self.end = 0
        if Timer.TIMER_MANAGER:
            Timer.TIMER_MANAGER.add(self)

    def start(self):
        self._counting = True

    def finish(self):
        return True if not self._timer else False

    def reset(self):
        self._counting = False
        self._timer = self.duration

    def in_cooldown(self):
        return self._timer % self.duration

    def update(self, dt=1):
        if self._counting:
            self._timer = max(0, self._timer-(1*dt))


    def get_bezier(self, a, b, c, d):
        return bezier(a, b, c, d, self.time)


    @property
    def time(self):
        return self._timer
    def __str__(self):
        return str(self.time)

    def __repr__(self):
        return self.time



class TimerManager:
    def __init__(self, app):
        self.app = app

        self.timers = {}

    def add(self, timer):
        self.timers[timer.id] = timer

    def update(self, dt=1):
        for name in self.timers:
            self.timers[name].update(dt)
