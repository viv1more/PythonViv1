import re
txt="The rain in Spain"
x=re.search("^The.*Spain$", txt)
if x:
    print("\nYes ! We have a match\n")
else:
    print("No match")