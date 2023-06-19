l=int(input("Enter the Lowwest Range: "))
h=int(input("Enter the Highest Range: "))

print("Prime numbers in the given Range are :")

for num in range(l,h+1):
    if num>1:
        for i in range(2,num):
            if(num %i)==0:
                break
            else:
                print(num)
                break