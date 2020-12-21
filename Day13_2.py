input_data=[line.strip("\n") for line in open("Day13_input.txt","r").readlines()]

#get the bus lines and the difference in departure time t
def get_busses(input):
    lines_raw=input[1]
    line=""
    bus_lines=[]
    t_plus=[]
    t=0
    for char in lines_raw:
        if char!="x" and char!=",":
            line+=char
        elif char==",":
            if line!="":
                bus_lines.append(int(line))
                line=""
                t_plus.append(t)
            t+=1
    next
    if not line=="":
        bus_lines.append(int(line))
        line=""
        t_plus.append(t)
    return bus_lines,t_plus

bus_lines,t_plus=get_busses(input_data)
bus_id=0

timestamp=(100000000000000//bus_lines[0])*bus_lines[0]

timestamp_found=[False for line in bus_lines]
step=1
index=0
while False in timestamp_found:
    timestamp+=step
    for i in range(index,len(bus_lines)):
        if (timestamp+t_plus[index])%bus_lines[i]==0:
            step*=bus_lines[i]
            timestamp_found[index]=True
            index+=1  
        else:
            break
    print(timestamp)
    

print(timestamp)