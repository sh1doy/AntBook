# Bribe_the_Prisoners

P=20
Q=3
A=[3,6,14]

def solve(P,Q,A):
	dp=[[0 for i in range(Q+2)]	for i in range(Q+2)] #dp[i][j]i~j人目までを開放するコスト
	A.insert(0,0)
	A.append(P+1)
	for j in range(1,Q+2):
		for i in range(j-1)[::-1]:
			dp[i][j]=min([dp[i][k]+dp[k][j] for k in range(i+1,j)])+A[j]-A[i]-2
	return(dp[0][Q+1])



print(solve(P,Q,A))