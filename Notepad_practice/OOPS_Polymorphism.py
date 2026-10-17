class Employee:
	def __init__(self,name,emp_id,salary,department):
		self.name = name
		self.emp_id = emp_id
		self.salary = salary
		self.department = department
	def cal_salary(self):
		base = self.salary
		return base


class Manager(Employee):
	def __init__(self,name,emp_id,salary,department):
		super().__init__(name,emp_id,salary,department)
	def cal_salary(self):
		base  = self.salary
		bonus = 50000
		salary = base + bonus
		return salary

emp1 = Employee("Mehar",60,200000,"development")

mngr = Manager("Mehar",60,200000,"development")

print(emp1.cal_salary())

print(mngr.cal_salary())