input_data=[line.strip("\n") for line in open("Day12_input.txt","r").readlines()]

waypoint_position=[10,1,0,0] #start position waypoint [east,north,west,south]
ship_position=[0,0,0,0] #start position ship [east,north,west,south]

for instruction in input_data:
    '''if direction_index<0:
        direction_index+=4
    elif direction_index>3:
        direction_index-=4'''
    if instruction.startswith("F"):
        units=int(instruction[1:])
        for index,direction in enumerate(ship_position):
            ship_position[index]+=units*waypoint_position[index]
    elif instruction.startswith("E"):
        units=int(instruction[1:])
        waypoint_position[0]+=units
    elif instruction.startswith("N"):
        units=int(instruction[1:])
        waypoint_position[1]+=units
    elif instruction.startswith("W"):
        units=int(instruction[1:])
        waypoint_position[2]+=units
    elif instruction.startswith("S"):
        units=int(instruction[1:])
        waypoint_position[3]+=units
    elif instruction.startswith("R"):
        units=int(int(instruction[1:])/90)
        waypoint_position=[waypoint_position[units-4],waypoint_position[1+units-4],\
            waypoint_position[2+units-4],waypoint_position[3+units-4]]
    elif instruction.startswith("L"):
        units=int(int(instruction[1:])/90)
        waypoint_position=[waypoint_position[-units],waypoint_position[1-units],\
            waypoint_position[2-units],waypoint_position[3-units]]

north=ship_position[1]-ship_position[3]
east=ship_position[0]-ship_position[2]

manhattan_distance=abs(north)+abs(east)
print("manhattan distance = "+str(manhattan_distance))