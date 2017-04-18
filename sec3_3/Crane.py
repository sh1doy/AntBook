#Crane
from math import cos,sin,pi
N = 3
C = 2
L = [5,5,5]
S = [1,2]
A = [270,90]

def solve(N,C,L,S,A):
	i = 1
	while i < N:
		i <<= 1
	class node(object):
		def __init__(self,y):
			self.x = 0
			self.y = y
			self.a = 0
		def __repr__(self):
			return(str([self.x, self.y, self.a]))

	array = [node(0) for i in range(i<<1)]
	for i in range(N):
		array[len(array)//2+i].y = L[i]

	def make(i):
		if i >= len(array)//2:
			return(array[i].y)
		else:
			array[i].y = make(i*2) + make(i*2+1)
			return(array[i].y)
	
	make(1)

	def do(s,a,i,l,r):
		if r-l<=1:
			return()
		m = (l+r)//2
		if s <= m:
			array[i].a += (a/360)*2*pi
			do(s,a,i*2,l,m)
			# do(s,a,i*2+1,m,r)
			array[i].x = array[i*2].x + array[i*2+1].x*cos(array[i].a) + array[i*2+1].y*sin(array[i].a)
			array[i].y = array[i*2].y + array[i*2+1].y*cos(array[i].a) - array[i*2+1].x*sin(array[i].a)
		else:
			do(s,a,i*2+1,m,r)

	for s,a in zip(S,A):
		do(s,a,1,0,len(array)//2)
		print((array[1].x,array[1].y))


print(solve(N,C,L,S,A))
