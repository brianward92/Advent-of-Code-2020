import sys
def proc_slope(all_rows, row_len, col_skip, row_skip = 1):
    
    x = 0
    count = 0
    for elt in all_rows[row_skip::row_skip]:
        x+=col_skip
        count+=(elt[x%row_len]=='#')

    return count

if __name__ == '__main__':
    all_rows = list(map(lambda x: x.strip('\n'), open('./input3.txt').readlines()))
    all_lens = list(set(map(len, all_rows))) 
    assert len(all_lens) == 1
    row_len = all_lens[0]

    res11 = proc_slope(all_rows, row_len, 1, 1)
    res31 = proc_slope(all_rows, row_len, 3, 1)
    res51 = proc_slope(all_rows, row_len, 5, 1)
    res71 = proc_slope(all_rows, row_len, 7, 1)
    res12 = proc_slope(all_rows, row_len, 1, 2)
    
    print(res11 * res31 * res51 * res71 * res12)
