# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
file = open(fname,"r")
ans = 0
count = 0
for line in file:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                ans = ans + float(line[20:])
                count = count + 1
print("Average spam confidence:", ans/count) 