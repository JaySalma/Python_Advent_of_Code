input_data=[line.strip("\n") for line in open("Day12_input.txt","r").readlines()]

#values for 4 directions
north=0
east=0
west=0
south=0

directions=[east,north,west,south]
direction_index=0 #start direction is east

for instruction in input_data:
    if direction_index<0:
        direction_index+=4
    elif direction_index>3:
        direction_index-=4
    if instruction.startswith("F"):
        units=int(instruction[1:])
        directions[direction_index]+=units
    elif instruction.startswith("E"):
        units=int(instruction[1:])
        directions[0]+=units
    elif instruction.startswith("N"):
        units=int(instruction[1:])
        directions[1]+=units
    elif instruction.startswith("W"):
        units=int(instruction[1:])
        directions[2]+=units
    elif instruction.startswith("S"):
        units=int(instruction[1:])
        directions[3]+=units
    elif instruction.startswith("R"):
        units=int(int(instruction[1:])/90)
        direction_index-=units
    elif instruction.startswith("L"):
        units=int(int(instruction[1:])/90)
        direction_index+=units

north=directions[1]-directions[3]
east=directions[0]-directions[2]

manhattan_distance=abs(north)+abs(east)
print("manhattan distance = "+str(manhattan_distance))