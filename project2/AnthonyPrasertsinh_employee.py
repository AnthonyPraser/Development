



'''Following the steps outlined in class and in the slides, you should have a functioning Employee Class

Define your class and include your constructor with any necessary attributes.
Create your string method to display your employee data 
Define a method for a total_expense() function 
Accessor and mutator methods (get and set) for all attributes. 
Test organize and document your class

'''



# Employee Class

class Point2d:

     # constructor with __init__
    def __init__(self, name = "Anthony", job_title = "Operator", 
                 department = "Vitals", salary = 35.000, hire_year = 2022):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year
        
    # Magic methods
    def __str__(self):
            return f"{self.name}, {self.job_title}, 
            {self.department}"
        
    # Accessor methods
    def get_name(self):
            return self.name
        






























































































