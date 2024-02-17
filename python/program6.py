s=input("enter the string ")
for i in s:
    print(i)
a=int(input("enter the ending index number:"))
print(s[:a])
b=int(input("enter the starting index number:"))
print(s[b:])
print("____membership oprations____\n")
print("....not in opretion....\n")
s1=input("enter the latters:\n")
#s2=s1 in s

if s1 in s:
    
    print("given latter is find\n")
else:
    print("given lattr is not find\n")
print("....not in opretion....\n")
    
c=input("enter the latters:\n")

if c not in s:
    print("given latter is not find")
else:
    print("given latter is find")

            
