number_memory=[9,3,1,0,8,4]

for i in range(0,2020):
    most_recent=number_memory[-1]
    if number_memory.count(most_recent)<=1:
        number_memory.append(0)
    else:
        for index in range(len(number_memory)-2,-1,-1):
            if number_memory[index]==most_recent:
                new_number=len(number_memory)-1-index
                number_memory.append(new_number)
                break
    if i%100==0:
        sequence=[number_memory[0]]
        index=0
        while number_memory.count(sequence)>1:
            index+=1
            sequence.append(number_memory[index])
        sequence.pop(-1)
        if number_memory.count(sequence)*len(sequence)==len(number_memory):
            print("sequence found")

print(number_memory)
print("the 30000000th number is: {}".format(number_memory[2020-1]))
