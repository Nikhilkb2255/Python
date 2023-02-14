dict1={}
dict2={}
dict3={}
n=int(input("Enter number of items in the dictionary 1:"))
for i in range(n):
	key=input("Enter key:")
	value=input("Enter value:")
	dict1[key]=value
n2=int(input("Enter number of items in the dictionary 2:"))
for i in range(n2):
	key=input("Enter key:")
	value=input("Enter value:")
	dict2[key]=value
print("1st dictionary:",dict1)
print("2nd dictionary:",dict2)
dict3={**dict1,**dict2}
for k,v in dict3.items():
	if k in dict1 and k in dict2:
		dict3[k]=[v,dict1[k]]
print("Dict1+ict2=",dict3)