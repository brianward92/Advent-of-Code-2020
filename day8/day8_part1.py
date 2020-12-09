all_instructions = open('./input8.txt').readlines()

cur_acc = 0
# acc just add i to acc
# nop just ignore
# jmp i index back i places

i_set = set()
cur_i = 0

while cur_i not in i_set:
    this_instruction = all_instructions[cur_i]
    
    i_set = i_set.union(set([cur_i]))

    this_instruction = this_instruction.strip().split(' ')

    i_type = this_instruction[0]
    i_len = int(this_instruction[1])

    if i_type == 'nop':
        cur_i+= 1
    elif i_type == 'acc':
        cur_i+= 1
        cur_acc+= i_len
    elif i_type == 'jmp':
        cur_i+= i_len
    else:
        raise ValueError

print(cur_acc)
