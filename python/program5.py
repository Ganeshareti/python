
print("1 coverting the string upper case")
print("2 coverting the string lower case")
print("3 exist")
while True:
    b=int(input("enter the options:"))
    
    if b==1:
          a=input("enter the string:")
          print(a.upper())
    elif b==2:
        a=input("enter the string:")
        print(a.lower())
    else:
        break;
