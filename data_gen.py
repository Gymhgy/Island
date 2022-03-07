from random import random
from math import dist, sqrt, pi, cos, sin, trunc, isclose
import numpy as np
import csv


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def setup(radius):
    def rand():
        def truncate(number, digits) -> float:
            stepper = 10.0 ** digits
            return trunc(stepper * number) / stepper
        theta = random() * 2 * pi
        r = sqrt(random()) * radius
        return truncate(cos(theta) * r, 3), truncate(sin(theta) * r, 3)
    
    data = [*rand(), *rand(), *rand(), *rand(), *rand()]
    while len(set(data)) != len(data):
        data = [*rand(), *rand(), *rand(), *rand(), *rand()]
    return data
with open('islanddata.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for i in range(1000):
        writer.writerow(setup(20))
