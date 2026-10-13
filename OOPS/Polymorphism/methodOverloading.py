# Method overloading is not supported in Python
# But we can achieve this with the help of
# --->> Default arguments
# --->> *args variable length argument


# If multiple methods have the same name, the latest definition replaces the previous one.

class Demo:
    def add(self,a,b,c=0):
        return a+b+c

    # def add(self,a,b,c):
    #     return a+b+c

d1 = Demo()
print(d1.add(4,7))
print(d1.add(4,7,1))


# With variable length arguments
      
class Demo:
    def add(self,*args):
        total = 0
        for i in args:
            total+=i
        return total

d1 = Demo()
print(d1.add(2,4,7,8,9))
 