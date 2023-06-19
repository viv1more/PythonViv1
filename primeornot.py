#WAP to check whether number is prime or not
a=int(input("Enter the Number: "))
if a>2:
    for i in range(2,int (a/2)+1):
        if(a%i)==0:
            print(a," is not a prime number")
            break
        else:
            print(a," is a Prime Number")
            break
elif(a==2):
    print(a, " is  prime number")
else:
    print(a," is not a prime number")