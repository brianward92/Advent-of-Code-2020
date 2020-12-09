from split import partition

def check_row_rule(row_rule):
    res = map(lambda x: x[2:],
              row_rule.strip().split(
                  ' contain ')[1].replace('bags','bag').replace('.','').split(', '))
    return res

if __name__ == '__main__':

    ll = open('./input7.txt').readlines()

    contain_gold, may_contain_gold = partition(
        lambda x: 'shiny gold' in x.strip().split(' contain ')[1], ll)

    contain_gold = list(contain_gold)
    may_contain_gold = list(may_contain_gold)

    ct = len(contain_gold)
    bag_set = set(map(lambda x: x.split(' contain ')[0].replace('bags','bag'), contain_gold))



    while contain_gold:
        contain_gold, may_contain_gold = partition(
            lambda x: any([elt in bag_set for elt in check_row_rule(x)]), may_contain_gold)

        contain_gold = list(contain_gold)
        may_contain_gold = list(may_contain_gold)

        ct+= len(contain_gold)
        bag_set = set(map(lambda x: x.split(' contain ')[0].replace('bags','bag'), contain_gold))

    print(ct)

