#WAP to find double factorial of given number
#5!!=1!*2!*3!*4!*5!
n=int(input("Enter n:"))
df=1
for cnt in range(1,n+1):
    fact=1
    for j in range(1,n+1):
        fact=fact*j
df=df*fact
print("Double factorial of",n,"is",df)