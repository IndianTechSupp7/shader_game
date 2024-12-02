import json
import math

def load_json(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

def get_dis(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

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



