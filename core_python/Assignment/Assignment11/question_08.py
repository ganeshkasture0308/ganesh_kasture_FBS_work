rows = 10
cols = 10
count = 100

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(count)
        count -= 1
    if i % 2 == 0:
        row.reverse()
    print('\t'.join(str(x) for x in row))
