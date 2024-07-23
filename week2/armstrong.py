#armstrong number or not
n=int(input("enter a number:"))
t=n
sum=0
while n>0:
	rem=n%10
	sum=sum+rem**3
	n=n//10
if(sum==t):
	print("It is  a armstrong number ")
else:
	print("it is  not a armstrong number")
