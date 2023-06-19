'''WAP to print pattern
A B C D E D C B A
  A B C D C B A
    A B C B A
      A B A
        A
'''
n=int(input("Enter the number of lines:"))
s=n-1
for i in range(n,0,-1):
    for j in range(1,s+1):
        print(end=" ")
    for j in range(1,i+1):
        print(chr(j+64),end='')
    for j in range(i-1,0,-1):
        print(chr(j+64),end='')
    print()
    s=s+1