
inputdata=open("Day1_input.txt","r")
lines=inputdata.readlines()
gotit=False


for elements in lines:
    if gotit:
        break
    for otherelements in lines:
        if int(elements)+int(otherelements)==2020:
            gotit=True
            myresult= int(elements)*int(otherelements)
            elements.index
            print("{0} + {1} = 2020 \n{0} * {1} = {2}.".format(int(elements),int(otherelements),myresult))
            break
    next
next