import datetime


'''Following the steps outlined in class and in the slides, you should have a functioning Employee Class

Define your class and include your constructor with any necessary attributes.
Create your string method to display your employee data 
Define a method for a total_expense() function 
Accessor and mutator methods (get and set) for all attributes. 
Test organize and document your class

'''



# Employee Class

class Employee:

     # constructor with __init__
    def __init__(self, name, job_title, department, salary, hire_year):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

        
        
    # Magic methods
    def __str__(self):
          return f"Name: {self.name}, Job Title: {self.job_title}, Department: {self.department}, Salary: {self.salary}, hire_year: {self.hire_year} "

    def years_worked(self):
         today = datetime.datetime.now()
         year = today.year
         return year - self.hire_year
    
    def total_expense(self):
        return self.salary * self.years_worked()
        
        
       
      
        
         
          
               
     # Accessor methods
    def get_name(self):
      return self.name

    def get_job_title(self):
      return self.job_title

    def get_department(self):
      return self.department

    def get_salary(self):
      return self.salary

    def get_hire_year(self):
      return self.hire_year
    
    
    # Mutator methods
    def set_name(self, new_name):
         self.name = new_name

    def set_job_title(self, new_job_title):
         self.job_title = new_job_title

    def set_department(self, new_department):
         self.department = new_department

    def set_salary(self, new_salary):
         self.salary = new_salary

    def set_hire_year(self, new_hire_year):
         self.hire_year = new_hire_year



         


# Class object or instance created
employee_info = Employee("Anthony", "Opeartor", "Vitals", 35.000, 2022)

# Printing employee information 
print(employee_info)


# Printing years worked
print(f"Years worked: {employee_info.years_worked()}")


# Printing total salary expense
print(f"Total salary expense: {employee_info.total_expense()}")


# Printing Accessor method 
# print(employee_info.get_name())
# print(employee_info.get_job_title())
# print(employee_info.get_department())
# print(employee_info.get_salary())
# print(employee_info.get_hire_year())


# Printing Mutator method
# print(employee_info)
# employee_info.set_name("Jean")
# print(employee_info)



































































































