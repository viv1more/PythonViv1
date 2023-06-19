#WAP to check wether the given numberis perfect no or not
n=int(input("enter the number: "))
count=1
sum=0
while(count<n):
    if n%count==0:
        sum=sum+count
    count+=1
if sum==n:
    print(n," is perfect number")
else:
    print(n," is not perfect number")