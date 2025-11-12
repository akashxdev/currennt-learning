def vowl_cons_dtct():
    vowels=("a","e","i","o","u")
    inpt_str=input("one word only\n")
    in_lowr=inpt_str.lower()
    vowels_c=0
    cons_c=0
    for i in in_lowr:
            if i in vowels:
                vowels_c +=1
                #print ("vwl",i)
            else:
                cons_c +=1
                #print("const",i)
    print(f"Vowels={vowels_c}\nCons_c={cons_c}")

vowl_cons_dtct()