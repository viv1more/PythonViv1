
#WAP to solve quadratic equation ex. x²+2x-3=0
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

d=(b**2)-(4*a*c)
sq=d**0.5
print("Value of Discriminant is: ",sq)
sol1=(-b+sq)/(2*a)
sol2=(-b-sq)/(2*a)
print("The roots are: ",sol1,"and ",sol2)


