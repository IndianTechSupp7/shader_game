from utils import bezier
class Timer:
    def __init__(self, duration = 1):
        self.duration = duration
        self._timer = self.duration

        self.end = 0

    def cooldown(self):
        return True if self._timer == self.end else False

    def step(self, amount=1, dt=1):
        am = amount*dt
        self._timer = max(self.end, self._timer - am)

    def reset(self):
        self._timer = self.duration

    def get(self):
        return self._timer

    def get_bezier(self, a, b, c, d):
        return bezier(a, b, c, d, self._timer)

    def __str__(self):
        return str(self._timer)

    def __repr__(self):
        return self._timer
