class first:
    def one(self):
        print("its first program")
class second():
        def two(self):
             print("its second program")
class third(first,second):
     def three(self):
          print("its third program")
x=third()
x.one()
x.two()
x.three()