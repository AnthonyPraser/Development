import datetime

'''
Classes
'''


class Point2d:
    pass

class Date:

    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    # __str__ this is what the user will see if they use the print built in function
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
        

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.year == other.year:
            return True
        return False
        

    def __lt__(self, other):
        selfdate = datetime(self.year, self.month, self.day)
        otherdate = datetime(other.year, other.month, other.day)
        if selfdate < otherdate:
            return True
        return False
        

    def is_leap_year(self):
          
          return True if self.year % 4 == 0 and (self.year % 100  != 0 or self.year % 400 == 0) else False
         
         
    
# Sample data
sample_date = Date()
date1 = Date(1985, 5, 19)
date2 = Date(2001, 10, 3)

# tested with __str__
# print(sample_date)
# print(date1)
# print(date2)

# testing __eq__
# print(date1 == date2)

# testing __it__
# print(date1 < date2)

# print(date1.is_leap_year())
# print(date2.is_leap_year())







class Point2d:

    ''' This docstring can be 
    displayed as well'''

    # constructor with __init__
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Magic methods
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
         return Point2d(self.x - other.x, self.y - other.y)
    
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Accessor Methods - returns an attribute to the user
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y




    # Mutator Methods - lets the user change the attribute
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


        


my_first_point = Point2d(10, 7) # class object or instance created
my_second_point = Point2d(11, 10)
my_fifth_point = Point2d(50, 100)

# Printing after adding __str__ magic method
# print(my_first_point)
# print(my_second_point)

# Equality __eq__

# print(my_first_point == my_second_point)

# Addition __add__
# my_third_point = my_first_point + my_second_point
# print(my_third_point)

# Subtraction __sub__
# my_fourth_point = my_first_point - my_second_point
# print(my_fourth_point)

# Less than __lt__
# print(my_first_point < my_second_point)

# Aceessor method
# print(my_first_point.get_x())
# print(my_second_point.get_x())
# print(my_fifth_point.get_x())

# print(my_first_point.get_y())
# print(my_second_point.get_y())
# print(my_fifth_point.get_y())

# Lets look at default parameters
# default_object = Point2d()
# print(default_object)


# Mutator method
# print(my_fifth_point)
# my_fifth_point.set_x(120) # mutator method changes x
# print(my_fifth_point)

# my_fifth_point.set_y(200)
# print(my_fifth_point)

# Doc String __doc__
# print(Point2d.__doc__)

    

class Dog:
    # Our constructor

    def __init__(self, name, birth_year, breed):
        self.name = name
        self.birth_year = birth_year
        self.breed = breed

    # String representation, this is what happens
    def __str__(self):
        return f'Name: {self.name}\nBirth year:{self.birth_year}\nBreed: {self.breed}'
    
    # This function will calculate the dog's human age
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return year - self.birth_year
    
    # This is using the return value from human_age(), we can make the function call, in another function 
    def show_results_from_another_function(self):
        return 100 * self.human_age()
    
    def dog_years(self):
        dogyears = 7 * self.human_age()
        return f'{self.name} is {dogyears} years old'
        

    


dog1 = Dog('fluffy', 2020, 'chihuhua')
dog2 = Dog('chino', 2015, 'japanese chin')
dog3 = Dog('fido', 2018, 'doberman')


# print(dog1)
# print(dog2)
# print(dog3)

# Human age
# print(dog1.human_age())


# testing call from another function 
print(dog1.show_results_from_another_function())




today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day

# print(year)
# print(month)
# print(day)




























































