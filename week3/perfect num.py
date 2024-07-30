#to print perfect number ot not
n=int(input("ENTER A NUMBER:"))
sum=0
for i in range(1,n):
	if n%i==0:
		sum=sum+i
if(sum==n):
	print("IT IS A PERFECT NUMBER")
else:
	print("IT IS NOT A PERFECT NUMBER")
