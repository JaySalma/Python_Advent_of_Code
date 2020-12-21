input_data=[line.strip("\n") for line in open("Day13_input.txt","r").readlines()]

def get_busses(input):
    lines_raw=input[1]
    line=""
    bus_lines=[]
    for char in lines_raw:
        if char!="x" and char!=",":
            line+=char
        elif char=="," and line!="":
            bus_lines.append(int(line))
            line=""
    next
    if not line=="":
        bus_lines.append(int(line))
        line=""
    return bus_lines

earliest_departure=int(input_data[0])
departure_time=earliest_departure
bus_lines=get_busses(input_data)
bus_id=0

while True:
    for time in bus_lines:
        if departure_time%time==0:
            bus_id=time
            time_waiting=departure_time-earliest_departure
            break
    if bus_id!=0:
        break
    departure_time+=1

print("i have to wait {} minutes, then i get on bus {}"\
    .format(time_waiting,bus_id))
print("bus_id * waiting time = {}".format(time_waiting*bus_id))