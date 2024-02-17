import math as m
print("1 circle")
print("2 taingle")
print("3 squre")
print("4 ractangle")
a=int(input("enter the options"))
if a==1:
    rad=float(input("radius"))
    r=m.pi*rad*rad
    print(r)
if a==2:
    b=int(input("enter base"))
    h=int(input("enter height"))
    r=1/2*b*h
    print(r)
if a==3:
    area=int(input("length of a side"))
    r=area*area
    print(r)
if a==4:
    l=int(input("length"))
    w=int(input("width"))
    print(l*w)

else:
    print("enter the vaild number")
        
    
