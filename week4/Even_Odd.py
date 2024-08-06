#reversing a list in python
l=[]
even=[]
odd=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
for i in range(n):
	if(l[i]%2==0):
		even.append(l[i])
	else:
		odd.append(l[i])

print("The even number list:"even)
print("The odd number list:"odd)
