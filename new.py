def data(a,b,c,d):
    global total
    global avg 
    global per 
    global mul
    global div
    total=a+b+c+d 
    avg=total/4
    per=total*100/400
    mul=a*b*c*d
    div=a/b/c/d
def total():
        print("Total :",total)
def avg():
        print("Avg :",avg)  
def per():
        print("percent:",per)
def grade():
       if per>=90:
             print("a",per)
       elif per>=70:
             print("b",per)
       elif per>=50:
             print("c",per)
       else:
              print("d",per)
def mul():
       print("multiple",mul) 
def div():
       print("divide",div)                   

                                


        