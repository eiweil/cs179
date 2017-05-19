from credentials import *

import png
import numpy as np
import random
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

width = 400
height = 400
dimension = 3

def tweet_image(filename):
    try:
        api.update_with_media(filename)
    except tweepy.TweepError as e:
        print(e.reason)

def get_rand_color():
	return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

def get_color_triad(c):
	s1 = random.choice([-1,1])
	s2 = random.choice([-1,1])
	s3 = random.choice([-1,1])
	c1 = [ (256+c[0]-(172*s1)) % 256, (256+c[1]+(10*s1)) % 256, c[2] ]
	c2 = [ (256+c[0]+(11*-s2)) % 256, (256+c[1]+(172*s2)) % 256, (256+c[2]-(183*s2)) % 256 ]
	c3 = [ (256+c[0]-(172*s3)) % 256, (256+c[1]+(183*s3)) % 256, (256+c[2]-(11*s3)) % 256 ]
	return [c1, c2, c3]

def pick_color(mode):	
	if mode is 1:
		return [0, 0, 255]
	if mode is 2:
		return [255, 255, 0]
	if mode is 3:
		return [255, 0, 0]

def v_gradient(c1, c2, w):
	ratio = (w*1.0)/width
	return [(c1[0]*(1-ratio)) + (c2[0]*ratio), (c1[1]*(1-ratio)) + (c2[1]*ratio), (c1[2]*(1-ratio)) + (c2[2]*ratio)]

def h_gradient(c1, c2, h):
	ratio = (h*1.0)/height
	return [(c1[0]*(1-ratio)) + (c2[0]*ratio), (c1[1]*(1-ratio)) + (c2[1]*ratio), (c1[2]*(1-ratio)) + (c2[2]*ratio)]

def dots(c1, c2, w, h):
	modw = (w+4)%20
	modh = (h+4)%20
	if modw < 8 and modh < 8:
		return c1
	else:
		return c2 
"""
def draw_random_triangles(self, bg, c1, c2, c3, w, h):
	# pick color to draw in
	color = []
	modw = w%3
	if modw is 0:
		color = c1
	if modw is 1:
		color = c2
	if modw is 2:
		color = c3

	if w%(random.randint(3,10)) is 0:
		base = random.randint(10, 30)
		for x in range(base):
			for y in range(base):

	else:
		return	
"""
for i in range(1):
	background = get_rand_color()
	#color2 = get_rand_color()
	#color3 = get_rand_color()
	colors = get_color_triad(background)
#	background = get_rand_color()

#	colors = [[255,0,0],[255,240,0],[0,0,255]]
#	background = [255,255,255]

	#image = (np.random.randint(256, size=(width, height))).tolist()
	image = np.zeros((height, width, dimension), dtype=np.int)
	for h in range(height):
		for w in range(width):
			image[h][w] = background

	for h in range(height):
		for w in range(width):
			# draw triangle
			funnyguy = random.randint(random.randint(5,20), random.randint(30,70))
			if w%funnyguy is 0 and h%funnyguy is 0:
				color = colors[funnyguy%3]
				base = funnyguy
				if funnyguy%4 < 3:
					for x in range(base):
						for y in range(base):
							if (x+y) > base:
								if y+h < height and ((base - x//2) + w - 1) < width:
									image[y+h][(x//2) + w] = color
									image[y+h][(base - x//2) + w - 1] = color
				else: 
					for x in range(base):
						for y in range(base):
							if y+h < height and x+w < width:
								image[y+h][x+w] = color


	image = image.tolist()
	filename = "triangles/test" + str((1 + i) * (random.randint(1,10000))) + ".png"
	png.from_array(image, 'RGB').save(filename)
	print(filename)
	#tweet_image(filename)
	#sleep(30)

"""

255, 0, 0
255, 255, 0

0, 0 = 100% of c1 0% of c2
5, 5 = 50/50
5, 10 = 50/50
10, 0 = 0% of c2 100% of c1


00000100000
00001110000
00011111000
00111111100
01111111110
11111111111


base = 5

w = 0, h = 0
x = 4 h = 4

0,2
1,1
1,2
1,3
2,0
2,



"""



