# lower_bound

n=5
a=list(range(10**7))
k=534400

def lower_bound(n,a,k):
	left=0
	right=len(a)-1
	if k>a[-1]:
		return(len(a))
	center=int((right+left)/2)
	while right-left>1:
		print(left,center,right)
		if a[center]<k:
			left=center
		else:
			right=center
		center=int((right+left)/2)
	return(right)


print(lower_bound(n,a,k))