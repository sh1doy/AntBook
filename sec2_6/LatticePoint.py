#Lattice point

x1=54364132
y1=46234
x2=234421
y2=-2354213

X=abs(x1-x2)
Y=abs(y1-y2)

def gcd(A, B):
	if B==0: return(A)
	else: return(gcd(B, A%B))


print(max(gcd(X,Y)-1,0))