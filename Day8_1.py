input_data=open("test_input.txt","r").readlines()
input_data=[i.strip("\n") for i in input_data]
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
    else:
        already_run.append(line)
print(acc)
