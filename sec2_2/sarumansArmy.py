
N=6
R=10
X=[1,7,15,20,30,50]

X.sort()

def solve(r,x):
	for i in range(len(x)):
		if x[i]>r+x[0]:
			return(1+solve(r,[a-x[i] for a in x[i:] if a-x[i]>r]))
	return(1)

print(solve(R,X))