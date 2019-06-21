#!/usr/bin/python3

from PIL import Image
import sys
import argparse


def output(args, list):

    with args.output as out:
        for i in range(0, len(pixel_ascii)):
            for j in pixel_ascii[i]:
                out.write(j)
            out.write("\n")



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Input file")
ap.add_argument("-o", "--output", required=False, type=argparse.FileType('w'), help="Output to file, else output to terminal")
ap.add_argument("-wi", "--width", required=True, type=int, help="Output size (Width)")
ap.add_argument("-he", "--height", required=True, type=int, help="Output size (Height)")


parsed = ap.parse_args()

image = Image.open(parsed.input)
image = image.transpose(Image.ROTATE_90)
height, width = image.size

new_width = parsed.width
new_height = parsed.height

img = image.resize((new_width, new_height), Image.ANTIALIAS)

new_height, new_width = img.size

rgb_image = img.convert('RGB')

pixels = []
for x in range(0, new_height):
    row = []
    for y in range(0, new_width):
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
        for n in range(0, 3):
            row.append(brightness_levels[ascii_c-1])
    pixel_ascii.append(row)


if parsed.output:
    output(parsed, pixel_ascii)
else:
    for x in range(0, len(pixel_ascii)):
        print(*pixel_ascii[x], sep='')
