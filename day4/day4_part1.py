def check_passport(passport):
    passport = passport.strip()
    return all([(key + ':') in passport for 
        key in ['byr','iyr','eyr','hgt','hcl','ecl','pid']])

if __name__ == '__main__':
    all_passports = open('./input4.txt').readlines()
    ct=0
    this_pass = ''
    for row in all_passports:
        row = row.strip()
        this_pass+= ' ' + row
        if (row == ''):
            ct+= check_passport(this_pass)
            this_pass = ''

    ct+= check_passport(this_pass)
    print(ct)
