#WAP to find out the factorial of the given number
n=int(input("Enter the number: "))
count=1
fact=1
if n<0:
    print("Factorial Doesnt exist of negative numbers")
elif n==0:
    print("Factorial of 0 is 1")
else:
   # for count in range(1,a+1):
    while(count<=n):
        fact=fact*count
        count=count+1
print("The Factorial of ",n,"is ",fact)    