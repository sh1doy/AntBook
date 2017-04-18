#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
print(sys.version_info)


s=\
"#S######.#\n"+\
"......#..#\n"+\
".#.##.##.#\n"+\
".#........\n"+\
"##.#####.#\n"+\
"....#....#\n"+\
"###.####.#\n"+\
"..........\n"+\
".###.####.\n"+\
"........G#\n"

aa=[list(x) for x in s.split()]

class Mass(object):
	"""docstring for Mass"""
	def __init__(self):
		self.cond=False
		self.dis=0
		self.goal=False

l=[[Mass() for j in range(len(aa[0]))] for i in range(len(aa))]

start=[0,0]
for i in range(len(aa)):
	for j in range(len(aa[0])):
		if aa[i][j]=="S":
			start=[i,j]
		elif aa[i][j]=="G":
			l[i][j].goal=True

queue=[]
def search(start,dis):
	now=l[start[0]][start[1]]
	now.dis=dis+1
	now.cond=True
	if now.goal ==True:
		g=now.dis
		print(now.dis-1)
	a=start[0]
	b=start[1]
	for x in [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]:
		i=x[0]
		j=x[1]
		if 0<=i and i<len(l):
			if 0<=j and j<len(l[0]):
				if l[i][j].cond==False and aa[i][j]!="#":
					queue.insert(0,[[i,j],now.dis])

queue.insert(0,[start,0])

while len(queue)!=0:
	a=queue.pop()
	search(a[0],a[1])
