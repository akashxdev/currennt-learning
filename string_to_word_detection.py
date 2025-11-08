usr_string=input("Enter a valid string: ")


#space detection fn
def spc_detect(string):
    space=" "
    space_in=[]
    
    for i in range(len(string)):
        if string [i]==space:
            space_in.append(i)
    return space_in

#seperator fn
def slicer(string,fn):
    
    spcd_in=fn(string) #calling spc_detect
    last_str_in=len(string)
    s_pos=0
    
    #words list
    words=[]
    
    #for splicing words
    for i in spcd_in:
        word=string[s_pos:i]
        s_pos=i+1
        words.append(word)
    
    #for end word
    word=string[s_pos:last_str_in]
    words.append(word)
    return words

new_w_lst=(slicer(usr_string,spc_detect))
print (new_w_lst)