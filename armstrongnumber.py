#WAP to check wether the given number is armstrong or not
n=int(input("Enter the Number: "))
temp=n
p=0
sum=0
while(temp>0):
    temp=int(temp/10)
    p=p+1
temp=n
count=1
while(count<=p):
    d=temp%10
    temp=int(temp/10)
    sum=sum+(d**p)
    count=count+1
    
if  sum==n:
    print(n," is Armstrong Number: ")
else:
    print(n," is not Armstrong Number: ")