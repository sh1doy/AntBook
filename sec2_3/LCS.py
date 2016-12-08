n=int(input())

l=[]

for i in range(n):
	a=list(input())
	b=list(input())
	dp=[[0 for i in range(len(b))] for j in range(len(a))]

	if a[0]==b[0]:
		dp[0][0]=1
	for i in range(1,len(a)):
		if a[i]==b[0]:
			dp[i][0]=1
		else:
			dp[i][0]=dp[i-1][0]
	for i in range(1,len(b)):
		if a[0]==b[i]:
			dp[0][i]=1
		else:
			dp[0][i]=dp[0][i-1]
	for i in range(1, len(a)):
		for j in range(1, len(b)):
			if a[i]==b[j]:
				dp[i][j]=dp[i-1][j-1]+1
			else:
				dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

	l.append(dp[len(a)-1][len(b)-1])

for i in l:
	print(i)