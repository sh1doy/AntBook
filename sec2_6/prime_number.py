# prime_number?

n=12940230

from math import sqrt
from random import randint

def isprime(num): # O(sqrt(n))
	root=int(sqrt(n))
	for i in range(2,root+1):
		if num%i==0:
			return(False)
	return(True)

def isprime_(num, n=1): # O(k+n)未満 (ミラー・ラビンテスト)
	q = num
	if q == 2:
		return(True)
	if q ==1 or q&1 == 0:
		return(False)
	d = (q-1)>>1
	while d&1 == 0:
		d >>= 1
	for i in range(n):
		a = randint(1,q-1)
		t = d
		y = pow(a,t,q)
		while t != q-1 and y != 1 and y != q-1: 
			y = pow(y,2,q)
			t <<= 1
		if y != q-1 and t&1 == 0:
			return(False)
	return(True)

def dividers(num, sort=True):
	root=int(sqrt(n))
	l=[]
	m=[]
	for i in range(1,root+1):
		if num%i==0:
			l.append(i)
			if i<root:
				m.append(int(num/i))
	if sort:
		l.extend(sorted(m))
		return(l)
	else:
		l.extend(m)
		return(l)

def decomposit(num):
	root=int(sqrt(n))
	l=[]
	i=2
	while i<root+1:
		if num%i==0:
			j=0
			while(num%i==0):
				j+=1
				num=num/i
			l.append([i,j])
			root=int(sqrt(n))
		i+=1
	if num!=1:
		l.append([int(num),1])
	return(l)

print(isprime(n))
print(decomposit(n))
print(dividers(n))



