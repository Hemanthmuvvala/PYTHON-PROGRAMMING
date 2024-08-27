def Reverse(l):
	s=0
	e=n-1
	while s<=e:
		l[s],l[e]=l[e],l[s]
		s+=1
		e-=1
	return l
	
		
l=[]
n=int(input("enter  the no.of elements:"))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
print(Reverse(l))
