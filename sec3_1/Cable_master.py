# cable_master

# import random
# N=4
# K=10000
# L=[random.random()*100000 for i in range(10000)]

N=4
K=11
L=[8.02,7.43,4.57,5.39]

def solve(N,K,L):
	def check(x):
		if sum([int(i/x) for i in L])>=K:
			return(True)
		else:
			return(False)
	left=0
	right=max(L)
	center=((right+left)/2)
	for i in range(500):
		if not check(center):
			right=center
		else:
			left=center
		center=((right+left)/2)

	center*=100
	center=list(str(int(center)))
	center.insert(-2,".")
	return("".join(center))


print(solve(N,K,L))