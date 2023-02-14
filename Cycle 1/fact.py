def fact(n):
	f=1
	while(n>0):
		f*=n
		n-=1
	return f
n=int(input("Enter a number:"))
f=fact(n)
print(f"Factorial of {n}={f}")