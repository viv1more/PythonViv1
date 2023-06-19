import re
txt= "SIBAR is my favourite college"
x=re.findall("^SIBAR",txt)
y=re.findall("college$",txt)
if x:
    print("Yes, the string starts with 'SIBAR'")
else:
    print("No match")
if y:
    print("Yes, the string ends with 'college'")
else:
    print("No match")