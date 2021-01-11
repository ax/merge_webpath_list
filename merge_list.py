#!/usr/bin/python3
import os
path = './lists/'
content = []
for filename in os.listdir(path):
	with open(path+filename) as fp:
		content = content + [l.strip() for l in fp.readlines()] 
for l in set(content):
	print(l)
