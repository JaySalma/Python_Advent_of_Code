'''
input_data=open("test_input.txt","r").readlines()
acc=0
already_run=[]
line=0
'''
input_data=[i.strip("\n") for i in open("Day8_input.txt","r").readlines()]
code_finished=False
jmp_index=[input_data.index(i) for i in input_data if i.startswith("jmp")]


while not code_finished:
    input_data=[i.strip("\n") for i in open("Day8_input.txt","r").readlines()]
    input_data[jmp_index[0]]=input_data[jmp_index[0]].replace("jmp","nop")
    jmp_index.pop(0)
    acc=0
    already_run=[]
    line=0
    
    while line<len(input_data):
        
        #edit acc
        if input_data[line].startswith("acc"):
            amount=input_data[line].strip("acc ")
            if amount.startswith("+"):
                acc+=int(amount[1:])
            elif amount.startswith("-"):
                acc-=int(amount[1:])
        
        #detect jmp
        if input_data[line].startswith("jmp"):
            amount=input_data[line].strip("jmp ")
            if amount.startswith("+"):
                line+=int(amount[1:])
            elif amount.startswith("-"):
                line-=int(amount[1:])
        else:
            line+=1
        
        #check, if line already run, else add to lines already run
        if line in already_run:
            break
        elif line==len(input_data)-1:
            code_finished=True
        else:
            already_run.append(line)


print(acc)
