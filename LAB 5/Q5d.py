'''
        1
       121
      12321
     1234321 
'''
n=int(input("Enter number of lines:"))
s=n-1
for i in range(1,n+1):
    for j in range(1,s+1):
        print(end=' ')
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
    s=s-1