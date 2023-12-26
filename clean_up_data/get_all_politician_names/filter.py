import re

f = open("parliament_list.txt", "r")
x=f.read()
arr = x.splitlines()

# print(arr)

for i in re.findall("(.*?)</a>", str(arr)):
    print(i)


