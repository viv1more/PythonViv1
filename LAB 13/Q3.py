import re
txt="The rain in spain"
x=re.findall("r\Bain",txt)
print(x)
if x:
    print("Yes, there is at least one match")
else:
    print("No there is no match")