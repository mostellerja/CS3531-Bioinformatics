import random
import math
d = 3
n = 2

all_rows = []
max_rows = math.pow(n+1, d)

while len(all_rows) < max_rows:
    row = []

for i in range(d):
    row.append(random.randint(0, n))

    print(row)

    if not all_rows.__contains__(row):
        all_rows.append(row)

print(sorted(all_rows))
