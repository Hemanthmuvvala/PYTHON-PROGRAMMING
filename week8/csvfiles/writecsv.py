import csv
l=[
['s.no','Name','Rollno'],[1,100,'Hemanth'],[2,200,'puneetth'],[3,300,'Lokesh']
]
with open('Table.csv','w',newline='') as file:
	f=csv.writer(file)
	f.writerows(l)
