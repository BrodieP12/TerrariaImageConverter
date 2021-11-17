from PIL import Image, ImageDraw  # pip install pillow
import numpy as np
from matplotlib import pyplot as plt

strip_h, strip_w = 100, 720
strip = 255*np.ones((strip_h,strip_w,3), dtype='uint8')
image_val = Image.fromarray(strip)
image_sat = Image.fromarray(strip)
draw0 = ImageDraw.Draw(image_val)
draw1 = ImageDraw.Draw(image_sat)
for y in range(strip_h):
    for x in range(strip_w):
        draw0.point([x, y], fill='hsl(%d,%d%%,%d%%)'%(x%360,y,50))
        draw1.point([x, y], fill='hsl(%d,%d%%,%d%%)'%(x%360,100,y))

plt.subplot(2,1,1)
plt.imshow(image_val)
plt.subplot(2,1,2)
plt.imshow(image_sat)
plt.show()