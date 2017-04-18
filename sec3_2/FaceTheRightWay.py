# Face The Right Way

N=8
a="BBBFBFFF"
a=list(a)

for i in range(N):
	if a[i]=="B":
		a[i]=1
	else:
		a[i]=0

def solve(N,a):
	k = N
	m = float("inf")
	for i in range(N):
		c=0
		f=[0 for x in range(N+1)]
		n=0
		for j in range(N-i):
			if (a[j]+n)%2==1:
				# print("Flip",j,"-",j+i)
				f[j+i]+=1
				n+=1
				c+=1
			if f[j]==1:
				n-=1
		flag = True
		for j in range(N-i,N):
			if (a[j]+n)%2==1:
				flag=False
				break
			if f[j]==1:
				n-=1
		if flag:
			# print("new!")
			if c<m:
				m=c
				k=i+1
		# print("next width",i+2)

	return(m, k)








print(solve(N,a))
