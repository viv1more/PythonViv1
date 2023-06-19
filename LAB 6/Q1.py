#WAP to create user defined list and display it
L=[]
n=int(input("Enter Total Elements: "))
it=0
for i in range (n):
    it=int(input("Enter Element: "))
    L.append(it)
print("List: ",L) 