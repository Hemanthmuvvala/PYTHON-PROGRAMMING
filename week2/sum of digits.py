#to find the sum of the digits of a given number
n=int(input("enter a number:"))
sum=0
while n>0:
	rem=n%10
	sum=sum+rem
	n=n//10
print("the sumof the digits= ",sum)
