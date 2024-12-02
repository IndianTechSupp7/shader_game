import json

def load_json(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data


def collide_rects(rect, rects):
    collide = []
    for r in rects:
        if rect.colliderect(r):
            collide.append(r)
    return collide



