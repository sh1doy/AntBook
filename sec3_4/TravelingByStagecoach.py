# TravelingByStagecoach

n = 2
m = 4
a = 2
b = 1
t = [3,1]

inf = float("inf")

A = [
[inf,inf,3,2],
[inf,inf,3,5],
[3,3,inf,inf],
[2,5,inf,inf]
]

def solve(n, m, a, b, tickets, A):
	
	dp = [[-1 for i in range(m)] for j in range(1<<n)]
	dp[-1] = [inf for i in range(m)]
	dp[-1][a] = 0

	def foo(tic, now):
		if dp[tic][now] != -1:
			return(dp[tic][now])
		minimum = inf
		for t,j in [(1<<t,t) for t in range(n)]:
			if tic & t == 0:
				for i in range(m):
					minimum = min(minimum, foo(tic|t, i)+A[i][now]/tickets[j])
		dp[tic][now] = minimum

		return(minimum)

	foo(0, b)

	return(min([dp[i][b] for i in range(1<<n)]))



print(solve(n, m, a-1, b-1, t, A))