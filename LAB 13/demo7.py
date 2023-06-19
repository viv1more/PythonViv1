import re
txt="The rain in spain falls mainly in the plain !"
x=re.findall("falls|in",txt)
print(x)
if x:
    print("Yes, there is at least one match")
else:
    print("No there is no match")