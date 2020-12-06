import string

if __name__ == '__main__':
    
    all_lowercase = string.ascii_lowercase

    all_passengers = open('./input6.txt')

    all_group_counts = []
    this_group = set(all_lowercase)
    this_line = all_passengers.readline()

    while this_line!='':
        this_line = this_line.strip()
        
        if this_line == '':
            all_group_counts.append(len(this_group))
            this_group = set(all_lowercase)
        else:
            this_group = this_group.intersection(set(this_line))

        this_line = all_passengers.readline()

    all_group_counts.append(len(this_group))

    print(sum(all_group_counts))
