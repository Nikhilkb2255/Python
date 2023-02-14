def createlist(a,b):
	l=[]
	s=[x*x for x in range(32,100)]
	for i in range(a+1,b):
		if isdigiteven(i)==1 and i in s:
			l.append(i)
			
	print(f"List of four digit numbers from {a} to {b} with all their digits even and the number is a perfect square:{l}")		
			
def isdigiteven(n):
	while(n>0):
		d=n%10
		if(d%2!=0):
			return 0
		n=int(n/10)
	return 1
	
a=int(input("Enter the range:\n\tLowerbound:"))
b=int(input("\tUpperbound:"))
createlist(a,b)