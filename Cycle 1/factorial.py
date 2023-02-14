n=a=int(input("Enter the number:"))

f=1
'''for i in range(1,a+1):
    f*=i
print("Factorial of ",a,":",f)'''
while(a>0):
    f*=a
    a-=1
print("Factorial of ",n,":",f)