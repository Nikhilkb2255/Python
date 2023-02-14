n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
i=1
while(i<=n1 and i<=n2):
	if(n1%i==0 and n2%i==0):
		gcd=i
	i+=1
print(f"GCD({n1},{n2})={gcd}")