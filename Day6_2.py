raw_data=open("Day6_input.txt","r").readlines()
test=["abc\n","\n","a\n","b\n","c\n","\n","ab\n","ac\n","\n","a\n","a\n","a\n","a\n","\n","b\n"]

def common_answers(group_string,number_of_persons):
    common_answer=""
    for char in group_string:
        if group_string.count(char)==number_of_persons and not(char in common_answer):
            common_answer+=char
    next
    return common_answer
    

def group_separation(raw_data):
    group_answers=[]
    raw_data=[lines.strip("\n") for lines in raw_data]
    collect_string=""
    persons_in_group=0
    #seperate group answers from raw_data
    for lines in raw_data:
        if lines=="":
            common=common_answers(collect_string,persons_in_group)
            group_answers.append(common)
            collect_string=""
            persons_in_group=0
        else:
            collect_string+=lines
            persons_in_group+=1
    next
    if collect_string!="":
        common=common_answers(collect_string,persons_in_group)
        group_answers.append(common)
    return group_answers


#add up the number of different answers of the groups
def sumup_group_answers(group_answers):
    sum_answers=0
    for answers in group_answers:
        sum_answers+=len(answers)    
    next

    return sum_answers



#different answers of the groups
common_group_answers=group_separation(raw_data)
sum_of_common_answers=sumup_group_answers(common_group_answers)
print(common_group_answers)
print(sum_of_common_answers)
