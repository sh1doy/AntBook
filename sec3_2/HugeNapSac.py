# huge napsac
from bisect import bisect_left
from bisect import bisect_right

# n=4
# w=[2,1,3,2]
# v=[3,2,4,2]
# W=5

from random import randint
n=30
w=[randint(1,pow(10,15)) for i in range(n)]
v=[randint(1,pow(10,15)) for i in range(n)]
W=10**18

def solve(n,w,v,W):
	res = -1
	data = [(w[i],v[i]) for i in range(n)]
	kireme = n//2
	A = data[:kireme]
	B = data[kireme:]
	genA = [list(map(int,list(format(i,"0"+str(kireme)+"b")))) for i in range(pow(2,kireme))]
	genB = [list(map(int,list(format(i,"0"+str(n-kireme)+"b")))) for i in range(pow(2,n-kireme))]
	AA = [(sum([A[j][0]*genA[i][j] for j in range(kireme)]),sum([A[j][1]*genA[i][j] for j in range(kireme)])) for i in range(pow(2,kireme))]
	BB = [(sum([B[j][0]*genB[i][j] for j in range(n-kireme)]),sum([B[j][1]*genB[i][j] for j in range(n-kireme)])) for i in range(pow(2,n-kireme))]
	AA.sort()
	BB.sort()
	BBw = [x[0] for x in BB]
	BBv = [x[1] for x in BB]
	BBmaxv=BBv[:]
	for i in range(1,len(BBmaxv)):
		BBmaxv[i] = max(BBmaxv[i],BBmaxv[i-1])

	for aitem in AA:
		if aitem[0]<=W:
			hi = bisect_right(BBw,W-aitem[0])
			if hi-1>=0:
				t = BBmaxv[hi-1]
			else:
				t =0
			res = max(res,t+aitem[1])
	return(res)
	

print(solve(n,w,v,W))
