inputdata=open("Day1_input.txt","r")
lines=inputdata.readlines()
gotit=False


for elements in lines:
    if gotit:
        break
    for otherelements in lines:
        if gotit:
            break
        for anotherelements in lines:
            if int(elements)+int(otherelements)+int(anotherelements)==2020:
                gotit=True
                myresult= int(elements)*int(otherelements)*int(anotherelements)
                elements.index
                print("{0} + {1} + {2} = 2020 \n{0} * {1} * {2} = {3}.".format(int(elements),int(otherelements),int(anotherelements),myresult))
                break
        next
    next
next