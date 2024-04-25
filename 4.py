name=[]
def start():
    sel=int(input("sel a num(1add,2sel,3edit,4del,5exit)"))
    if sel==1:
        n=input("enter a name")
        name.append(n)
        print(name)
        start()    
    elif sel==2:
        n=input("select a name")
        if n in name:
            print(n)
        else:
            name.append(n)
            print(name)    
        data=name.index(n)
        print("name of index value",name[data])
        start()
    elif sel==3:
        n=input("enter a name to replace ")
        m=input("enter a name to be replaced")
        if n in name:
            data=name.index(n)
            name[data]=m
            print(name)
        else:
            print("not i n list",n)    
        start()
    elif sel==4:
        n=input("enter a name to del")
        data=name.index(n)
        del name[data]
        print(name)    
        start()
    else:
        exit()
start()         
