import numpy as np
'''import the seat_distribution and replace "L" with
"0", "." with "2" and "#" will be "1"
Then write the lines into the array'''
input_data=[line.strip("\n") for line in open("Day11_input.txt","r").readlines()]
input_data=[line.replace("L","0") for line in input_data]
input_data=[line.replace(".","2") for line in input_data]
no_change=False

seats=np.arange(len(input_data)*len(input_data[0])).reshape(len(input_data),len(input_data[0]))
#fill the array with input
for rindex,line in enumerate(input_data):
    for cindex,char in enumerate(line):
        seats[rindex,cindex]=char

'''1st rule: every "L"(now "0") becomes "#" (now "1")
if no visible seats are taken
2nd rule: if a seat is taken and for or more visible seats
are taken too, the seat becomes empty

            123
directions: 4O5 
            678
'''

while not no_change:
    current_version=seats.copy()
    free=[]
    occupy=[]
    #limits of array
    last_row,last_column=np.shape(seats)
    for rindex,row in enumerate(seats):
        for cindex,current_seat in enumerate(row):
            visible_seats=[]
        #direction1:
            for i in range(rindex-1,-1,-1):
                j=i-(rindex-cindex)
                if j<0:
                    break
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction2:
            for i in range(rindex-1,-1,-1):
                j=cindex
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction3:
            for i in range(rindex-1,-1,-1):
                j=(rindex+cindex)-i
                if j>=last_column:
                    break
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction4:
            for j in range(cindex-1,-1,-1):
                i=rindex
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction5:
            for j in range(cindex+1,last_column):
                i=rindex
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction6:
            for i in range(rindex+1,last_row):
                j=(rindex+cindex)-i
                if j<0:
                    break
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction7:
            for i in range(rindex+1,last_row):
                j=cindex
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
        #direction8:
            for i in range(rindex+1,last_row):
                j=i-(rindex-cindex)
                if j>=last_column:
                    break
                if not seats[i,j]==2:
                    visible_seats.append(seats[i,j])
                    break
            #devide, if seat will get free or occupied
            if current_seat==1 and visible_seats.count(1)>=5:
                free.append((rindex,cindex))
            elif current_seat==0 and visible_seats.count(1)==0:
                occupy.append((rindex,cindex))

    for position in free:
        seats[position]=0
    for position in occupy:
        seats[position]=1
    
    if (current_version==seats).all():
        no_change=True


occupied_seats=np.sum(seats==1)
print("{} seats are occupied.".format(occupied_seats))