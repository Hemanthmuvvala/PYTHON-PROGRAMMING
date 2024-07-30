#to print fibonacci sequence
n=int(input("ENTER A NUMBER:"))
n1,n2=0,1
while n>0:
	print(n1,end=" ")
	n3=n1+n2
	n1=n2
	n2=n3
	n-=1
