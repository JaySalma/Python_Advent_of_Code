passport_file=open("Day4_input.txt","r")
raw_data=passport_file.readlines()

def check_passport(passport):
    
    #check if nessasarry fields are present
    if not ((len(passport)==8 or (len(passport)==7 and passport.get("cid")==None))):
        valid=False
        return valid

    #check Birth Year (1920-2002 valid)
    if not int(passport.get("byr")) in range(1920,2003):
        valid=False
        return valid
    #check Issue Year (2010-2020 valid)
    if not int(passport.get("iyr")) in range(2010,2021):
        valid=False
        return valid
    #check Expiration Year (2020-2030 valid)
    if not int(passport.get("eyr")) in range(2020,2031):
        valid=False
        return valid
    #check Height (150-193cm and 59-76in valid)
    if not ((passport.get("hgt").endswith("cm") and\
        int(passport.get("hgt")[:-2]) in range(150,194)) or\
            ((passport.get("hgt").endswith("in") and\
        int(passport.get("hgt")[:-2]) in range(59,77)))):
        valid=False
        return valid
    #check Hair Color ("#"+6 characters(0-9 or a-f) valid)
    valid_hairchar="abcdef0123456789"
    if not (len(passport.get("hcl"))==7 and\
        passport.get("hcl").startswith("#")\
    and [i in valid_hairchar for i in passport.get("hcl")[1:]]):
        valid=False
        return valid
    #check Eye Color (amb blu brn gry grn hzl oth valid)
    valid_eyes=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport.get("ecl") in valid_eyes:
        valid=False
        return valid
    #check Passport ID (leading "0" and 9 charachters valid)
    #passport.get("pid").startswith("0")\and 
    if not (len(passport.get("pid"))==9 and\
            [i in "0123456789" for i in passport.get("pid")] ):
        valid=False
        return valid

    valid=True
    return valid


def passport_get(raw_data):
    passport={}
    valid_passports=0
    for lines in raw_data:
        if lines=="\n":
            if check_passport(passport):
                valid_passports+=1
            passport.clear()
        else:
            passport_fields=lines.split()
            {passport.update({field.split(":")[0]:field.split(":")[1]}) for field in passport_fields}            
    next
    if passport!={}:
        if check_passport(passport):
                valid_passports+=1
    return valid_passports

print(passport_file.name.replace(".txt","")+" contains {} valid passports".format(passport_get(raw_data)))

