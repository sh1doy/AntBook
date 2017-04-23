# TSP

inf = float("inf")

n = 5
A = [
[inf,3,inf,4,inf],
[inf,inf,5,inf,inf],
[4,inf,inf,5,inf],
[inf,inf,inf,inf,3],
[7,6,inf,inf,inf]
]

def solve(n, A):

	dp = [[inf for i in range(n)] for j in range(1<<n)]
	dp[-1] = [0 for i in range(n)]

	def foo(visited, now):
		
		if dp[visited][now] != inf:
			return(dp[visited][now])
		minimum = inf
		for i,x in [(1<<x,x) for x in range(n)]:
			if visited & i == 0:
				minimum = min(minimum, foo(visited | i, x) + A[x][now])
		dp[visited][now] = minimum

		return(dp[visited][now])

	return(foo(0, 0))

print(solve(n, A))