#reverse any input string
in_str=input("Give input string:")
spl=list(in_str.split(" ")) #spliting into words


def reverse_str (in_lst):
    rev_lst=[] #store list items in rev
    
    #method:1 slicing
    #for i in in_lst[::-1]: #slicing directly
    #    rev_lst.append(i)

    #method:2 reversed()
    for i in reversed(in_lst): #reversing list directly
        rev_lst.append(i)
        
    rev_str= " ".join(rev_lst) #.join method for joining an itrable
    return rev_str
    
print ("Reversed string:",reverse_str(spl)) #printing reversed str