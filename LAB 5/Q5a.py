#WAP to print pattern
'''
1 1 1 1
2 2 2 
3 3 
4
'''
n=int(input("Enter the number of lines:"))
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(k,end=" ")
    print()
    k=k+1