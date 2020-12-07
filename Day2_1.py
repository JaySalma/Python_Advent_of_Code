input_file=open("Day2_input.txt","r")
input_data=input_file.readlines()
valid_passwords=0
number_of_elements=len(input_data)

for element in input_data:
    element_range=(element.split( ))[0]
    minimum=int((element_range.split("-"))[0])
    maximum=int((element_range.split("-"))[1])
    letter=((element.split( ))[1])[:-1]
    sequence=(element.split( ))[2]
    if sequence.count(letter) in range(minimum,maximum+1):
        valid_passwords+=1
next

print("{} out of the {} passworts are valid".format(valid_passwords,number_of_elements))
