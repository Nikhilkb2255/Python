def fib(n):
	a=1
	b=0
	c=a+b
	count=1
	while(count<=n):
		print(b,end="\t")
		count+=1
		a=b
		b=c
		c=a+b
	
n=int(input("Enter a number:"))
print("Fibonacci series:",end=" ")
fib(n)