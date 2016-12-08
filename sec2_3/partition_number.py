n = 999
m = 999

# nをm個 [以 下] に分割するのは何通りあるか
def partition_number(n,m):
	dp = [[0 for x in range(m+1)] for x in range(n+1)]
	dp[0][0]=1
	for i in range(0,n+1):
		for j in range(1,m+1):
			if i-j>=0:
				dp[i][j]=dp[i][j-1]+dp[i-j][j]
			else:
				dp[i][j]=dp[i][j-1]

	return(dp[n][m])

print(partition_number(n,m)%10000)