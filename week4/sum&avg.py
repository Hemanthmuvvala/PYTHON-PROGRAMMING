l=[]
n=int(input("enter  the no.of elements"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
avg=(sum(l))/len(l)
print("the average of the list:",avg)
