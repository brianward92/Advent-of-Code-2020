def find_pair(lst, tgt):
    dd = {elt:i for elt, i in zip(lst, range(len(lst)))}
    for k in dd.keys():
        if (tgt - k) in dd:
            return k, tgt - k, dd[k], dd[tgt - k]

    return None

if __name__ == '__main__':
    input_expenses = open('./input1.txt').readlines()
    input_expenses = list(map(lambda x: int(x.strip('\n')), input_expenses))

    i = 0
    found_pair = False
    while (i < len(input_expenses)) & (not found_pair):
        this_lst = input_expenses[:i] + input_expenses[(i+1):]
        res = find_pair(this_lst, 2020 - input_expenses[i])
        i+= 1
        found_pair = (res is not None)
    
    res1, res2, res3 = res[0], res[1], input_expenses[i-1]
    print(res1, res2, res3, res1 * res2 * res3)

