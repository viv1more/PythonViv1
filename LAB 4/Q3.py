#Write a program to print the sum of first n odd numbers

n=int(input("enter the n:"))
sum=0
for i in range(n,2*n+1,2):
    sum=sum+i
    print(i,end='+')
print("=",sum)