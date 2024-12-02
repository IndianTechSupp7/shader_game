import json
import math

def load_json(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

def get_dis(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def lerp(a, b, t):
    return a + (b-a)*t


def interpolate(x, y, step):
    """
    Gradually interpolates x towards y in steps.

    Parameters:
        x (float): The starting number.
        y (float): The target number.
        step (float): The step size for interpolation (positive).

    Returns:
        generator: A generator that yields the intermediate values of x until it reaches y.
    """
    if step <= 0:
        raise ValueError("Step size must be a positive number.")

    while abs(x - y) > step:
        x += step if y > x else -step
        yield x
    yield y  # Ensure the target value is yielded at the end.


def get_dir(a, b):
    m = get_dis(a, b)
    return [(b[0] - a[0]) / m, (b[1] - a[1]) / m]

def collide_rects(rect, rects):
    collide = []
    for r in rects:
        if rect.colliderect(r):
            collide.append(r)
    return collide

def bezier(a: float, b: float, c: float, d: float, t: float):
    # return a * (1 - t)**3 + 3*b * (1 - t)**2*t + 3*c * (1-t)*t**2 + d*t**3
    x = (1 - t)**3 * 0 + t*a*(3*(1-t)**2) + c*(3*(1-t)*t**2) + 1*t**3
    y = (1 - t)**3 * 0 + t*b*(3*(1-t)**2) + d*(3*(1-t)*t**2) + 1*t**3
    return x, y



