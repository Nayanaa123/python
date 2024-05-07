#class student:
    #def name(self):
       # print("student name:nayana")
    #def phone(self):
       # print("student phone:3298574")
#x=student()
#x.name()
#x.phone()        
class calculation:
    def data(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        print("sum",c)
    def sub(self):
        c=self.a-self.b
        print("sub",c) 
    def multi(self):
        c=self.a*self.b
        print("multiply",c)
    def div(self):
        c=self.a//self.b
        print("div",c)    
x=calculation()
x.data(20,40)
x.sum()
x.sub()
x.multi()
x.div()        