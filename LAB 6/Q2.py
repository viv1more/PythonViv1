'''WAP to create list of natural numbers and perform following things
a)print all natural numbers b)print odd numbers c)print even numbers'''
L=[]
it=0
n=int(input("Enter Total Elements: "))
for i in range(n):
    it=it+1
    L.append(it)
print("List ",L)
print("Even Numbers=",L[1:n:2])
print("Odd Numbers=",L[0:n:2])

#d)Table of 4
l=[]
m=4
for  i in range(m,m*10+1,m):
    l.append(i)
print("Table of 4 ")
print(l)

#e)Table of 14
l=[]
m=14
for  i in range(m,m*10+1,m):
    l.append(i)
print("Table of 14 ")
print(l)

#f)Table of 'n' number
l=[]
v=int(input("Enter the number:"))
for i in range(v,v*10+1,v):
    l.append(i)
print(l)