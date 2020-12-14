def find_pair(lst, tgt):
    dd = {elt:i for elt, i in zip(lst, range(len(lst)))}
    for k in dd.keys():
        if (tgt - k) in dd:
            return k, tgt - k, dd[k], dd[tgt - k]

    return None 

if __name__ == '__main__':
    input_series = open('./input9.txt').readlines()
    input_series = list(map(lambda x: int(x.strip('\n')), input_series))

    for x in range(25, len(input_series)):
        this_series = input_series[(x-25):x]
        this_val = input_series[x]
        obj = find_pair(this_series, this_val)
        if obj is None:
            break

    print(this_val)

