# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
x = open("ActivitySet#1/resum.txt")
x=x.read()
y = sum([int(i) for i in re.findall("[0-9]+",x)])
print(y)
#sol: 317750