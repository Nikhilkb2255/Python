def stringend(str):
	if(str[-3:]=="ing"):
		str=str+"ly"
	else:
		str=str+"ing"
	print("String after update:",str)

str=input("Enter a string:")
print("String:",str)
stringend(str)