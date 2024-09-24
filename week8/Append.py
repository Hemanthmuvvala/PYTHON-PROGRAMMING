f=open('textfile.txt','w')
f.write('hi hello This is write operator\n')
l=['My name is\n','Hemanth\n','I am a student\n']
f.writelines(l)
f=open('textfile.txt','r')
print(f.read())
print(f.readline())
print(f.readlines())
with open('textfile.txt','a') as f:
	f.write('He is an engineer\n')
print(f.read())
f.close()
