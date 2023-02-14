str=input("Enter a string:")
d={}
for i in str:
	d[i]=str.count(i)
print("String:",str)
for i in d:
	print(f"Number of {i}:{d[i]}")