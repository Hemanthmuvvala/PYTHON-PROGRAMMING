#to check whether the number is prime or not
f=0
p=int(input("enter the number to check:"))
for i in range(1,p+1):
	if(p%i==0):
		f=f+1
if(f==2):
	print("it is a prime number")
elif (f==1):
	print("it is neither prime nor composite")
else:
	print("it is not a prime number")
