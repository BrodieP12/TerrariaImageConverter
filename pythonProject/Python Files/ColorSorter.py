from PIL import Image
import typing
from math import sqrt
from ColorMatcher import getRgbColors as GetColors
from itertools import groupby
import math
import random
import os
import sys
from lrange import xrange


file = open("../Text Files/TerrariaBlockColors.txt")

lines = file.readlines()
BlockCount = {}
Blocks = []
Colors1 = []

for i in lines:
    line = i.split("|")
    Blocks.append(line[0])
    Colors1.append(line[1])
Colors2 = []
for i in Colors1:
    line = i.split("\n")
    Colors2.append(line[0])
Colors = []
for i in Colors2:
    line = i.split("(")
    line = line[1].split(")")
    line = line[0]
    res = tuple(map(int, line.split(', ')))
    Colors.append(res)
def closest_color(color, list):
    r, g, b = color
    color_diffs = []
    for color in list:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
"""UsedBlocks = []
for i in range(256):
    for j in range(256):
        for k in range(256):
            cc = closest_color((i, j, k), Colors)
            if Blocks[Colors.index(cc)] not in UsedBlocks:
               UsedBlocks.append(Blocks[Colors.index(cc)])
               print(Blocks[Colors.index(cc)])
            else:
                pass"""
import colorsys
from colormap import rgb2hex
from colormap import hex2rgb
def step(val, repetitions=1):
    r = val[0]
    g = val[1]
    b = val[2]
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)
    return (h2, lum, v2)
sortColors = []
for i in Colors:
    sortColors.append(i)

sortColors.sort(key=lambda val: step(val, 8))
indexes = []
running = True
print(Colors)
def getAllValues():
    for i in sortColors:
        ind = Colors.index(i)
        if ind in indexes:
            print(Colors.pop(ind))
        else:
            indexes.append(Colors.index(i))
            running = False
errors = 0
while running:
    if len(Colors) != 0:
        getAllValues()
    else:
        running = False
img = Image.open("../Pngs/ColorPallet.png").convert("RGB")
width, height = img.size
for i in range(width-1):
    img.putpixel((i, 0), sortColors[i])
img.save("ColorPallet.png")
file = open("../Text Files/BlockOrder.txt", "w")
for i in indexes:
    file.write(Blocks[i])
    file.write("\n")
file.close()

