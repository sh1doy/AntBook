import numpy

n=9
s=[1,2,2,6,6,4,3,5,7]
t=[3,4,4,8,8,6,5,7,9]

def solve(s,t):
	time=0
	c=0
	while(s!=[]):
		f=numpy.argmin(t)
		if time<s[f]:
			time=t[f]
			s.pop(f)
			t.pop(f)
			c+=1
		else:
			s.pop(f)
			t.pop(f)
	return(c)

print(solve(s,t))