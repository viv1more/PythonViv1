#WAP to print all armstrong numbers within the given range
r1=int(input("Enter First Range:"))
r2=int(input("Enter Second Range:"))
print("Armstrong Numbers=",end=':')
for n in range(r1,r2):
    sum=0
    p=len(str(n))
    n1=n
while(n1>0):
    d=n1%10
    sum=sum+(d**p)
    n1=int(n1/10)
    if(n==sum):
        print(n,end="")