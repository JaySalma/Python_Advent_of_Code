def get_row(string_code):
    row_range=(0,128)
    row_code=string_code[:-3]
    for char in row_code:
        lower_limit=row_range[0]
        upper_limit=row_range[1]
        spread=upper_limit-lower_limit
        if char=='F':
            row_range=(lower_limit,upper_limit-0.5*spread)
        elif char=='B':
            row_range=(lower_limit+0.5*spread,row_range[1])
        else:
            print('invalid code')
    next
    row=int(row_range[0])
    return row

def get_column(string_code):
    column_code=string_code[-3:]
    column_range=(0,8)
    for char in column_code:
        lower_limit=column_range[0]
        upper_limit=column_range[1]
        spread=upper_limit-lower_limit
        if char=='L':
            column_range=(lower_limit,upper_limit-0.5*spread)
        elif char=='R':
            column_range=(lower_limit+0.5*spread,column_range[1])
        else:
            print('invalid code')
    next
    column=int(column_range[0])
    return column

def get_seat_id(row,column):
    seat_id=8*row+column
    return seat_id

boarding_passes=open("Day5_input.txt","r").readlines()
boarding_passes=[passes.replace("\n","") for passes in boarding_passes]
high_seat_id=0

for passes in boarding_passes:
    row=get_row(passes)
    column=get_column(passes)
    seat_id=get_seat_id(row,column) 
    if seat_id>high_seat_id:
        high_seat_id=seat_id
        high_row=row
        high_column=column
next

print(high_row,high_column,high_seat_id)

