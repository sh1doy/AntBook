# Physics Experiment
from math import sqrt

N,H,R,T = 100000,10,10,10254524521

def solve(N,H,R,T):
	def calc(h,t):
		if t<0:
			return h
		period = sqrt(2*h/10)
		k = t//period
		if k%2==1:
			return(h-(1/2)*10*((k+1)*period-t)**2)
		else:
			return(h-(1/2)*10*(t-k*period)**2)

	res = [calc(H,T-i) for i in range(N)]
	res.sort()
	res = [res[i]+2*R*0.01 for i in range(N)]
	return(res)


print(solve(N,H,R,T))
