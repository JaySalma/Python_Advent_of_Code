#Day10_input
input_data=[int(i.strip("\n")) for i in open("Day10_input.txt","r").readlines()]
built_in_device=max(input_data)+3
#input_data.append(built_in_device)
input_data.insert(0,0)
sorted_input=sorted(input_data)
space=[]
multiplicator_list=[]
variations=1
diff1_row=0

#get the spaces between the elements of the list
for index,item in enumerate(sorted_input):
    if index<len(sorted_input)-1:
        next_item=sorted_input[index+1]
        space.append(next_item-item)


#get the multiplyer corresponding with the consicutive one_spaces
for spaces in space:
    if spaces==1:
        diff1_row+=1
    else:
        if diff1_row==2:
            multiplicator_list.append(2)
        elif diff1_row>=3:
            multiplicator=(2**(diff1_row-3))*3+1
            multiplicator_list.append(multiplicator)
        diff1_row=0
if diff1_row==2:
    multiplicator_list.append(2)
elif diff1_row>=3:
    multiplicator=(2**(diff1_row-3))*3+1
    multiplicator_list.append(multiplicator)
diff1_row=0


for multiplyers in multiplicator_list:
    variations*=multiplyers
print(variations)
        