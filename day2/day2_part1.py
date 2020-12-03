def proc_elt(elt):
    
    res = elt.strip('\n').split(': ')
    pwd = res[1]
    
    res = res[0].split(' ')
    ltr = res[1].strip()
    
    res = res[0].split('-')
    n_min = int(res[0])
    n_max = int(res[1])
    
    count = pwd.count(ltr)

    return (n_min <= count) & (count <= n_max)

if __name__ == '__main__':
    all_pwds_and_reqs = open('./input2.txt').readlines()
    print(sum(map(proc_elt, all_pwds_and_reqs)))
