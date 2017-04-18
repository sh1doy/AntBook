# 4ValuesWhoSumIs0
from bisect import bisect_left


# n=6
# A=[-45,-41,-36,-36,26,-32]
# B=[22,-27,53,30,-38,-54]
# C=[42,56,-37,-75,-10,-6]
# D=[-16,30,77,-46,62,45]

from random import randint
n = 400
A = [randint(-2**28,2**28) for i in range(n)]
B = [randint(-2**28,2**28) for i in range(n)]
C = [randint(-2**28,2**28) for i in range(n)]
D = [randint(-2**28,2**28) for i in range(n)]

def solve(n,A,B,C,D):
	AB = [x+y for x in A for y in B]
	CD = [x+y for x in C for y in D]
	CD.sort()
	c = 0
	for i in AB:
		p = bisect_left(CD,-i)
		if p<n**2 and CD[p]+i==0:
			c+=1

	return(c)

	

print(solve(n,A,B,C,D))
