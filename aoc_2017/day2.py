import sys

def day2_1(spreadsheet):
    sum = 0
    for row in spreadsheet:
        row_min = sys.maxsize
        row_max = 0
        for cell in row:
            if cell < row_min:
                row_min = cell
            if cell > row_max:
                row_max = cell
        sum += row_max - row_min
    return sum

def day2_2(spreadsheet):
    sum = 0
    for row in spreadsheet:
        sum += calc_row(row)
    return sum

def calc_row(row):
    for i in range(0, len(row)):
        for j in range(i, len(row)):
            if i != j:
                max_val = max(row[i], row[j])
                min_val = min(row[i], row[j])
                if max_val % min_val == 0:
                    return max_val // min_val
    raise Exception("uh, oh!")
