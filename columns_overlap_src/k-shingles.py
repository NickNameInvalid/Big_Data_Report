from argparse import ArgumentParser
from typing import Set

import sys

def get_arguments():
    parser = ArgumentParser()
    parser.add_argument('-k', type=int, required=True)
    parser.add_argument('-t', type=float, required=True, help='similarity lower limit')
    parser.add_argument('-n', type=float, required=True, help='min number of overlap columns')
    return parser.parse_args()

def k_shingles(s: str, k: int) -> Set[str]:
    if len(s) <= k:
        return {s}
    else:
        return {s[i:i+k] for i in range(len(s)-k+1)}

def jaccard_similarity(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)

DS_NAME = 'k397-673e'

COLUMNS = [
    "Fiscal Year",
    "Payroll Number",
    "Agency Name",
    "Agency Start Date",
    "Borough",
    "Title Description",
    "Leave Status",
    "Salary",
    "Salaries",
    "Base Salary",
    "Pay Basis",
    "Paid",
    "Regular Hours",
    "Work Hours",
    "OT Hours"
]

# COLUMNS = [
#     "Fiscal Year",
#     "Payroll Number",
#     "Agency Name",
#     "Last Name",
#     "First Name",
#     "Mid Init",
#     "Agency Start Date",
#     "Work Location Borough",
#     "Title Description",
#     "Leave Status as of June 30",
#     "Base Salary",
#     "Pay Basis",
#     "Regular Hours",
#     "Regular Gross Paid",
#     "OT Hours",
#     "Total OT Paid",
#     "Total Other Pay"
# ]



def main():
    arg = get_arguments()
    out_file = open("../sim_columns.txt", "w")
    # sys.stdout = out_file
    with open('../overlap_metadata/file_columns.txt', encoding='utf-8') as f:
        lines = f.readlines()
    
    SHINGLES = [k_shingles(c.upper(), arg.k) for c in COLUMNS]

    for line in lines:
        line = line.split('\t')
        filename, columns = line[0], line[1].rstrip()
        if columns == '':
            continue
        if filename.find(DS_NAME) >= 0:
            continue
        
        result = []
        line_similarity = 0.0
        columns = columns.split(',')
        for c1 in columns:
            shingles1 = k_shingles(c1.upper(), arg.k)
            for c0, shingles0 in zip(COLUMNS, SHINGLES):
                similarity = jaccard_similarity(shingles0, shingles1)
                if similarity < arg.t:
                    continue
                line_similarity += similarity
                # result.append(f'({c1},{c0}: {similarity:.2f})')
                result.append(f'{c1},{c0}')
                # result.append(f'("{c1}" - "{c0}": {similarity:.2f})')
        
        if line_similarity > arg.n:
            result = '\t'.join(result)
            print(f'{filename} {result}')
            out_file.write(f'{filename}\t{result}\n')
    out_file.close()


if __name__ == '__main__':
    main()