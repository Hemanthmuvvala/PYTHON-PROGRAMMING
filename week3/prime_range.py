#to check prime or not with in the interval
s=int(input("enter the starting number:"))
n=int(input("enter the ending number:"))

print("The prime numbers within the given range are:")
for i in range(s,n+1):
	f=0
	for j in range(1,i+1):
		if i%j==0:
			f+=1
	if f==2:
		print(i)
