raw_data=open("Day6_input.txt","r").readlines()
test=[line.replace("\n","") for line in open("Day6_input.txt","r").readlines() if line!="\n"]

def group_separation(raw_data):
    group_answers=[]
    raw_data=[lines.strip("\n") for lines in raw_data]
    collect_string=""
    #seperate group answers from raw_data
    for lines in raw_data:
        if lines=="":
            group_answers.append(collect_string)
            collect_string=""
        else:
            #only add answers not given yet
            for char in lines:
                if collect_string.find(char)<0:
                    collect_string+=char
            next
    next
    if collect_string!="":
        group_answers.append(collect_string)
    return group_answers

#add up the number of different answers of the groups
def sumup_group_answers(group_answers):
    sum_answers=0
    for answers in group_answers:
        sum_answers+=len(answers)    
    next
    return sum_answers

#different answers of the groups
group_answers=group_separation(raw_data)
sum_different_answers=sumup_group_answers(group_answers)
print(sum_different_answers)