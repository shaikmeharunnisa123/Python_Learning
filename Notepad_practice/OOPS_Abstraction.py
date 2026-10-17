
from abc import ABC,abstractmethod

class Employee(ABC):

	def __init__(self,name,emp_id,salary,department):
		self.name = name
		self.emp_id = emp_id
		self.salary = salary
		self.department = department
	@abstractmethod
	def calculate_salary(self):
		pass 
		

class FullTimeEmployee(Employee):
	
	def calculate_salary(self):
		base = self.salary
		return base+10000

fullTimeEmp = FullTimeEmployee("Mehar",60,20000,"development")

print(fullTimeEmp.calculate_salary())