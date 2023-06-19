import re
txt= "SIBAR is my favourite college"
x=re.findall("S.*R",txt)
y=re.findall("f.*te",txt)
'''if x:
    print("Yes, the string starts with 'SIBAR'")
else:
    print("No match")
if y:
    print("Yes, the string ends with 'college'")
else:
    print("No match")'''
print(x)
print(y)