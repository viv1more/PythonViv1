#xy^n+x2y^n-1/(n-1)+x^3y^n-2/(n-2)
n=int (input("Enter n:"))
x=int (input("Enter x:"))
y=int(input("Enter y:"))
sum=1
t=n
for i in range(1,n+1):
    fact=1
    for j in range (1,t+1):
        fact=fact*j
        sum=sum+(x**i)*(y**t)/fact
    print("x**",i,"y**",t,"/",fact,end='+')
    t=t-1
print('=',sum)