class Employee:
	def __init__(self,name,emp_id,salary,department):
		self.name = name
		self.emp_id = emp_id
		self.__salary = salary
		self._department = department
	def show_details(self):
		print(f"Employee name : {self.name}")
		print(f"Employee ID : {self.emp_id}")
		print(f"Salary : {self.__salary}")
		
		 
	
	def get_salary(self):
		return f"Salary : {self.__salary}"
	
	def set_salary(self,salary):
		if(salary <= 0):
			return f"Invalid Salary"
		else:
			self.__salary = salary
			return f"Updated Salary : {self.__salary}"

emp1 = Employee("Mehar",60,20000,"development")

print(emp1.get_salary())
print(emp1.set_salary(0))
print(emp1.show_details())