a=input("Enter a string:")
print(f"String:{a}")
al=list(a)
al[0],al[-1]=al[-1],al[0]
a=""
a=a.join(al)
print(f"String after replace:{a}")	