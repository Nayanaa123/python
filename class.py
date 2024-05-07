class student:
    def data(self,a,b,u,v):
        self.a=a
        self.b=b
        self.u=u
        self.v=v
    def sum(self):
        self.c=self.a+self.b+self.u+self.v
        print("total",self.c)
    def average(self):
        self.n=self.c//4
        print("average",self.n)
    def percent(self):
        self.m=self.c*100//400
        print("percentage",self.m)
x=student()
a=int(input("enter a first mark"))
b=int(input("enter a second mark"))
u=int(input("enter a third mark"))
v=int(input("enter a fourth mark"))
x.data(a,b,u,v)                       
x.sum()
x.average()
x.percent()

