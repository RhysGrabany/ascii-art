#!/usr/bin/python3

from PIL import Image
import sys

image = Image.open(sys.argv[1])
rows, columns = image.size
rgb_image = image.convert('RGB')

pixels = []
for x in range(0, rows-1):
    row = []
    for y in range(0, columns-1):
        row.append(rgb_image.getpixel((x, y))) 
    pixels.append(row)

pixel_brightness = []
for x in range(0, len(pixels)):
    row = []
    for y in range(0, len(pixels[x])):
        pixel = pixels[x][y]
        row.append(sum(pixel)/3)
    pixel_brightness.append(row)

print(pixel_brightness)


