#to reverse number
n=int(input("enter a number:"))
t=n
sum=0
while n>0:
	rem=n%10
	sum=sum*10+rem
	n=n//10
if(sum!=t):
	print("It is   not a palindrome")
else:
	print("it is  a palindrome")
