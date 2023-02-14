d1={}
n=int(input("Enter No of Elements in Dictionary : "))
for i in range(n):
	key=input("\nEnter the Key : ")
	value=input("Enter the Value : ")
	d1[key]=value
print(f"Dict:{d1}")
a_dict=sorted(d1.items(),reverse=0)
d_dict=sorted(d1.items(),reverse=1)

print("\nAscending Order : ",dict(a_dict))
print("\nDescending Order : ",dict(d_dict))
a_dict=sorted(d1.items(),key=lambda item:item[1],reverse=0)
d_dict=sorted(d1.items(),key=lambda item:item[1],reverse=1)
print("\nSort by Value:\nAscending Order : ",dict(a_dict))
print("\nDescending Order : ",dict(d_dict))