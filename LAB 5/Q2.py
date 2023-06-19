#WAP to print all prime numbers within the given range
r1=int(input("Enter First Range:"))
r2=int(input("Enter Second Range:"))
print("Prime Numbers=",end=' ')
for n in range (r1,r2+1):
    flag=1
    for j in range (2,n):
        if n%j==0:
            flag=0
            break
        if flag==1:
            print(n,end=':')           