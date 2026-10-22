def next_row(row):
        rowL = [0] + row
        rowR = row + [0]
        pairs = zip(rowL, rowR)
        sums = []
        for pair in pairs:
            total = pair[0] + pair[1] 
            sums.append(total)
        return sums

def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        smaller = rows(row_count - 1)
        previous = smaller[-1]
        new = next_row(previous)
        return smaller + [new]
    
