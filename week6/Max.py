def Max(l):
	m=l[0]
	for val in l[1:]:
		if val>m:
			m=val
	return m
		
l=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
print(Max(l))
