input_file=open("Day2_input.txt","r")
input_data=input_file.readlines()
valid_passwords=0
number_of_elements=len(input_data)

for element in input_data:
    position_string=(element.split( ))[0]
    first_position=int((position_string.split("-"))[0])-1
    second_position=int((position_string.split("-"))[1])-1
    letter=((element.split( ))[1])[:-1]
    sequence=(element.split( ))[2]
    first_pos_bool=sequence[first_position]==letter
    second_pos_bool=sequence[second_position]==letter
    if first_pos_bool:
        if not second_pos_bool:
            valid_passwords+=1
    elif second_pos_bool:
        valid_passwords+=1
next

print("{} out of the {} passworts are valid".format(valid_passwords,number_of_elements))
