# Power
# python標準の方が若干はやい

n=65000

def power(x,n,mod):
	res=1
	i=x
	while(n):
		if n&1:
			res*=i
			res%=mod
		n>>=1
		i=(i*i%mod)
	return(res)

from math import sqrt
def isprime(num): # O(sqrt(n))
	root=int(sqrt(n))
	for i in range(2,root+1):
		if num%i==0:
			return(False)
	return(True)

def Carmichael(n):
	for i in range(n):
		if power(i,n,n)==i:
			return("No")
	if isprime(n):
		return("No")
	else:
		return("Yes")

print(Carmichael(n))