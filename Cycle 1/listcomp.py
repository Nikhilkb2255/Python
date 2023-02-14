a=[int(x) for x in input("Enter elements:").split(" ")]
b=input("Enter a word:")
c=[x for x in a if x>0 ]
print("List:",a)
print("1.Positive integer list:",c)
c=[x*x for x in a]
print("2.Square list:",c)
c=[i for i in b if(i in ['a','e','i','o','u','A','E','I','O','U'])]
print(f"3.Vowels in string \"{b}\":{c}")
c=[ord(i) for i in b]
print(f"4.Ordinal of \"{b}\":",c)