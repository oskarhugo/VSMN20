from tabulate import tabulate

table = []

for i in range(0,110,10):
    row = [i,5*(i-32)/9]
    table.append(row)

print(tabulate(table, headers=['Grader C','Grader F']))