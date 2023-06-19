#Write a program to reverse digits of the number of given numbers

n=int(input("enter the number:"))
sum=0
rv=''
st=str(n)
for i in st:
    rv=i+rv
r=int(rv)
print("Reverse Number of ",n,"is",r)