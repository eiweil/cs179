import png
import numpy as np
import random

width = 400
height = 400
dimension = 3

def pickcolor(mode):
	if mode is 0:
		return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
	if mode is 1:
		return [0, 0, 255]
	if mode is 2:
		return [255, 255, 0]
	if mode is 3:
		return [255, 0, 0]

def v_gradient(c2, c1, w):
	ratio = (w*1.0)/width
	return [(c1[0]*ratio) + (c2[0]*(1-ratio)), (c1[1]*ratio) + (c2[1]*(1-ratio)), (c1[2]*ratio) + (c2[2]*(1-ratio))]

def h_gradient(c2, c1, h):
	ratio = (h*1.0)/height
	return [(c1[0]*ratio) + (c2[0]*(1-ratio)), (c1[1]*ratio) + (c2[1]*(1-ratio)), (c1[2]*ratio) + (c2[2]*(1-ratio))]

for i in range(20):
	color1 = pickcolor(0)
	color2 = pickcolor(0)

	#image = (np.random.randint(256, size=(width, height))).tolist()
	image = np.zeros((height, width, dimension), dtype=np.int)
	for h in range(height):
		for w in range(width):
			image[h][w] = h_gradient(color1,color2, h)


	image = image.tolist()
	filename = "gradients/" + str(i) + "b.png"
	png.from_array(image, 'RGB').save(filename)

"""

255, 0, 0
255, 255, 0

0, 0 = 100% of c1 0% of c2
5, 5 = 50/50
5, 10 = 50/50
10, 0 = 0% of c2 100% of c1



"""



