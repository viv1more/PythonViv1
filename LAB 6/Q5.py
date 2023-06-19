#write a python program reverse a string
s=input("Enter String:")
s1=""
print("Original String=",s)
for i in s:
    s1=i+s1
print("Reverse String=",s1)