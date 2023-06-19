import re
txt="The rain in spain"
x=re.findall("\AThe",txt)
print(x)
if x:
    print("Yes, there is  match")
else:
    print("No there is no match")