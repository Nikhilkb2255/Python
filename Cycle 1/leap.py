n=int(input("Enter the year:"))
print(f"Leap years from 2022 to {n}:",end='\t')
for i in range(2022,n):
	if(i%100==0 and i%400==0):
		print(i,end='\t')
	if(i%4==0 and i%100!=0):
		print(i,end='\t')