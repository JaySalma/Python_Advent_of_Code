from operator import eq

number_memory=[9,3,1,0,8,4]


for i in range(6,30000000):
    most_recent=number_memory[-1]
    if number_memory.count(most_recent)<=1:
        number_memory.append(0)
    else:
        for index in range(len(number_memory)-2,-1,-1):
            if number_memory[index]==most_recent:
                new_number=len(number_memory)-1-index
                number_memory.append(new_number)
                break
    if number_memory.__len__()%10000==0:
        print(number_memory.__len__())
    '''if number_memory.__len__()%2==0:
        half_nummem=int(number_memory.__len__()/2)
        sequence=number_memory[:half_nummem]
        index=0
        while sequence[index]==number_memory[index+half_nummem]:
            if index==half_nummem-1:
                #print("match")
                break
            else:
                index+=1
        if index==half_nummem-1:
            print("sequence returning:")
            print(sequence)'''
        

print("the 30000000th number is: {}".format(number_memory[30000000-1]))
