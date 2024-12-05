# fin = open("input_d1_p1_p1","r")
fin = open(r"2023/Day 1/input_d1_p1_p1.txt", "r")

total = 0 # keep track of total sum
for line in fin.readlines():
    for i in range(len(line)):
        if line[i] in "0123456789":
            first = line[i]
            break
    for i in range(1, len(line) + 1): # reverse
        if line[-i] in "0123456789":
            last = line[-i]
            break
    total += int(first + last)

print(total)