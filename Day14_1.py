#masks=[mask.strip("mask = ") for mask in open("Day14_input.txt","r").readlines() if mask.startswith("mask")]
#masks=[mask.strip("\n") for mask in masks]
#mem_strings=[mem.strip("\n") for mem in open("Day14_input.txt","r").readlines() if mem.startswith("mem")]
#print(masks,mem)
input_data=[line.strip("\n") for line in open("Day14_input.txt","r").readlines()]

def decimal_to_binary(number):
    powers=[]
    while number>0:
        if number%2==1:
            powers.append(1)
        else:
            powers.append(0)
        number//=2
    powers.reverse()
    return powers

def binary_to_decimal(sequence):
    to_power=0
    decimal=0
    if type(sequence)==str:
        sequence=[digit for digit in sequence]
    sequence.reverse()
    for digit in sequence:
        decimal+=2**to_power*int(digit)
        to_power+=1

    return decimal

def get_mem(mem_string):
    mem_index=int(mem_string[mem_string.find("[")+1:mem_string.find("]")])
    mem_value=int(mem_string[mem_string.find("=")+2:])
    return mem_index,mem_value

def get_mask(sequence):
    mask=sequence.strip("mask = ")
    '''position_zero=[]
    position_one=[]
    for index,char in enumerate(mask):
        if char=="0":
            position_zero.append(index)
        elif char=="1":
            position_one.append(index)'''
    return mask


#lengh of mem_list
max_index=0
for line in input_data:
    if line.startswith("mem"):
        index=int(get_mem(line)[0])
        if index>max_index:
            max_index=index


#all addresses initialized to 0
mem=[0 for i in range(0,max_index+1)]


for line in input_data:
    if line.startswith("mask"):
        mask=get_mask(line)
    else:
        mem_index,mem_value=get_mem(line)
        mem_binary=decimal_to_binary(mem_value)
        for i in range(len(mask)-len(mem_binary)):
            mem_binary.insert(0,0)
        
        for index,char in enumerate(mask):
            if char=="1":
                mem_binary[index]=1
            elif char=="0":
                mem_binary[index]=0
        mem_value=binary_to_decimal(mem_binary)
        mem[mem_index]=mem_value

mem_sum=sum(mem)
print("the sum of all values in the mem_list = {}".format(mem_sum))
  


