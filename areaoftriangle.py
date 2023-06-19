a=float(input("Enter the side a : "))
b=float(input("Enter the side b : "))
c=float(input("Enter the side c : "))

#calculate the semi-perimeter

s=(a+b+c)/2

#calculate the area

area=(s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle %0.3f'%area)
