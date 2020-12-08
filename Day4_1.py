passport_file=open("Day4_input.txt","r")
raw_data=passport_file.readlines()
#valid_passports=0

def check_passport(passport):
    valid=False
    if ((len(passport)==8 or (len(passport)==7 and passport.get("cid")==None))):
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

'''
#collect the data for a passport in one list-->separate passports
def passport_data_collector(raw_data):
    #short_memory=[]
    #passports=[]
    for lines in raw_data:
        if lines=="\n":
            passport_dict={i.split(":")[0]:i.split(":")[1] for i in short_memory}
            passports.append(passport_dict)
            short_memory=[]
            next
        else:
            passport_fields=lines.split()
            [short_memory.append(field) for field in passport_fields]
            
    next
    if short_memory!=[]:
        passport_dict={i.split(":")[0]:i.split(":")[1] for i in short_memory}
        passports.append(passport_dict)
    return passports
'''


