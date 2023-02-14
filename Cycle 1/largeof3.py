a=int(input("Enter 3 number:"))
b=int(input())
c=int(input())
print("Numbers:",a,b,c)
if(a>b):
	if(a>c):
		print(f"{a} is biggest")
	else:
		print(f"{c} is biggest")
else:
	if(b>c):
		print(f"{b} is biggest")
	else:
		print(f"{c} is biggest")