#reversing a list in python
l=[]
even=[]
odd=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
print("The max element in list pos:",l.index(max(l)))
print("The min element in list pos:",l.index(min(l)))
