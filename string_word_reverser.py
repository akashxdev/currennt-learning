in_str=input()
spl=list(in_str.split(" ")) #spliting into words
rev_lst=[] #store list items in rev
addin_in=len(spl)
for i in spl:
    rev_lst.append(spl[addin_in-1])
    addin_in -=1

rev_str= " ".join(rev_lst)
print (rev_str) #printing reversed str