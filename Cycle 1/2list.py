a=[]
b=[]
astr=input("Enter the elements of list1:")
astr=astr.split(" ")
a=list(map(int,astr))
n=len(a)
s1=sum(a)
bstr=input("Enter the elements of list2:")
bstr=bstr.split(" ")
b=list(map(int,bstr))
m=len(b)
s2=sum(b)
c=[]
for i in a:
    if i in b:
        c.append(i)
if(m==n):
    print("Both list have same length")
else: 
    print("Both list have different length")
#print("S1=",s1,"S2=",s2)
if(s1==s2):
    print("Sum of elements in both list are same")
else:
    print("Sum of elements in both list are different")
if(len(c)==0):
    print("No common elements")
else:
    print("Common elements:",c)