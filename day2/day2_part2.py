def proc_elt(elt):
    
    res = elt.strip('\n').split(': ')
    pwd = res[1]
    
    res = res[0].split(' ')
    ltr = res[1].strip()
    
    res = res[0].split('-')
    first_pos = int(res[0]) - 1
    secnd_pos = int(res[1]) - 1

    return (pwd[first_pos] == ltr) ^ (pwd[secnd_pos] == ltr)

if __name__ == '__main__':
    all_pwds_and_reqs = open('./input2.txt').readlines()
    print(sum(map(proc_elt, all_pwds_and_reqs)))
