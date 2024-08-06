#reversing a list in python
l=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
t=l[0]
l[0]=l[n-1]
l[n-1]=t
print(l)
