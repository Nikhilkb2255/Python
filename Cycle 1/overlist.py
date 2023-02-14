a=[int(i) for i in input("Enter number list:").split(" ")]
a=[x if x<100 else "over" for x in a]
print(f" List:{a}")