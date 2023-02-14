s1=input("Enter string1:")
s2=input("Enter string2:")
s1=s1.replace(s1[0],s2[0])+" "+s2.replace(s2[0],s1[0])
print(s1)