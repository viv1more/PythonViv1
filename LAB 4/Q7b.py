# 1²+2²+3²+4²
n=int (input("Enter n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i*i
    print(i,"^",2,end='+')
print('=',sum)