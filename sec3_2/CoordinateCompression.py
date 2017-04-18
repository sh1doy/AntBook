# Coordinate Compression
import sys

w = 1000000
h = 1000000
n = 300
from random import randint
x1 = [randint(1,1000000) for i in range(n)]
x2 = x1[:n//2]+[randint(1,1000000) for i in range(n//2)]
y1 = [randint(1,1000000) for i in range(n)]
y2 = [randint(1,1000000) for i in range(n//2)]+y1[n//2:]

def lake_counting(field):
	field_x_length = len(field)
	field_y_length = len(field[0])
	lake_count = 0
	from queue import Queue
	q = Queue()
	def dfs(x,y):
		if field[x][y] != 0:
			return(None)
		field[x][y] = 1
		for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
			nx = x + dx
			ny = y + dy
			if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 0):
				q.put((nx,ny))
	for i in range (0, field_x_length):
		for j in range (0, field_y_length):
			if (field[i][j] == 0):
				while not q.empty():
					dfs(*q.get())
				lake_count+=1
	return(lake_count)

def solve(w,h,n,x1,x2,y1,y2):
	def neighbor(l):
		res = []
		for i in l:
			if i-1>0:
				res.append(i-1)
			res.append(i)
			if i+1<w:
				res.append(i+1)
		return(res)
	compx = list(set([1]+neighbor(x1)+neighbor(x2)+[w]))
	compy = list(set([1]+neighbor(y1)+neighbor(y2)+[w]))
	compx.sort()
	compy.sort()
	unzipx = {i:x for i,x in enumerate(compx)}
	unzipy = {i:x for i,x in enumerate(compy)}
	zipx = {x:i for i,x in enumerate(compx)}
	zipy = {x:i for i,x in enumerate(compy)}

	table = [[0 for i in range(len(zipx))] for j in range(len(zipy))]

	for Y1,X1,Y2,X2 in zip([zipy[i] for i in y1],[zipx[i] for i in x1],[zipy[i] for i in y2],[zipx[i] for i in x2]):
		Y1,Y2 = sorted([Y1,Y2])
		X1,X2 = sorted([X1,X2])
		for i in range(Y1,Y2+1):
			for j in range(X1,X2+1):
				table[i][j] = 1

	# for i in table:
	# 	print("".join(map(str,i)))
	return(lake_counting(table))



print(solve(w,h,n,x1,x2,y1,y2))
