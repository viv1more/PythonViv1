#WAP to find out greatest no. out of 5 numbers.

num1=int(input("Enter Number First : "))
num2=int(input("Enter Number Second : "))
num3=int(input("Enter Number Third : "))
num4=int(input("Enter Number Fourth : "))
num5=int(input("Enter Number Fifth  : "))

#if(num1>num2 and num1>num3 and num1>num4 and num1>num5):
 #   print(num1," is the Largest Number")
#elif(num2>num1 and num2>num3 and num2>num4 and num2>num5):
 #   print(num2," is the Largest Number")
#elif(num3>num2 and num3>num1 and num3>num4 and num3>num5):
 #   print(num3," is the Largest Number")
#elif(num4>num2 and num4>num3 and num4>num1 and num4>num5):
#    print(num4," is the Largest Number")
#else:
 #   print(num5," is the Largest Number")   
 #ORRRRRRRRRRRRRRRRRRRRR#

if(num1>num2):
    if(num1>num3):
        if(num1>num4):
            if(num1>num5):
                print(num1," is  Greatest")
            else:
                print(num5," is Greatest")
if(num2>num1):
    if(num2>num3):
        if(num2>num4):
            if(num2>num5):
                print(num2," is  Greatest")
            else:
                print(num5," is Greatest")
if(num3>num2):
    if(num3>num1):
        if(num3>num4):
            if(num3>num5):
                print(num3," is  Greatest")
            else:
                print(num5," is Greatest")
if(num4>num2):
    if(num4>num3):
        if(num4>num1):
            if(num4>num5):
                print(num4," is  Greatest")
            else:
                print(num5," is Greatest")
