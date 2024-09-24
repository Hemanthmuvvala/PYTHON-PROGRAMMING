f=open('textfile.txt','w')
f.write('hi hello This is write operator\n')
l=['My name is\n','Hemanth\n','I am a student\n']
f.writelines(l)
with open('textfile.txt','a') as f:
	f.write('Iam  an engineer\n')
f=open('textfile.txt','r')
print(f.read())
f.close()
