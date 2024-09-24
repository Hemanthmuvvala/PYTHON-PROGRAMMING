import csv
l=[
['s.no','Name','Rollno'],[1,100,'Hemanth'],[2,200,'puneetth'],[3,300,'Lokesh']
]
with open('Table.csv','w',newline='') as file:
	f=csv.writer(file)
	f.writerows(l)
f=open('Table.csv','r')
read=csv.reader(f)
for row in read:
        print(row)
'''output
['s.no', 'Name', 'Rollno']
['1', '100', 'Hemanth']
['2', '200', 'puneetth']
['3', '300', 'Lokesh']
'''
