#WAP to check whether the given no is positive or negative

a=int(input(" Enter the Number to check whether Negative or positive: "))
if(a>0):
    print(a," is Positive")
elif(a==0):
    print(a, " is Zero")
else:
    print(a, " is Negative")