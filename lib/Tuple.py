#TUPLES
#concatenation of two tuples.
T1=(1,2,3,4,5,3,3,3)
T2=(6,7,8,9,10)
print(T1+T2)
#repetition of the tuples
print((T1+T2)*3)
#accesing the tuple values using index
print(T1[4])
print(1 in T1)
for i in T2:
	print(i)
#slicing in tuple
#split method,map method,join method.
print(T1)
print(T1[1])
print(T1[2:4])
print(T1[::-1])
print(T1[::-2])
print(T1[1:4:-1])
print(T1.index(3))
print(len(T1+T2))
print(T1.count(3))
#copying one tuple data to another tuple data using assingment operator.
T2=T1
print(T2)
t3=tuple(zip(T1,T2))
print(t3)

