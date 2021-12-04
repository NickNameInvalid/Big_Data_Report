from argparse import ArgumentParser
from typing import Set


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument('-k', type=int, required=True)
    parser.add_argument('-t', type=float, required=True, help='similarity lower limit')
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
    "Last Name",
    "First Name",
    "Mid Init",
    "Agency Start Date",
    "Work Location Borough",
    "Title Description",
    "Leave Status as of June 30",
    "Base Salary",
    "Pay Basis",
    "Regular Hours",
    "Regular Gross Paid",
    "OT Hours",
    "Total OT Paid",
    "Total Other Pay"
]


def main():
    arg = get_arguments()
    with open('Big_Data_Report/file_columns.txt', encoding='utf-8') as f:
        lines = f.readlines()
    
    SHINGLES = [k_shingles(c, arg.k) for c in COLUMNS]

    for line in lines:
        line = line.split('\t')
        filename, columns = line[0], line[1]
        if columns == '':
            continue
        if filename.find(DS_NAME) >= 0:
            continue
        
        result = []
        columns = columns.split(',')
        for c1 in columns:
            shingles1 = k_shingles(c1, arg.k)
            for c0, shingles0 in zip(COLUMNS, SHINGLES):
                similarity = jaccard_similarity(shingles0, shingles1)
                if similarity < arg.t:
                    continue

                result.append(f'("{c1}" - "{c0}": {similarity:.2f})')
        
        if len(result) > 0:
            result = ', '.join(result)
            print(f'{filename} {result}')


main()