f=open('textfile.txt','w')
f.write('hi hello This is write operator\n')
l=['My name is\n','Hemanth\n','I am a student\n']
f.writelines(l)
with open('textfile.txt','a') as f:
	f.write('Iam  an engineer\n')
f=open('textfile.txt','r')
print(f.read())
print("This is cursor position=",f.tell())
print("The position has became zero=",f.seek(0))
print(f.tell())
f.close()
'''output
hi hello This is write operator
My name is
Hemanth
I am a student
Iam  an engineer
This is cursor position= 83
The position has became zero= 0
0
'''
