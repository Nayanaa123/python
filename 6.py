def data(a,b):
    global c
    global d
    global e
    global f
    c=a+b
    d=a-b
    e=a*b
    f=a//b
def sum():
    print("sum:",c)
def sub():
    print("subrate:",d)
def mul():
    print("multiple:",e)
def div():
    print("divide:",f)
a=int(input("enter a num"))
b=int(input("enter a num"))
data(a,b)
sum() 
sub()
mul()
div()               