def sum(l):
	sum=0
	for i in l:
		sum+=i
	print(f"List={l}\nSum={sum}")
list=[int(x) for x in input("Enter the list of numbers:").split(" ")]
sum(list)