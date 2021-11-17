import pygame
from PIL import Image
import numpy
import cv2
import os
import sys
img = Image.open("Bosses/Betsy/Map Icon Betsy.png")
class Image_Data:
    def __init__(self, image_path):
        self.image = Image.open(image_path)




width, height = img.size
croppedRow1 = img.crop((0, row - 1, width, row))


