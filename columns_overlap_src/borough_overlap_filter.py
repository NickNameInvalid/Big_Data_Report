lines = []

for line in open('../sim_columns.txt'):
    line_split = line.strip().split('\t')
    filename = line_split[0]
    cols = []
    should_append = False
    for col in line_split[1 : ]:
        col_split = col.split(',')
        ori_col = col_split[1].rstrip()
        ds_col = col_split[0].rstrip()
        cols.append((ori_col, ds_col))
        if ori_col == "Work Location Borough":
            should_append = True
    if should_append:
        lines.append((filename, cols))

for i in lines:
    print(i)