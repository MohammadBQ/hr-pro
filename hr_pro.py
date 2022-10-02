class Employee:

   def __init__(self, name, age, salary, employment_years):
    self.name = name 
    self.age = age 
    self.salary = salary
    self.employment_years = employment_years
   

        

    def get_annual_salary(self, annual_salary):
        return self.annual_salary == self.salary * 12


    def __init__(self, employees):
        self.employees = employees
        employees = []
        self.employees.append(Employee("Khalid", 34, 373, "8 years"))
        self.employees.append(Employee("Aziz", 57, 4356, "13 years"))


    

    print(self.employees)
    
    


    def __str__(self):
        return Employee


       




         

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, get_annual_salary, bonus_percentage):
        super().__init__(name, age, salary, employment_years, get_annual_salary)
        self.bonus_percentage == bonus_percentage

    
    def __init__(self, managers):
        self.managers = managers
        managers = []
        managers.append(Manager("Rashid", 34, 2727, "7 yyears"))
        managers.append(Manager("Hamad", 23, "9 years of employment"))

    
   
    
        
    def get_bonus(self, bonus):
        return self.bonus == self.bonus_percentage * self.salary

    def __str__(self):
        return Manager

    
employees_options = ["Show employees", "Show managers", "Add an employee", "Add a manager"]
 










def main():
    print("Welcome to HR Pro\n Options:")
    for i in employees_options:
        print(employees_options.index(i) +1, end=' ')
        print(" ",i)
    what_you_do = input("What will you like to do ?")
    print(what_you_do)
    
    if input == 1:
        print(Employee("Khalid", 34, 373, "8 years"))
        print(Employee("Aziz", 57, 4356, "13 years"))
    if input == 2:
        print(Manager)

    


   

if __name__ == '__main__':
	main()
