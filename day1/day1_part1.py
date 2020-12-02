def find_pair(lst, tgt):
    dd = {elt:i for elt, i in zip(lst, range(len(lst)))}
    for k in dd.keys():
        if (tgt - k) in dd:
            return k, tgt - k, dd[k], dd[tgt - k]

    return None

if __name__ == '__main__':
    input_expenses = open('./input1.txt').readlines()
    input_expenses = list(map(lambda x: int(x.strip('\n')), input_expenses))
    
    k, j, id1, id2 = find_pair(input_expenses, 2020)
    print(k, j, k * j)

