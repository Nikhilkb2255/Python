line=input("Enter the line:")
words=line.split(" ")
d={}
for i in words:
	d[i]=words.count(i)
print(f"Occurance of words in line \'{line}\' : {d}")