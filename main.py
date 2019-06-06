#!/usr/bin/python3

from PIL import Image
import sys

image = Image.open(sys.argv[1])
image = image.transpose(Image.ROTATE_90)
height, width = image.size

new_width = 120
new_height = 150

img = image.resize((new_width, new_height), Image.ANTIALIAS)

rgb_image = img.convert('RGB')

pixels = []
for x in range(0, new_width):
    row = []
    for y in range(0, new_height):
        row.append(rgb_image.getpixel((x, y))) 
    pixels.append(row)

pixel_brightness = []
for x in range(0, len(pixels)):
    row = []
    for y in range(0, len(pixels[x])):
        pixel = pixels[x][y]
        row.append(sum(pixel)/3)
    pixel_brightness.append(row)

brightness_levels = ('`^",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$')

constant = 255/65

pixel_ascii = []
for x in range(0, len(pixel_brightness)):
    row = []
    for y in range(0, len(pixel_brightness[x])):
        pixelb = pixel_brightness[x][y]
        ascii_c = int(pixelb/constant)
        #print(ascii_c)
        for n in range(0, 3):
            row.append(brightness_levels[ascii_c-1])
    pixel_ascii.append(row)

for x in range(0, len(pixel_ascii)):
    print(*pixel_ascii[x], sep='')
#print(*pixel_ascii, sep='')
