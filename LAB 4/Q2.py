##Write a program to print the sum of first n even numbers
n=int(input("Enter the N:"))
sum=0
for i in range(2,2*n+1,2):
    sum=sum+i
    print(i,end='+')
print("=",sum)