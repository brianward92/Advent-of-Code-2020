def proc_passenger_id(row_or_col, upper_id, id_len):
    return sum([(2 ** i) * (half == upper_id) for half, i in zip(row_or_col, range(id_len - 1, -1, -1))])

if __name__ == '__main__':
    all_passengers = open('./input5.txt')
    this_passenger = all_passengers.readline().strip()
    passenger_ids = []
    while this_passenger!='':
        this_row = this_passenger[:-3]
        this_col = this_passenger[-3:]
        this_row = proc_passenger_id(this_row, 'B', 7)
        this_col = proc_passenger_id(this_col, 'R', 3)
        passenger_ids.append(this_row * 8 + this_col)
        this_passenger = all_passengers.readline().strip()

    print(max(passenger_ids))
