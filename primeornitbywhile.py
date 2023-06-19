#wap to check the number is prime ornot
n=int(input("Enter the number: "))
count=2
flag=1
while(count<n):
    if n%count==0:
        print(n, ' is not Prime number')
        flag=0
        break
    else:
        count=count+1
if flag==1:
    print(n,' is Prime number')
