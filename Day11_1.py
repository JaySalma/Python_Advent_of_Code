import numpy as np
'''import the seat_distribution and replace "L" with
"0", "." with "2" and "#" will be "1"
Then write the lines into the array'''
input_data=[line.strip("\n") for line in open("Day11_input.txt","r").readlines()]
input_data=[line.replace("L","0") for line in input_data]
input_data=[line.replace(".","2") for line in input_data]
no_change=False

seats=np.arange(len(input_data)*len(input_data[0])).reshape(len(input_data),len(input_data[0]))

for rindex,line in enumerate(input_data):
    for cindex,char in enumerate(line):
        seats[rindex,cindex]=char

for rindex,row in enumerate(seats):
    for cindex,column in enumerate(row):
        if column==0:
            seats[rindex,cindex]="L"
        elif column==2:
            seats[rindex,cindex]="."
'''1st rule: every "L"(now "0") becomes "#" (now "1")
if no adjacent seats are taken
2nd rule: if a seat is taken and four or more adjacent seats
are taken too, the seat becomes empty'''

while not no_change:
    current_version=seats.copy()
    free=[]
    occupy=[]
    for rindex,row in enumerate(seats):
        for cindex,current_seat in enumerate(row):
            adjacent_seats=[]
            if rindex==0:
                i=0
            else:
                i=rindex-1
            
            #set limits for the while-loop
            last_row,last_column=np.shape(seats)
            #get the values of the adjacent seats
            while i<rindex+2 and i<last_row:
                if cindex==0:
                    j=0
                else:
                    j=cindex-1
                while j<cindex+2 and j<last_column:
                    if i==rindex and j==cindex:
                        j+=1
                    else:
                        adjacent_seats.append(seats[i,j])
                        j+=1
                i+=1
            
            if current_seat==1 and adjacent_seats.count(1)>=4:
                free.append((rindex,cindex))
            elif current_seat==0 and adjacent_seats.count(1)==0:
                occupy.append((rindex,cindex))
    for position in free:
        seats[position]=0
    for position in occupy:
        seats[position]=1
    
    if (current_version==seats).all():
        no_change=True

print(seats)
occupied_seats=np.sum(seats==1)
print("{} seats are occupied.".format(occupied_seats))