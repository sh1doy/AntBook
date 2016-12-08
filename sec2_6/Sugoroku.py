#Sugoroku

a=24665436354
b=14545989929

def solve(a, b):
	l=[]
	while b!=0:
		l.append([a,b])
		tmp=a%b
		a=b
		b=tmp
	#gcd!=1 -> OUT
	if a!=1:
		return(-1)
	x=1
	y=0
	while l!=[]:
		a,b=l.pop()
		xp=x
		yp=y
		x=yp
		y=xp-(a//b)*yp
		# print("1 =",a,"*",x,"+",b,"*",y)
	return(" ".join([str(i) for i in [max(0,x),max(0,y),max(0,-x),max(0,-y)]]))


print(solve(a,b))