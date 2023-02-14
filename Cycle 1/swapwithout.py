'''a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
print("Before swapping\n a:",a,"\n b:",b)
a+=b
b=a-b
a-=b
print("After swapping\n a:",a,"\n b:",b)'''

c=int(input("Enter number1:"))
d=int(input("Enter number2:"))
print("Before swapping\n a:",c,"\n b:",d)
c,d=d,c
print("After swapping\n a:",c,"\n b:",d)