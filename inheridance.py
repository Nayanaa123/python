class first:
    def one(self):
        print("its first program")
class second(first):
        def two(self):
             print("its second program")
class fourth:
     def four(self):
          print("its fourth program")
class third(second,fourth):
     def three(self):
          print("its third program")
x=third()
x.one()
x.two()
x.three()
x.four()


