address={"name":"nayana","name2":"mki","name3":"maths"}
sel=int(input("sel a num(1 edit,2 select,3 del,4add)"))
if sel==1:
    n=input("enter a name")
    m=input("rnter a value")
    address[n]=m
    print(address)
elif sel==2:
    n=input("enter a value to sel")
    print(address[n]) 
elif sel==3: 
    n=input("enter a n to del")
    del address[n]   
    print(address)
else:
    n=input("enter a name")
    address["name4"]=n
    print(address)    


