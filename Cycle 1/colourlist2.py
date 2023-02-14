color1=[x for x in input("Enter list-1:").split(" ")]
color2=[x for x in input("Enter list-2:").split(" ")]
print([x for x in color1 if x not in color2])