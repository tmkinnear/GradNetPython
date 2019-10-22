# Model solution for exercise 12 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

with open('read_in_example.csv','r') as f:
    fdata = f.read().split('\n')

col1 = []
col2 = []
col3 = []
for line in fdata:
    split_line = line.split(',')
    col1.append(int(split_line[0]))
    col2.append(int(split_line[1]))
    col3.append(int(split_line[2]))

mean1 = sum(col1) / len(col1)
mean2 = sum(col2) / len(col2)
mean3 = sum(col3) / len(col3)
print("means:", mean1, mean2, mean3)

min1 = min(col1)
min2 = min(col2)
min3 = min(col3)
print("minima:", min1, min2, min3)

max1 = max(col1)
max2 = max(col2)
max3 = max(col3)
print("maxima:", max1, max2, max3)

if mean1 == max(mean1, mean2, mean3):
    print("The first column has the highest mean")
elif mean2 == max(mean1, mean2, mean3):
    print("The second column has the highest mean!")
else:
    print("The third column has the highest mean!")
