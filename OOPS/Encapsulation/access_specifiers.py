class Employee:
    def __init__(self,name,emp_id,salary,department):
        self.name = name  #Public
        self.emp_id = emp_id # public
        self._department = department # Protected
        self.__salary = salary # private
    
    def get_salary(self):
        return self.__salary

class FullTimeEmployee(Employee):
    def get_department(self):
        return self._department

    
    def get_salary(self):
        return self.__salary
    
emp1 = Employee("Lahari",75,20000,"development")
fullTimeEmp = FullTimeEmployee("Siri",59,20000,"development")



print(emp1.name)   # Public Specifiers
print(emp1.emp_id)

print(emp1._department)           # Protected
print(fullTimeEmp.get_department())

print(emp1.get_salary())            # Private


# print(emp1.__salary)  ## This will throw an Attribute error



# print(fullTimeEmp.get_salary()) This will throw an error