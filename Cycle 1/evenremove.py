list=[int(x) for x in input("Enter number list:").split(" ")]
list=[x for x in list if x%2!=0]
print(list)