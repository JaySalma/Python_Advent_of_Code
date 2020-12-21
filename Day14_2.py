#masks=[mask.strip("mask = ") for mask in open("Day14_input.txt","r").readlines() if mask.startswith("mask")]
#masks=[mask.strip("\n") for mask in masks]
#mem_strings=[mem.strip("\n") for mem in open("Day14_input.txt","r").readlines() if mem.startswith("mem")]
#print(masks,mem)
input_data=[line.strip("\n") for line in open("Day14_input.txt","r").readlines()]

def decimal_to_binary(number):
    #binary=""
    powers=[]
    while number>0:
        if number%2==1:
            #binary="1"+binary
            powers.append(1)
        else:
            #binary="0"+binary
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
    return mask

#collect the variants of the sequence by replacing "X" and sum the variants together
def get_variants_sum(sequence):
    
    variations=[sequence.copy()]
    index=0
    while index<2**sequence.count("X")-1:
        while "X"  in variations[index]:
            variations.insert(index+1,variations[index].copy())
            X_index=variations[index].index("X")
            variations[index][X_index]=1
            variations[index+1][X_index]=0
        index+=1
    mem_addresses=[]
    for variant in variations:
        mem_addresses.append(binary_to_decimal(variant))

    return mem_addresses


#lengh of mem_list
max_index=0
for line in input_data:
    if line.startswith("mem"):
        index=int(get_mem(line)[0])
        if index>max_index:
            max_index=index


#all addresses initialized to 0
mem_addresses=[]
mem=[]


for line in input_data:
    if line.startswith("mask"):
        mask=get_mask(line)
    else:
        mem_index,mem_value=get_mem(line)
        mem_binary=decimal_to_binary(mem_index)
        for i in range(len(mask)-len(mem_binary)):
            #mem_binary="0"+mem_binary
            mem_binary.insert(0,0)
        
        for index,char in enumerate(mask):
            if char=="1":
                mem_binary[index]=1
            elif char=="X":
                mem_binary[index]="X"
        for address in get_variants_sum(mem_binary):
            if address in mem_addresses:
                mem[mem_addresses.index(address)]=mem_value
            else:
                mem_addresses.append(address)
                mem.append(mem_value)
                
mem_sum=sum(mem)
print(mem_sum)
  


