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



invalid_number=find_invald(input_data)
print("the first invalid number is {} (index {}) of the input list.".format(invalid_number,input_data.index(invalid_number)))
