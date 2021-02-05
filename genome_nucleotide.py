import numpy as np
import matplotlib.pyplot as plt

file1 = open('thermophile.fasta', 'r')
Lines = file1.readlines()

count_A = 0
count_C = 0
count_G = 0
count_T = 0

for line in Lines:
    if not line.startswith('>'):
        print(line)

        for i in range(len(line)):
            # print(line[i])
            if line[i] == 'A':
                count_A += 1
                # print("A count: ", count_A)
            if line[i] == 'C':
                count_C += 1
                # print("C count: ", count_C)
            if line[i] == 'G':
                count_G += 1
                # print("G count: ", count_G)
            if line[i] == 'T':
                count_T += 1
                # print("T count: ", count_T)
A_percent = (count_A) / (count_A + count_C + count_G + count_T) * 100
print("A percent is: ", A_percent)
C_percent = (count_C) / (count_A + count_C + count_G + count_T) * 100
print("C percent is: ", C_percent)
G_percent = (count_G) / (count_A + count_C + count_G + count_T) * 100
print("G percent is: ", G_percent)
T_percent = (count_T) / (count_A + count_C + count_G + count_T) * 100
print("T percent is: ", T_percent)
print("GC percent is: ", G_percent + C_percent)
print("AT percent is: ", A_percent + T_percent)

# creating the dataset
data = {'A': A_percent, 'C': C_percent, 'G': G_percent,
        'T': T_percent}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='blue',
        width=0.4)

plt.xlabel("Nucleotides")
plt.ylabel("Percentage of nucleotide Present")
plt.title("Percentage of Each Nucleotide in a Genome Sequence")
plt.show()
