name=["adhi","kasi","adhik"]
sel=int(input("select a num (1 add,2 sel,3 edit,4 delect)"))
if sel==1:
    n=input("enter a name")
    name.append(n)
    print(name)
elif sel==2:
    n=input("select a name")
    data=name.index(n)
    print("name of index value",name[data])
elif sel==3:
    n=input("enter a name to replace ")
    m=input("enter a name to be replaced")
    data=name.index(n)
    name[data]=m
    print(name)
else:
    n=input("enter a name to reple")
    data=name.index(n)
    del name[data]
    print(name)   
 
