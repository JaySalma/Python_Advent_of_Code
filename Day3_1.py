input_file=open('Day3_input.txt','r')
input_matrix=input_file.readlines()
horizontal_position=0
trees_hit=0
rows_hit=list() #rows, where I hit a tree
for element in input_matrix:
    print(len(element))
#when index bigger than line lengh, start from begin
    if horizontal_position>=(len(element)-1):
        horizontal_position=horizontal_position-(len(element)-1)
    if element[horizontal_position]=="#":
        trees_hit+=1
        rows_hit.append(input_matrix.index(element)+1)
    horizontal_position+=3
next

print('on the way down I hit {} trees in the rows: '.format(trees_hit))
print(rows_hit)

