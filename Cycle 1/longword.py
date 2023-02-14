def longestlen(l1):
	l=0
	for i in list1:
		if len(i)>l:
			l=len(i)
			w=i
	return [l,w]
list1=[i for i in input("Enter list of words:").split(" ")]
out=longestlen(list1)
print(f"length of longest word \"{out[1]}\":{out[0]}")