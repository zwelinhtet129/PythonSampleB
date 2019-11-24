import math, colorsys
from PIL import Image, ImageDraw

spread = 17
width, height = 1000, 800
maxd = 12
len = 8.0

img = Image.new('RGB', (width,height))
d = ImageDraw.Draw(img)

def drawTree(x1, y1, angle, depth):
		if depth & amp:gt; 0:
			x2 = x1 + int(math.cos(math.radians(angle)) * depth * len)
			y2 = y1 + int(math.sin(math.radians(angle)) * depth * len)

			(r, g, b) = colorsys.hsv_to_rgb(float(depth) / maxd, 1.0, 1.0)
			R, G, B = int(255 * r), int(255 * g), int(255 * b)
			d.line([x1, y1, x2, y2],(R,G,B), depth )

			drawTree(x2, y2, angle - spread, depth - 1)
			drawTree(x2, y2, angle + spread, depth - 1)

drawTree(width / 2, height * 0.9, -90, maxd)
img.show()
img.save("Tree.png", "PNG")
			