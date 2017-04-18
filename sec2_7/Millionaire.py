# Millionaire
# PythonではM=10ぐらいまでしかとおりませ〜ん

M=3
P=0.75
X=600000

def solve(M,P,X):
	X/=1000000
	n=pow(2,M)+1
	dp=[[0 for i in range(n)] for i in range(M+1)]
	dp[0][-1]=1 
	for i in range(1,M+1):
		for j in range(n):
			dp[i][j]=max([dp[i-1][j-k]*(1-P)+dp[i-1][j+k]*P for k in range(min(j,n-j-1)+1)])

	p=pow(1/2,M)
	return(dp[-1][int(X//p)])

print(solve(M, P, X))