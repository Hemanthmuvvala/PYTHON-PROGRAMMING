#to find the factorial of a given number
f=1

n=int(input("enter the number:"))

for i in range(1,n+1) :
	f=f*i
print("the factorial of the given number=",f)
