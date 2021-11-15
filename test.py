import pygame as pg
from solar_vis import *
from solar_model import *
from solar_input import *
from solar_objects import *
import matplotlib.pyplot as plt
import thorpy
import time
import numpy as np


t = 0

input_filename = "stats.txt"

V = []
r = []
k = []
with open(input_filename, 'r') as input_file:
    for line in input_file:
        t = t + 1
        x = float(line.split()[0])
        y = float(line.split()[1])
        Vx = float(line.split()[2])
        Vy = float(line.split()[3])
        r.append(((x) ** 2 + (y) ** 2) ** 0.5)
        V.append(((Vx) ** 2 + (Vy) ** 2) ** 0.5)
        k.append(t)

fig, axs = plt.subplots(3, 1, figsize=(5, 10))

axs[0].plot(V, k)
axs[1].plot(r, k)
axs[2].plot(V, r)
plt.tight_layout()
plt.show()

