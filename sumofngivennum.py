#WAP to find out the sum of n given numbers
n=int(input("Enter n: "))
count=1
sum=0
while(count<=n):
    num=int(input("Enter Number: "))
    sum=sum+num
    count=count+1
print("sum = ",sum)