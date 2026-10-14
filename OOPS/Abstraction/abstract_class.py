
# from abc import ABC, abstractmethod
# class A(ABC): 
#     @abstractmethod
#     def show(self):
#         print("in a show")

# obj1 = A()
# obj1.show()

# @abstractmethod — marks a method that a concrete child class must implement.

# pass — leaves the method body empty; it does not calculate anything.

# ABC — enables Python's abstract-class mechanism.



from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    # Concrete method
    def show_name(self):
        print("Employee:", self.name)


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return 50000


class ContractEmployee(Employee):

    def calculate_salary(self):
        return 1000 * 20


emp1 = FullTimeEmployee("Mehar")
emp2 = ContractEmployee("Siri")

emp1.show_name()
print("Salary:", emp1.calculate_salary())

emp2.show_name()
print("Salary:", emp2.calculate_salary())
