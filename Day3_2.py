input_file=open('Day3_input.txt','r')
input_matrix=input_file.readlines()
horizontal_position=0
trees_hit=list()
rows_hit=list() #rows, where I hit a tree
variants_to_check=((1,1),(3,1),(5,1),(7,1),(1,2)) #(to right,down)-combinations

def check_hits(matrix,to_right,down):
    horizontal_position=0
    hits=0
    for element in matrix:
        #check the line step
        if matrix.index(element)%down==0:
            if horizontal_position>=(len(element)-1):
                horizontal_position=horizontal_position-(len(element)-1)
            if element[horizontal_position]=="#":
                hits+=1
                rows_hit.append(input_matrix.index(element)+1)
            horizontal_position+=to_right
    next
    return hits

def multipy_elements(list_of_numbers):
    product=1
    for i in list_of_numbers:
        product=product*i
    return product

def answer(number_of_hits):
    i=1
    answer=""
    product=multipy_elements(number_of_hits)
    
    for elements in number_of_hits:
        if answer=="":
            answer="number of hits multiplied: "+ str(elements)
        else:
            answer=answer+" * " +str(elements)
    next

    answer=answer+" = "+str(product)
    return answer



for i in variants_to_check:
    trees_hit.append(check_hits(input_matrix,i[0],i[1]))
next
print(answer(trees_hit)) 