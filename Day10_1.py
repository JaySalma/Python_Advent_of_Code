input_data=[int(i.strip("\n")) for i in open("Day10_input.txt","r").readlines()]
built_in_device=max(input_data)+3
input_data.append(built_in_device)
sorted_input=sorted(input_data)
voltage=0
difference_one=0
difference_two=0
difference_three=0

for adapters in sorted_input:
    if adapters-voltage>3:
        print("Difference is too high!")
        break
    elif adapters-voltage==1:
        difference_one+=1
    elif adapters-voltage==2:
        difference_two+=1
    else:
        difference_three+=1
    voltage=adapters
next

print("difference=1: {} times\ndifference=3: {} times".format(difference_one,difference_three))
#print("diff1*diff3 = {}".format(difference_one*difference_three))
print("difference=2: {} times".format(difference_two))
print(len(sorted_input))