dict1={'a':1,'b':2}
dict2={'a':3,'b':4}
'''n=int(input("Enter the number of items for the dict1:"))
for i in range(n):
	key=input("Enter key:")
	val=input("enter value:")
	dict1[key]=val
m=int(input("Enter the number of items for the dict2:"))
for i in range(m):
	key=input("Enter key:")
	val=input("enter value:")
	dict2[key]=val'''
print(f'dict1={dict1}')
print(f'dict2={dict2}')

#dict1.update(dict2)
d3={**dict1,**dict2}
print(f"After update dict3={d3}")
for k,v in d3.items():
	if k in (dict1 and dict2):
		d3[k]=[v,dict1[k]]
print(f"After update dict3={d3}")