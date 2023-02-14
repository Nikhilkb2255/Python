a=input("Enter a string:")
print(f"String before replace:{a}")
al=list(a)
for i in range(1,len(a)):
	if al[i]==al[0]:
		al[i]='$'
a=""
a=a.join(al)
print(f"String after replace:{a}")