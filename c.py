n=open("b.py","a")
def add():
    name=input("enter a name")
    place=input("enter a place")
    phone=int(input("enter a phn"))
    n.write("name :"+name+"\nplace :"+place+"\nphone :"+str(phone)+"")
    print(name+ "details added successfuly")
for a in range(4):
    add()
