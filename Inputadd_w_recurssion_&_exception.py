def inpt_add():
    try:
        inpt=input("Use only numarical values without any space or comma.\nInput=") #take str in input
        add=0
        for i in inpt:
            add +=int(i) #int type conversion
        print ("Sum=",add)
    except ValueError:
        print ("Invalid input")
        inpt_add()#for auto fn call if error occured 

#calling fn
inpt_add()