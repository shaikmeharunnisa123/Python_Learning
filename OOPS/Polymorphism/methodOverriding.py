# method overriding -- Runtime polymorphism

# Method overriding is implemented in inheritance only
# Method name and parameters are same but 
# the behaviour of the method is going to change from parent class to child class

class Employee:
    '''This is parent class'''
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self): # This is the default behaviour for every employee
        return self.base_salary # this will return base salry

class Manager(Employee):
    '''This is child class which is inheriting properties
     from Employee class'''
    def __init__(self,name,base_salary,bonus):
        super().__init__(name,base_salary) # Pull in name and base salary from parent constructor
        self.bonus = bonus

    def calculate_salary(self):
        base  = super().calculate_salary()
        return base + self.bonus

emp =  Employee("Mehar",100000)
mgr = Manager("Mehar",100000,30000)
print(emp.calculate_salary())
print(mgr.calculate_salary())
