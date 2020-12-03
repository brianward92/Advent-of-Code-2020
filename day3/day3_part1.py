if __name__ == '__main__':
    all_rows = list(map(lambda x: x.strip('\n'), open('./input3.txt').readlines()))
    
    all_lens = list(set(map(len, all_rows)))
    
    assert len(all_lens) == 1

    row_len = all_lens[0]

    x = 0
    count = 0
    for elt in all_rows[1:]:
        x+=3
        count+=(elt[x%row_len]=='#')

    print(count)
