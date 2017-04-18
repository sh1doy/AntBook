# Maximize avarage

n=3
k=2
wv=[[2,2],[5,3],[2,1]]

def solve(n,k,wv):
	def check(x):
		wv.sort(key=lambda y: (y[1]-y[0]*x),reverse=True)#降順にしないとだめ
		if sum([i[1] for i in wv[:k]])>=x:
			return(True)
		else:
			return(False)

	left=0
	right=sum([i[1] for i in wv])
	center=(left+right)/2
	for i in range(200):
		if check(center):
			left=center
		else:
			right=center
		center=(left+right)/2

	we=sum([i[0] for i in wv[:k]])
	center/=we
	
	return("{:.02}".format(center))

print(solve(n,k,wv))