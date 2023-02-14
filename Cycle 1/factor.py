def fact(n):
	for i in range(1,n+1):
		if(n%i==0):
			print(i,end="\t")
	print()
n=int(input("Enter a number:"))
print(f"factor of {n}:",end="\t")
fact(n)