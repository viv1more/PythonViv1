#Write a program to print the sum of n natural numbers

n=int(input("Enter n:"))
sum=0
for i in range (1,n+1):
    sum=sum+i
    print(i,end='+')
print('=',sum)