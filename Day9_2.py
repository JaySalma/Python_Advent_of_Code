input_data=[int(i.strip("\n")) for i in open("Day9_input.txt","r").readlines()]
#valid_number=False
step_width=25
i=0
invalid=False

def find_invald(number_list):
    for n in range(step_width,len(input_data)):
        valid_number=False
        sum=input_data[n]
        for i in  range(n-step_width,n-1):
            first_summand=input_data[i]
            for j in range(i+1,n):
                second_summand=input_data[j]
                if sum==first_summand+second_summand:
                    valid_number=True
                    break
            next
            if valid_number==True:
                break
        next
        if not valid_number:
            first_invalid=sum
            first_invalid_index=input_data.index(sum)
            break
    next
    return first_invalid

'''functions, that iterates the given number until it finds the 
the a list with continguous numbers that sum up to the invalid
number. This list is returned'''
def contiguous_sum(number_list,invalid_number):
    invalid_index=number_list.index(invalid_number)
    for i in range(invalid_index-2):
        list_summands=number_list[i:invalid_index-1]
        while sum(list_summands)!=invalid_number and list_summands!=[]:
            list_summands=list_summands[:-1]
        if sum(list_summands)==invalid_number:
            break
    next
    return list_summands

def encryption_weakness(list_summands):
    encryp_weakness=max(list_summands)+min(list_summands)
    return encryp_weakness

invalid_number=find_invald(input_data)
print("the first invalid number is {} (index {} of the input list.".format(invalid_number,input_data.index(invalid_number)))

contiguous_list=contiguous_sum(input_data,invalid_number)
weakness=encryption_weakness(contiguous_list)
print("the weakness of the XMAS-encrypted list is {}".format(weakness))