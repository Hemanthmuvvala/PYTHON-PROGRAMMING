#reversing a list in python
l=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
x=int(input("enter the element to remove: "))
l.remove(x)
print(l)
