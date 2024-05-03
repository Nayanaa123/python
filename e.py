file=open("b.txt","w")
sel=int(input("sel a number(1 add,2 sel, 3 edit,4 del)"))
def add():
    if sel==1:
        n=input("enter a name")
        file.write(n+"\n")
        print(n+ "added successfully")
add()