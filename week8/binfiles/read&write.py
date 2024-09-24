f=open('binaryfile.bin','wb')
f.write(b'\x00\x01\x02\x03\x04\x05')
f=open('binaryfile.bin','rb')
print(f.read())
'''output
b'\x00\x01\x02\x03\x04\x05'
Ā̂Ԅ
'''
