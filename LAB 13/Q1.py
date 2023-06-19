import re
txt="Sky is only Limit of the Programmer in year 2022"
x=re.findall("[A-Z]",txt)
y=re.findall("[0-9]",txt)
z=re.findall("[a-z]",txt)
t=re.findall("[m-s]",txt)
r=re.findall("/d",txt)
print(r)
print(x)
print(y)
print(z)
print(t)