# Minimum_Scalar_Product
import random
n = 800
v1=[random.randint(-100000,100000) for i in range(n)]
v2=[random.randint(-100000,100000) for i in range(n)]

def solve(v1,v2):
	v1.sort()
	v2.sort(reverse=True)
	return(sum([v1[a]*v2[a] for a in range(len(v1))]))

print(solve(v1, v2))