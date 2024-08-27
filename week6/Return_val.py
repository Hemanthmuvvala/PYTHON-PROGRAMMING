def Calculator(n):
	Total=sum(n)
	count=len(n)
	average=Total/count
	return Total,count,average
n=[10,20,30]
Total,count,average=Calculator(n)
print("Total:",Total)
print("Count:",count)
print("Average:",average)
