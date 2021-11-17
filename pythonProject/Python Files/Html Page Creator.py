from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
import PIL
import typing
from math import sqrt
from ColorMatcher import getRgbColors as GetColors
from itertools import groupby
import math
import random
import os
import sys
import ImageColorGrabber as ICG

"""
inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.png')
"""
file = Image.open("Larva.png")

def createImage(main_image):
    img = main_image
    width, height = img.size
    newImg = Image.new("RGBA", (width+20, height+40), (120, 20, 20))
    draw = ImageDraw.Draw(newImg);
    draw.chord((100, 75, 125, 100), 0, 360, fill='green')
    draw.chord((75, 100, 100, 125), 0, 360, fill='blue')
    draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')
    draw = ImageDraw.Draw(img)

    newImg.save("test.png")

createImage(file)