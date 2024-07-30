#to print patterns using nested loops
n=int(input("enter a number:"))
c=65
for i in range(1,n+1):
	for j in range(1,i+1):
	print(chr(c),end=" ")	
	print("")
	c+=1
	
