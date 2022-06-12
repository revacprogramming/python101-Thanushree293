# Strings
    # """012345678901234567890"""
text = "X-DSPAM-Confidence:    0.8475"
Pos=text.find(':')
print(Pos)
c=Pos+1
print(c)
value=text[Pos+1:]#it should be 5
print(value)
result=float(value)#instead use print(float(value))
print(result)