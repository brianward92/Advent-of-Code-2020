import sys

if __name__ == '__main__':
    tgt = int(sys.argv[1])
    input_series = open('./input9.txt').readlines()
    input_series = list(map(lambda x: int(x.strip('\n')), input_series))
    cur_sum = input_series[0]
    i1 = 0
    i2 = 0
    while (cur_sum != tgt) & (i2 < len(input_series)):
        if cur_sum < tgt:
            i2+=1
            cur_sum+=input_series[i2]
        else:
            cur_sum-=input_series[i1]
            i1+=1

    if cur_sum == tgt:
        obj = input_series[i1:(i2+1)]
        print(min(obj)+max(obj))
    else:
        print('Could not find such a pair.')

