#Write a program to add digits of the number of given numbers

n=int(input("enter the number:"))
sum=0
str=str(n)
for i in str:
    sum=sum+(int(i))
print("Sum of Digits of number",n,"is",sum)