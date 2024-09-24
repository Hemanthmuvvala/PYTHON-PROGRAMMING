#In this program the basic operations for the files like read,readline,read lines,write,writelines are written below
f=open('textfile.txt','w')
f.write('hi hello This is write operator\n')
l=['My name is\n','Hemanth\n','I am a student\n']
f.writelines(l)
f=open('textfile.txt','r')
print(f.read())
print(f.readline())
print(f.readlines())
