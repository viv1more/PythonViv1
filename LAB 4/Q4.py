#Write a program to print the sum of n given numbers with number

n=int(input("enter the n:"))
sum=0
for i in range(n):
    num=int(input("Enter Number:"))
    sum=sum+num
    print(num,end='+')
print("=",sum )