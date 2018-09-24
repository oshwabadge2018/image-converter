#!/usr/bin/python
import sys
import Image

imagefile = "ohs17.png"

if (len(sys.argv) > 1):
	imagefile = sys.argv[1]

img = Image.open(imagefile)
img = img.resize((128,250), Image.ANTIALIAS)
xsize = img.size[0]
ysize = img.size[1]

frame = bytearray(int(xsize/8) * ysize)

for y in xrange(img.size[1]):
	for x in xrange(img.size[0]):
		fx = xsize - 1 - x
		byte = int((fx) / 8) + 16 * y
		mask = 0x80 >> (fx % 8)
		color = img.getpixel((x,y))
		gs = color[0] * .25 + color[1] * .5 + color[2] *.25
		if gs > 128:
			frame[byte] |= mask

print("image = b'" + "".join("\\x%02x" % i for i in frame) + "'")
