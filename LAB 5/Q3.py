#WAP to print all perfect numbers within the given range
r1=int(input("Enter First Range:"))
r2=int(input("Enter Second Range:"))
print("Perfect Numbers=",end=' ')
for n in range (r1,r2):
    sum=0
    for f in range (1,n):
        if n%f==0:
            sum=sum+f
        if sum==n:
            print(n,end=':')           