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






# class Employee:
#     def __init__(self, name, emp_id, salary, department):
#         self.name = name                  # Public
#         self._department = department     # Protected
#         self.__salary = salary            # Private
#         self.emp_id = emp_id              # Public

#     def show_details(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Department:", self._department)
#         print("Salary:", self.__salary)

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, new_salary):
#         if new_salary > 0:
#             self.__salary = new_salary
#             print("Salary updated successfully")
#         else:
#             print("Invalid salary")


# class Manager(Employee):
#     def show_department(self):
#         print("Department:", self._department)


# # Create an employee object
# emp = Employee("Mehar", 101, 50000, "IT")

# # PUBLIC: access directly
# print("Name:", emp.name)
# print("Employee ID:", emp.emp_id)

# # PROTECTED: accessible, but intended for internal/subclass use
# print("Department:", emp._department)

# # PRIVATE: access through a method
# print("Salary:", emp.get_salary())

# # Update private salary through a method
# emp.set_salary(60000)
# print("Updated salary:", emp.get_salary())

# # Child class can access the protected attribute
# manager = Manager("Ravi", 102, 80000, "HR")
# manager.show_department()

# # Uncomment the next line to see an AttributeError:
# # print(emp.__salary)
