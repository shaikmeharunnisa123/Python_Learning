
class Employee:
	def __init__(self,name,emp_id):
		self.name = name
		self.emp_id = emp_id
		

class FullTimeEmployee(Employee):
	def __init__(self,name,emp_id,salary,department):
		super().__init__(name,emp_id)
		self.salary = salary
		self.department = department
		
	def show_details(self):
		print(f" Employee name : {self.name}")
		print(f" Employee Id : {self.emp_id}")
		print(f" Salary : {self.salary}")
		print(f" Department : {self.department}")


class ContractEmployee(Employee):
	def __init__(self,name,emp_id,hours,department):
		super().__init__(name,emp_id)
		self.hours = hours
		self.department = department
	def cal_salary(self):
		salary = self.hours * 1000
		return salary 

	def show_details(self):
		print(f" Employee name : {self.name}")
		print(f" Employee Id : {self.emp_id}")
		print(f" Salary : {self.cal_salary()}")
		print(f" Department : {self.department}")




fullTimeEmp = FullTimeEmployee("Mehar",60,20000,"development")
contctEmp = ContractEmployee("Siri",61,40,"testing")

fullTimeEmp.show_details()

contctEmp.show_details()