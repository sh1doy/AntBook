# K-th number

n = 7
m = 3
a = [1,5,2,6,3,7,4]
q = [[2,5,3],[4,4,1],[1,7,3]]

import math
from bisect import bisect_left , bisect_right

rn = int(math.sqrt(n))+1
while len(a) != rn*rn:
	a.append(0)

b = []
for i in range(rn):
	t = []
	for j in range(rn):
		t.append(a[i*rn+j])
	b.append(t)
for i in range(len(b)):
	b[i].sort()

nmax = 10**9
nmin = -(10**9)

def foo(i,j,k):
	bi = i//rn
	bj = j//rn
	
	def bar_right(x):
		s1 = 0
		s1 += sum([l for l in a[i:rn*bi] if l<=x])
		s1 += sum([l for l in a[j:rn*bj] if l<=x])
		for l in range(bi,bj):
			s1 += bisect_right(b[l], x)
		return(s1)

	def bar_left(x):
		s1 = 0
		s1 += sum([l for l in a[i:rn*bi] if l<x])
		s1 += sum([l for l in a[rn*bj:j] if l<x])
		for l in range(bi,bj):
			s1 += bisect_left(b[l], x)
		return(s1)

	left = nmin
	right = nmax+1
	mid = (left+right)//2
	while right-left>1:
		if bar_left(mid) < k:
			left = mid
			if bar_right(mid) >= k:
				break
		else:
			right = mid
		mid = (left+right)//2
	return(mid)


for i in q:
	print(foo(*i))







