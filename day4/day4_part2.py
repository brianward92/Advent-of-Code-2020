import pandas as pd

def passport_str_to_dict(passport):
    passport = passport.strip()
    passport = passport.split(' ')
    dd = {str(elt.split(':')[0]):str(elt.split(':')[1]) for elt in passport}
    return dd

if __name__ == '__main__':
    all_passports = open('./input4.txt').readlines()
    dict_passports = []
    this_pass = ''
    for row in all_passports:
        row = row.strip()
        this_pass+= ' ' + row
        if (row == ''):
            dict_passports.append(passport_str_to_dict(this_pass))
            this_pass = ''

    dict_passports.append(passport_str_to_dict(this_pass))
    df_pass = pd.DataFrame(dict_passports)
    del df_pass['cid']
    
    idx = df_pass.isnull().sum(axis=1) == 0
    
    idx&= df_pass['byr'].str.len() == 4
    tmp_byr = df_pass['byr'].fillna('0').astype(int)
    idx&= (tmp_byr >= 1920) & (tmp_byr <= 2002)
    
    idx&= df_pass['iyr'].str.len() == 4
    tmp_iyr = df_pass['iyr'].fillna('0').astype(int)
    idx&= (tmp_iyr >= 2010) & (tmp_iyr <= 2020)
    
    idx&= df_pass['eyr'].str.len() == 4
    tmp_eyr = df_pass['eyr'].fillna('0').astype(int)
    idx&= (tmp_eyr >= 2020) & (tmp_eyr <= 2030)
    
    tmp_hgt = df_pass['hgt'].str.replace('cm','').str.replace('in','').fillna('0').astype(int)
    
    idx_cm = df_pass['hgt'].str.endswith('cm')
    idx_cm&= (tmp_hgt >= 150) & (tmp_hgt <= 193)
    
    idx_in = df_pass['hgt'].str.endswith('in')
    idx_in&= (tmp_hgt >= 59) & (tmp_hgt <= 76)
    
    idx&= idx_cm | idx_in

    valid_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    idx&= df_pass['ecl'].isin(valid_colors)
    
    idx&= df_pass['hcl'].str.startswith('#')
    idx&= df_pass['hcl'].str.slice(1,).str.isalnum()
    
    idx&= df_pass['pid'].str.len() == 9
    
    print(idx.sum())
