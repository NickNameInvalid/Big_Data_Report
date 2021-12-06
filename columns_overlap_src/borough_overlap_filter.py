lines = []

for line in open('../sim_columns.txt'):
    line = line.strip().split('\t')[0]
    filename = line[0]
    for col in line[1 : ]:
