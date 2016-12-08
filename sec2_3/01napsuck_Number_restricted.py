from pprint import pprint

n_max=100
a_max=100000
m_max=100000
K_max=100000

n=3 
a=[3,5,8]
m=[3,2,2]
K=19

dp=[[-1 for x in range(K + 1)] for y in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
	for j in range(K+1):
		if dp[i-1][j]>=0:
			dp[i][j]=m[i-1]
		elif j<a[i-1] or dp[i][j-a[i-1]]<=0:
			dp[i][j]=-1
		else:
			dp[i][j]=dp[i][j-a[i-1]]-1

# pprint(dp)
print(dp[n][K])

