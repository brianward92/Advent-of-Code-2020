if __name__ == '__main__':
    all_passengers = open('./input6.txt')

    all_group_counts = []
    this_group = set()
    this_line = all_passengers.readline()

    while this_line!='':   
        this_line = this_line.strip()
        this_group = this_group.union(set(this_line))
        if this_line == '':
            all_group_counts.append(len(this_group))
            this_group = set()
        this_line = all_passengers.readline()

    all_group_counts.append(len(this_group))

    print(sum(all_group_counts))
