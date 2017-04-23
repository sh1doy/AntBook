# Domino

n = 3
m = 3

color = [
	[0,0,0],
	[0,1,0],
	[0,0,0]
]

def solve(n, m, color):
	dp = [[[0 for i in range(1<<m)] for j in range(m)] for k in range(n)]
	dp[0][0][0] = 1

	for i in range(n):
		for j in range(m):
			for k in range(1<<m):
				if k&(1<<j) or color[i][j] == 1:
					nex = k&~(1<<j)
					if j+1<m:
						dp[i][j+1][nex] += dp[i][j][k]
					elif i+1<n:
						dp[i+1][0][nex] += dp[i][j][k]
				else:
					# 横
					if j !=	m-1 and color[i][j+1]==0 and not(k&(1<<(j+1))):
						nex = k|(1<<(j+1))
						dp[i][j+1][nex] += dp[i][j][k]
					# 縦
					if i+1<n and color[i+1][j]==0:
						nex = k|(1<<j)
						if j+1<m:
							dp[i][j+1][nex] += dp[i][j][k]
						else:
							dp[i+1][0][nex] += dp[i][j][k]


	return(dp[n-1][m-1][1<<m-1]) # 最後は境界が001となっていればよい

print(solve(n,m,color))


	