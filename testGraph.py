import numpy as np
import matplotlib.pyplot as plt

# creating the dataset
data = {'A': 20, 'C': 15, 'G': 30,
        'T': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='blue',
        width=0.4)

plt.xlabel("Nucleotides")
plt.ylabel("Percentage of nucleotide present")
plt.title("Percentage of each Nucleotide in a genome")
plt.show()
