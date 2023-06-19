#WAP to find out greatest number out of 3 no

a=float(input("Enter Number 1= "))
b=float(input("Enter Number 2= "))
c=float(input("Enter Number 3= "))

if (a>b and a>c):
    print(a," is greatest")
elif(b>a and b>c):
    print(b, " is greatest")
else:
    print(c, " is greatest")    