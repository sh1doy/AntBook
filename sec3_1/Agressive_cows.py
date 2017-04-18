# Agressive_cows

N=5
M=3
x=[1,2,8,4,9]
x.sort()

def solve(N,M,x):
	def check(d):
		now=x[0]
		c=1
		for i in x:
			if i-now>=d:
				c+=1
				now=i
		if c>=M:
			return(True)
		else:
			return(False)

	left=0
	right=x[-1]
	center=int((left+right)/2)
	while right-left>1:
		if check(center):
			left=center
		else:
			right=center
		center=int((left+right)/2)
	return(int(left))


print(solve(N,M,x))