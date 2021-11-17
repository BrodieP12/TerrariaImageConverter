from PIL import Image

#img = Image.open("Eye of cthulhu.png").convert("RGB")

def getWidthHeight(img):
    return img.size

def getAllColors(img, widthAndHeight):
    width = widthAndHeight[0]
    height = widthAndHeight[1]
    i = img.convert("RGB")
    colors = []
    rgb = []
    for j in range(width):
        for k in range(height):
            r = i.getpixel((j, k))[0]
            g = i.getpixel((j, k))[1]
            b = i.getpixel((j, k))[2]
            rgb = [r, g, b]
            if rgb in colors:
                pass
            else:
                colors.append(rgb)
                rgb = []
    return colors

def getRGB(hex):
    h = hex.strip("#")
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return str(RGB).strip("(").strip(")")

def getRgbColors(img):
    return [tuple(i) for i in getAllColors(img, getWidthHeight(img))]