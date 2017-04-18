# subseqence

n=10
S=15
a=[5,1,3,5,10,7,4,9,2,8]

def solve(n,S,a):
	suml = a
	for i in range(1,len(a)):
		suml[i]=suml[i-1]+suml[i]
	
	left=0
	right=0
	minlen=float("inf")

	while right<len(a):
		if suml[right]-suml[left]>=S:
			minlen=min(minlen,right-left)
			left+=1
		else:
			right+=1

	return(minlen)


print(solve(n,S,a))
